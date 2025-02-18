import { JupyterFrontEnd, JupyterFrontEndPlugin } from '@jupyterlab/application';
import { INotebookTracker, NotebookPanel } from '@jupyterlab/notebook';
// import { IFileBrowserModel } from '@jupyterlab/filebrowser';
const extension: JupyterFrontEndPlugin<void> = {
  id: 'maxroe-extension',
  autoStart: true,
  requires: [INotebookTracker, IFileBrowserFactory],
  activate: async (app: JupyterFrontEnd,
    tracker: INotebookTracker,
    fileBrowserFactory: IFileBrowserFactory,
    palette: ICommandPalette
  ) => {
    console.log('JupyterLab extension cell-ui-extension is activated!');
};

export default extension;
