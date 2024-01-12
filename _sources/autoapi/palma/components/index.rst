:py:mod:`palma.components`
==========================

.. py:module:: palma.components


Submodules
----------
.. toctree::
   :titlesonly:
   :maxdepth: 1

   base/index.rst
   checker/index.rst
   dashboard/index.rst
   data_checker/index.rst
   data_profiler/index.rst
   logger/index.rst
   performance/index.rst


Package Contents
----------------

Classes
~~~~~~~

.. autoapisummary::

   palma.components.Component
   palma.components.FileSystemLogger
   palma.components.MLFlowLogger
   palma.components.ProfilerYData
   palma.components.ExplainerDashboard
   palma.components.RegressionAnalysis
   palma.components.ScoringAnalysis
   palma.components.ShapAnalysis
   palma.components.DeepCheck




.. py:class:: Component


   Bases: :py:obj:`object`

   .. py:method:: __str__()

      
      Return str(self).
















      ..
          !! processed by numpydoc !!


.. py:class:: FileSystemLogger(uri: str = tempfile.gettempdir(), **kwargs)


   Bases: :py:obj:`Logger`

   



   :Parameters:

       **uri** : str
           root path or directory, from which will be saved artifacts and metadata 














   ..
       !! processed by numpydoc !!
   .. py:method:: log_project(project: palma.base.project.Project) -> None

      
      log_project performs the first level of backup as described
      in the object description. 

      This method creates the needed folders and saves an instance of         :class:`~palma.Project`.

      :Parameters:

          **project: :class:`~palma.Project`**
              an instance of Project














      ..
          !! processed by numpydoc !!

   .. py:method:: log_metrics(metrics: dict, path: str) -> None


   .. py:method:: log_artifact(obj, path: str) -> None


   .. py:method:: log_params(parameters: dict, path: str) -> None


   .. py:method:: create_directories()



.. py:class:: MLFlowLogger(uri: str)


   Bases: :py:obj:`Logger`

   
   MLFlowLogger class for logging experiments using MLflow.


   :Parameters:

       **uri** : str
           The URI for the MLflow tracking server.





   :Raises:

       ImportError: If mlflow is not installed.
           ..







   :Attributes:

       **tmp_logger** : (FileSystemLogger)
           Temporary logger for local logging before MLflow logging.

   .. rubric:: Methods



   ========================================================  ==========
               **log_project(project: 'Project') -> None:**  Logs the project information to MLflow, including project name and parameters.  
   **log_metrics(metrics: dict[str, typing.Any]) -> None:**  Logs metrics to MLflow.  
            **log_artifact(artifact: dict, path) -> None:**  Logs artifacts to MLflow using the temporary logger.  
                      **log_params(params: dict) -> None:**  Logs parameters to MLflow.  
                        **log_model(model, path) -> None:**  Logs the model to MLflow using the temporary logger.  
   ========================================================  ==========

   ..
       !! processed by numpydoc !!
   .. py:method:: log_project(project: palma.base.project.Project) -> None


   .. py:method:: log_metrics(metrics: dict[str, Any], path=None) -> None


   .. py:method:: log_artifact(artifact: dict, path) -> None


   .. py:method:: log_params(params: dict) -> None


   .. py:method:: log_model(model, path)



.. py:class:: ProfilerYData(**config)


   Bases: :py:obj:`palma.components.base.ProjectComponent`

   
   Base Project Component class

   This object ensures that all subclasses Project component implements a















   ..
       !! processed by numpydoc !!
   .. py:method:: __call__(project: Project)



.. py:class:: ExplainerDashboard(dashboard_config: Union[str, Dict] = default_config_path, n_sample: int = None)


   Bases: :py:obj:`palma.components.base.Component`

   .. py:method:: __call__(project: Project, model: Model) -> explainerdashboard.ExplainerDashboard

      
      This function returns dashboard instance. This dashboard is to be run
      using its `run` method.


      :Parameters:

          **project: Project**
              Instance of project used to compute explainer.

          **model: Run**
              Current run to use in explainer.











      .. rubric:: Examples

      >>> db = ExpDash(dashboard_config="path_to_my_config")
      >>> explainer_dashboard = db(project, model)
      >>> explainer_dashboard.run(
      >>>    port="8050", host="0.0.0.0", use_waitress=False)



      ..
          !! processed by numpydoc !!

   .. py:method:: update_config(dict_value: Dict[str, Dict])

      
      Update specific parameters from the actual configuration.


      :Parameters:

          **dict_value: dict**
              explainer_parameters: dict
                  Parameters to be used in see `explainerdashboard.RegressionExplainer`
                  or `explainerdashboard.ClassifierExplainer`.
              dashboard_parameters: dict
                  Parameters use to compose dashboard tab, items or themes
                  for `explainerdashboard.ExplainerDashboard`.
                  Tabs and component of the dashboard can be hidden, see
                  `customize dashboard section <https://explainerdashboard.readthedocs.io/en/latest/custom.html>`_
                  for more detail.














      ..
          !! processed by numpydoc !!

   .. py:method:: _prepare_dataset() -> None

      
      This function performs the following processing steps :
          - Ensure that column name is str (bug encountered in dashboard)
          - Get code from categories just in case of category data types
          - Sample the data if specified by user
















      ..
          !! processed by numpydoc !!

   .. py:method:: _get_explainer(project: Project, model: Model) -> explainerdashboard.explainers.BaseExplainer


   .. py:method:: _get_dashboard(explainer: explainerdashboard.explainers.BaseExplainer) -> ExplainerDashboard



.. py:class:: RegressionAnalysis(on)


   Bases: :py:obj:`Analyser`

   
   Base Model Component class
















   ..
       !! processed by numpydoc !!
   .. py:method:: compute_predictions_errors(fun=None)


   .. py:method:: plot_prediction_versus_real(colormap=plot.get_cmap('rainbow'))


   .. py:method:: plot_errors_pairgrid(fun=None, number_percentiles=4, palette='rocket_r', features=None)



.. py:class:: ScoringAnalysis(on)


   Bases: :py:obj:`Analyser`

   
   Base Model Component class
















   ..
       !! processed by numpydoc !!
   .. py:property:: threshold


   .. py:attribute:: mean_fpr

      

   .. py:method:: confusion_matrix(in_percentage=False)


   .. py:method:: __interpolate_roc(_)


   .. py:method:: plot_roc_curve(plot_method='mean', plot_train: bool = False, c=colors[0], cmap: str = 'inferno', cv_iter=None, label: str = '', mode: str = 'std', label_iter: iter = None, plot_base: bool = True, **kwargs)

      
      Plot the ROC curve.


      :Parameters:

          **plot_method** : str,
              Select the type of plot for ROC curve
              
              - "beam" (default) to plot all the curves using shades
              - "all" to plot each ROC curve
              - "mean" plot the mean ROC curve

          **plot_train: bool**
              If True the train ROC curves will be plot, default False.

          **c: str**
              Not used only with plot_method="all". Set the color of ROC curve

          **cmap: str**
              ..

          **cv_iter**
              ..

          **label**
              ..

          **mode**
              ..

          **label_iter**
              ..

          **plot_base: bool,**
              Plot basic ROC curve helper

          **kwargs:**
              Deprecated

      :Returns:

          
              ..













      ..
          !! processed by numpydoc !!

   .. py:method:: compute_threshold(method: str = 'total_population', value: float = 0.5, metric: Callable = None)

      
      Compute threshold using various heuristics
















      ..
          !! processed by numpydoc !!

   .. py:method:: plot_threshold(**plot_kwargs)



.. py:class:: ShapAnalysis(on, n_shap, compute_interaction=False)


   Bases: :py:obj:`Analyser`

   
   Base Model Component class
















   ..
       !! processed by numpydoc !!
   .. py:method:: __call__(project: Project, model: ModelEvaluation)


   .. py:method:: __select_explainer()


   .. py:method:: _compute_shap_values(n, is_regression, explainer_method=shap.TreeExplainer, compute_interaction=False)


   .. py:method:: __change_features_name_to_string()


   .. py:method:: plot_shap_summary_plot()


   .. py:method:: plot_shap_decision_plot(**kwargs)


   .. py:method:: plot_shap_interaction(feature_x, feature_y)



.. py:class:: DeepCheck(name: str = 'Data Checker', dataset_parameters: dict = None, dataset_checks: Union[List[deepchecks.core.BaseCheck], deepchecks.core.BaseSuite] = data_integrity(), train_test_datasets_checks: Union[List[deepchecks.core.BaseCheck], deepchecks.core.BaseSuite] = Suite('Checks train test', train_test_validation()))


   Bases: :py:obj:`palma.components.base.ProjectComponent`

   
   This object is a wrapper of the Deepchecks library and allows to audit the
   data through various checks such as data drift, duplicate values, ...


   :Parameters:

       **dataset_parameters** : dict, optional
           Parameters and their values that will be used to generate
           :class:`deepchecks.Dataset` instances (required to run the checks on)

       **dataset_checks: Union[List[BaseCheck], BaseSuite], optional**
           List of checks or suite of checks that will be run on the whole dataset
           By default: use the default suite single_dataset_integrity to detect
           the integrity issues

       **train_test_datasets_checks: Union[List[BaseCheck], BaseSuite], optional**
           List of checks or suite of checks to detect issues related to the
           train-test split, such as feature drift, detecting data leakage...
           By default: use the default suites train_test_validation and
           train_test_leakage














   ..
       !! processed by numpydoc !!
   .. py:method:: __call__(project: palma.base.project.Project) -> None

      
      Run suite of checks on the project data.


      :Parameters:

          **project: project**
              ..














      ..
          !! processed by numpydoc !!

   .. py:method:: __generate_datasets(project: palma.base.project.Project, **kwargs) -> None

      
      Generate :class:`deepchecks.Dataset`


      :Parameters:

          **project: project**
              :class:`~palma.Project`














      ..
          !! processed by numpydoc !!

   .. py:method:: __generate_suite(checks: Union[List[deepchecks.core.BaseCheck], deepchecks.core.BaseSuite], name: str) -> deepchecks.tabular.Suite

      
      Generate a Suite of checks from a list of checks or a suite of checks


      :Parameters:

          **checks: Union[List[BaseCheck], BaseSuite], optional**
              List of checks or suite of checks

          **name: str**
              Name for the suite to returned

      :Returns:

          suite: :class:`deepchecks.Suite`
              instance of :class:`deepchecks.Suite`













      ..
          !! processed by numpydoc !!

   .. py:method:: __str__() -> str

      
      Return str(self).
















      ..
          !! processed by numpydoc !!


