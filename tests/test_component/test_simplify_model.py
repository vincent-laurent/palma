# Copyright 2023 Eurobios
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import matplotlib
import numpy as np
import pytest
import pandas as pd
from sklearn import metrics, model_selection

from palma.components import performance, FileSystemLogger, MLFlowLogger
from sklearn.ensemble import RandomForestClassifier
import tempfile
from palma import ModelEvaluation, Project
from palma import set_logger
from palma.components.simplify_model import SingleDecisionTree
from sklearn.datasets import make_classification


def test_simplify(classification_data):
    set_logger(FileSystemLogger(tempfile.gettempdir() + "/logger"))

    X, y = make_classification(random_state=0, n_samples=5000)
    X = pd.DataFrame(X)
    y = pd.Series(y)
    project = Project(problem="classification",
                      project_name=str(np.random.uniform()))

    project.start(
        X, y,
        splitter=model_selection.ShuffleSplit(n_splits=4, random_state=42))
    estimator = RandomForestClassifier()

    model = ModelEvaluation(estimator)
    model.add(SingleDecisionTree())
    model.fit(project)
    self = model
