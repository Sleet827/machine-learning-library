class Layer:
    """
    An abstract base class for neural network layers.
    Defines the basic properties and methods that can be used by all derived layers.

    Methods:
    forward_pass(input)
    backpropagation(output_gradient, learning_rate)
    """
    def __init__(self) -> None:
        pass

    def forward_pass(self, input) -> None:
        pass

    def backpropagation(self, output_gradient, learning_rate) -> None:
        pass