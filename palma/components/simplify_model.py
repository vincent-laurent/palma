from palma.components import Component
from palma import Project, ModelEvaluation
from sklearn.tree import DecisionTreeRegressor


class SingleDecisionTree(Component):

    def __init__(self, base_estimator=DecisionTreeRegressor()):
        self.__base_estimator = base_estimator

    def __call__(self, project: Project, model: ModelEvaluation):
        X_train = project.X.iloc[project.validation_strategy.train_index]

        predictions = model.avg_estimator_.predict_proba(X_train)[:, 1]

        tree = self.__base_estimator.fit(
            X_train,
            predictions
        )
        self.y1 = tree.predict(
            project.X.iloc[project.validation_strategy.test_index])
        self.y2 = model.avg_estimator_.predict_proba(
            project.X.iloc[project.validation_strategy.test_index])[:, 1]

    def plot_true_vs_pred(self):
        import matplotlib.pyplot as plt
        plt.scatter(self.y1, self.y2)
        plt.plot([0, 1], [0, 1])
