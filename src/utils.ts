import { NotebookPanel, NotebookActions } from '@jupyterlab/notebook';

interface NotebookCell {
    cell_type: "markdown" | "code";
    metadata?: { position?: number };
    source: string[];
}

interface LabeledNotebook {
    cells: NotebookCell[];
}

export function insert_labels_into_notebook(panel: NotebookPanel, labeled_notebook: LabeledNotebook) {
    if (panel.content.model?.cells.length === undefined || panel.content.model?.cells.length === 0) {
        console.log("No cells in notebook");
        alert("No cells in notebook");
        return;
    }

    let markdownIndiceList: number[] = [];
    labeled_notebook.cells.forEach((cell, index) => {
        if (cell.cell_type === "markdown" && cell.metadata?.position !== undefined) {
            markdownIndiceList.push(index);
            panel.content.activeCellIndex = cell.metadata?.position!;
            NotebookActions.insertAbove(panel.content);
        }
    });
    setTimeout(() => {
        for (let i = 0; i < labeled_notebook.cells.length; i++) {
            if (labeled_notebook.cells[i].cell_type === "markdown") {
                panel.content.activeCellIndex = i + 1;
                NotebookActions.selectAbove(panel.content);
                NotebookActions.replaceSelection(panel.content, labeled_notebook.cells[i].source.join('\n'));
            }
        }
    }, 0);

    setTimeout(() => {
        for (let idx of markdownIndiceList) {
            panel.content.activeCellIndex = idx;
            NotebookActions.changeCellType(panel.content, "markdown");
            NotebookActions.run(panel.content);
        }
    }, 0);
}   