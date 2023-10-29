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

    if (panel.content.model?.cells.length === undefined || panel.content.model?.cells.length === 0) {
        console.log("No cells in notebook");
        alert("No cells in notebook");
        return;
    }
    // panel.content.activeCellIndex = 0;
    // NotebookActions.insertAbove(panel.content);
    // panel.content.activeCellIndex = 1;
    // NotebookActions.selectAbove(panel.content);
    // // setTimeout(() => {
    // //     NotebookActions.replaceSelection(panel.content, "### Test");
    // // }, 1000);
    // NotebookActions.replaceSelection(panel.content, "### Test");

    // panel.content.activeCellIndex = 0;
    // NotebookActions.changeCellType(panel.content, "markdown");


    // setTimeout(() => {
    //     panel.content.activeCellIndex = 0;
    // }, 1000);
    // setTimeout(() => {
    //     NotebookActions.insertAbove(panel.content);
    // }, 2000);
    // setTimeout(() => {
    //     panel.content.activeCellIndex = 5;
    // }, 3000);
    // setTimeout(() => {
    //     panel.content.activeCellIndex = 1;
    // }, 4000);
    // setTimeout(() => {
    //     NotebookActions.selectAbove(panel.content);
    // }, 5000);
    // setTimeout(() => {
    //     NotebookActions.replaceSelection(panel.content, "### Data Ingestion");
    // }, 6000);
    // setTimeout(() => {
    //     panel.content.activeCellIndex = 0;
    // }, 7000);
    // setTimeout(() => {
    //     NotebookActions.changeCellType(panel.content, "markdown");
    // }, 8000);
    // setTimeout(() => {
    //     panel.content.activeCellIndex = 0;
    // }, 9000);
    // setTimeout(() => {
    //     NotebookActions.run(panel.content);
    // }, 10000);
    // ########################
    // panel.content.activeCellIndex = 0;
    // console.log("Length of cells:", panel.content.model?.cells.length);
    // NotebookActions.insertAbove(panel.content);
    // NotebookActions.insertAbove(panel.content);
    // NotebookActions.insertAbove(panel.content);
    // NotebookActions.insertAbove(panel.content);
    // setTimeout(() => {
    //     panel.content.activeCellIndex = 4;
    //     NotebookActions.selectAbove(panel.content);
    //     NotebookActions.replaceSelection(panel.content, "### Data Ingestion");
    //     panel.content.activeCellIndex = 3;
    //     NotebookActions.selectAbove(panel.content);
    //     NotebookActions.replaceSelection(panel.content, "### Data Ingestion");
    //     panel.content.activeCellIndex = 2;
    //     NotebookActions.selectAbove(panel.content);
    //     NotebookActions.replaceSelection(panel.content, "### Data Ingestion");
    //     panel.content.activeCellIndex = 1;
    //     NotebookActions.selectAbove(panel.content);
    //     NotebookActions.replaceSelection(panel.content, "### Data Ingestion");

    // }, 1000);
    // ########################
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