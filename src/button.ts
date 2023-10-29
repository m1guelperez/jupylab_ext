import { requestAPI } from './handler';
import { ToolbarButton } from "@jupyterlab/apputils";
import { DocumentRegistry } from "@jupyterlab/docregistry";
import { INotebookModel, NotebookPanel } from "@jupyterlab/notebook";
import { IDisposable } from "@lumino/disposable";
import { insert_labels_into_notebook } from "./utils";


export class ButtonExtension implements DocumentRegistry.IWidgetExtension<NotebookPanel, INotebookModel> {

    createNew(panel: NotebookPanel): IDisposable {
        // Create the toolbar button
        let mybutton = new ToolbarButton({
            label: 'Label Notebook',
            onClick: () => {
                let notebook = panel.content.model;
                let cells = notebook?.cells;
                let length = cells?.length;

                let notebookContent = {
                    cells: [] as any[]
                };

                // Iterate through each cell and log its content
                for (let i = 0; length !== undefined && i < length; i++) {
                    let cell = cells?.get(i);
                    if (cell) {
                        let source = cell.toJSON().source;
                        let cellContent: string[] = [];

                        if (typeof source === 'string') {
                            cellContent = source.split('\n');
                        } else if (Array.isArray(source)) {
                            cellContent = source;
                        }

                        notebookContent.cells.push({
                            cell_type: cell.type,
                            source: cellContent
                        });
                    }
                }
                // Continue with the original onClick function
                requestAPI<any>('label-notebook', {
                    body: JSON.stringify(notebookContent),
                    method: 'POST',
                })
                    .then(data => {
                        console.log(data);
                        insert_labels_into_notebook(panel, data)
                    })
                    .catch(reason => {
                        console.error(
                            `The notebook_labeling server extension appears to be missing.\n${reason}`
                        );
                    })
            }
        });

        panel.toolbar.insertItem(10, 'label notebook', mybutton);
        return mybutton;
    }
}
