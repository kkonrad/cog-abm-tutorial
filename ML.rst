Machine Learning in COG-ABM
===========================

All functionality is stored in **cog_abm.ML** package.

Currently we don't support samples with missing values.

Interesting modules:

- core
- statistics
- diversity


core
----

See https://github.com/CogSys/cog-abm/blob/master/src/cog_abm/ML/core.py for:

- Classifier API (classify methods, train methods)
- Sample (values and meta data)
- distances
- load_samples_arff
- split_data, split_data_cv (cross-validation)


Soon there will be also more on distances and numeric attribute normalization.


statistics
----------
Calculating classifier performance statistics.
See https://github.com/CogSys/cog-abm/blob/master/src/cog_abm/ML/statistics.py for more details.

The only metrics that work for multiclass problem are:

- correct
- AUCROC

Useful functions there provided:

- avg_classifier_performance
- aucroc_avg_classifier_performance


diversity
---------
Provides tools for skipping some attributes or samples when training.


Examples
--------

Loading data and checking classifiers quality.

::

    import pprint
    from cog_abm.ML.core import load_samples_arff, split_data, Sample, split_data_cv
    from cog_abm.ML.orange_wrapper import OrangeClassifier
    from cog_abm.ML.statistics import aucroc_avg_classifier_performance

    samples = load_samples_arff('glass.arff')
    cv_data = split_data_cv(samples, 8)

    classifiers = [
        OrangeClassifier('kNNLearner', k=3),
        OrangeClassifier('BayesLearner'),
        OrangeClassifier('TreeLearner')
    ]

    for cl in classifiers:
        avg, std = aucroc_avg_classifier_performance(cl, cv_data)
        print "%s: AUCROC: %f  stdev: %f" % (str(cl), avg, std)

    known_sample = samples[0]
    unknown_sample = Sample([v + (-1) ** i for i, v in enumerate(known_sample.get_values())])

    print
    print "Known sample:", str(known_sample)
    print "Unknown sample:", str(unknown_sample)

    for cl in classifiers:
        print
        print cl
        cl_distr = cl.class_probabilities(known_sample)
        print "for known_sample:"
        pprint.pprint(cl_distr)
        cl_distr = cl.class_probabilities(unknown_sample)
        print "for unknown_sample:"
        pprint.pprint(cl_distr)


Extending with new libraries
----------------------------

We can add support for new algorithms from different libraries.
Example of how to do this can be seen in module **cog_abm.ML.orange_wrapper**.

This is good project for students.

Note
----

In your projects you don't have to create this abstraction.
You can directly use any library that you want.

