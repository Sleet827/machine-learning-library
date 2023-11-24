Usage
=====

PyLearn provides different features from supervised and unsupervised learning. 

To use them, just import pylearn:

.. code-block:: python

   import pylearn as pl

|
The major features are:

|
Classification
~~~~~~~~~~~~~~

Documentation following soon.

|
|
Clustering
~~~~~~~~~~

You can choose between K-Means and K-Medoids as clustering algorithms.

The usage of both is quite similar:

.. code-block:: python

   kmeans = pl.KMeans()
   kmedoids = pl.KMedoids()

|
Now, train the algorithm by using the fit function, we will use kmeans to continue:

.. code-block:: python

   kmeans.fit(points)

|
This returns a list of the to the data points assigned clusters.
You could visualize the result with matplotlib.

|
If you want to customize the result, the following functions may help you:

.. code-block:: python

   kmeans.assigned_clusters(any_cluster)
   kmeans.rename(old, new)

|
|
Neural Network
~~~~~~~~~~~~~~

The neural network comes with different activation functions and loss functions.

First, you need to create a network, for example:

.. code-block:: python

   network = [
        pl.Dense_layer(input_length, output_length),
        pl.Tanh(),
        plpDense_layer(input_length, output_length),
        pl.Tanh()
    ]

|
Now, train the model:

.. code-block:: python

    train(x_train, y_train, network, loss, loss_derivative, epochs, log_error, log_duration)

|
Depending on your needs, training could take some time. To prevend training again each time, store the model:

.. code-block:: python

   save("network.pkl", network)

|
Let the model predict your input:

.. code-block:: python

   predict(x, network)

|
You can also evaluate the training:

.. code-block:: python
   
   evaluate(x_test, y_test)

