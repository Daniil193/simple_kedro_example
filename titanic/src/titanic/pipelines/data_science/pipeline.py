from kedro.pipeline import Pipeline, node
from .nodes import split_data, train_model, evaluate_model

def create_pipeline(**kwargs):
    return Pipeline([
                      node(
                            func=split_data,
                            inputs=["preprocessed_input_data", "parameters"],
                            outputs=["X_train", "X_test", "y_train", "y_test"],
                            name="split_data_node"
                           ),
                      node(
                            func=train_model,
                            inputs=["X_train", "y_train", "parameters"],
                            outputs="classificator",
                            name="train_model_node",
                          ),
                      node(
                            func=evaluate_model,
                            inputs=["classificator", "X_test", "y_test", "parameters"],
                            outputs=None,
                            name="evaluate_model_node"
                           )
                    ])