:py:mod:`palma.base.engine`
===========================

.. py:module:: palma.base.engine


Module Contents
---------------

Classes
~~~~~~~

.. autoapisummary::

   palma.base.engine.BaseOptimizer
   palma.base.engine.FlamlOptimizer




.. py:class:: BaseOptimizer(engine_parameters: dict)


   .. py:property:: best_model_
      :type: None
      :abstractmethod:


   .. py:property:: transformer_
      :type: None
      :abstractmethod:


   .. py:property:: engine_parameters
      :type: Dict


   .. py:property:: allow_splitter


   .. py:property:: run_id
      :type: str


   .. py:method:: __optimize(X: pandas.DataFrame, y: pandas.Series, splitter: palma.base.splitting_strategy.ValidationStrategy = None) -> None
      :abstractmethod:


   .. py:method:: allowing_splitter(splitter)


   .. py:method:: start(project: Project)



.. py:class:: FlamlOptimizer(engine_parameters: dict)


   Bases: :py:obj:`BaseOptimizer`

   .. py:property:: best_model_
      :type: sklearn.base.BaseEstimator


   .. py:property:: transformer_


   .. py:property:: allow_splitter


   .. py:method:: __optimize(X: pandas.DataFrame, y: pandas.DataFrame, splitter: palma.base.splitting_strategy.ValidationStrategy = None) -> None



