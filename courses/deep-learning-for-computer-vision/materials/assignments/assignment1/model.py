import torch
from torch.nn.functional import one_hot

__all__ = [
  'softmax',
  'cross_entropy',
  'softmax_classifier',
  'softmax_classifier_backward'
]


##########################################################
# Softmax
##########################################################

def softmax(x):
  """Softmax activation.

  Args:
    x (torch.Tensor): The input tensor, has shape `(batch_size, num_classes)`.

  Returns:
    y (torch.Tensor): The softmax distribution over `x`. Has the same shape as `x`.
      Each row in `y` is a probability over the classes.
  """
  # BEGIN SOLUTION
  raise NotImplementedError
  # END SOLUTION


##########################################################
# Cross Entropy
##########################################################

def cross_entropy(pred, target):
  """Cross-entropy loss for hard-labels.

  Hint: You can use the imported `one_hot` function.

  Args:
    pred (torch.Tensor): The predictions (probability per class), has shape `(batch_size, num_classes)`.
    target (torch.Tensor): The target classes (integers), has shape `(batch_size,)`.

  Returns:
    loss (torch.Tensor): The mean cross-entropy loss over the batch.
  """
  # BEGIN SOLUTION
  raise NotImplementedError
  # END SOLUTION


##########################################################
# Softmax Classifier
##########################################################

def softmax_classifier(x, w, b):
  """Applies the prediction of the Softmax Classifier.

  Args:
    x (torch.Tensor): The input tensor, has shape `(batch_size, in_dim)`.
    w (torch.Tensor): The weight tensor, has shape `(num_classes, in_dim)`.
    b (torch.Tensor): The bias tensor, has shape `(num_classes,)`.

  Returns:
    pred (torch.Tensor): The predictions, has shape `(batch_size, num_classes)`.
      Each row is a probablity measure over the classes.
  """
  # BEGIN SOLUTION
  raise NotImplementedError
  # END SOLUTION


##########################################################
# Softmax Classifier Backward
##########################################################

def softmax_classifier_backward(x, w, b, pred, target):
  """Computes the gradients of weight in the Softmax Classifier.

  The gradients computed for the parameters `w` and `b` should be stored in
  `w.grad` and `b.grad`, respectively.

  Hint: You can use the imported `one_hot` function.

  Args:
    x (torch.Tensor): The input tensor, has shape `(batch_size, in_dim)`.
    w (torch.Tensor): The weight tensor, has shape `(num_classes, in_dim)`.
    b (torch.Tensor): The bias tensor, has shape `(num_classes,)`.
    pred (torch.Tensor): The predictions (probability per class), has shape `(batch_size, num_classes)`.
    target (torch.Tensor): The target classes (integers), has shape `(batch_size,)`.
  """
  # BEGIN SOLUTION
  raise NotImplementedError
  # END SOLUTION
