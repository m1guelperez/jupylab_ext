import {
  JupyterFrontEnd,
  JupyterFrontEndPlugin
} from '@jupyterlab/application';
import { ButtonExtension, } from './button';



/**
 * Initialization data for the notebook_labeling extension.
 */
const plugin: JupyterFrontEndPlugin<void> = {
  id: 'notebook_labeling/toolbar-button:plugin',
  description: 'A JupyterLab extension to label notebooks.',
  autoStart: true,
  activate: (app: JupyterFrontEnd) => {
    console.log('JupyterLab extension notebook_labeling is activated!');
    const your_button = new ButtonExtension();
    app.docRegistry.addWidgetExtension('Notebook', your_button);
  }
};

export default plugin;
