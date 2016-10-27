import nengo

# create a configuration for a threshold of 0.3
thresh_config = nengo.presets.ThresholdingEnsembles(0.3)

with nengo.Network() as model:
    # make a cycling ramp input to show the threshold is working
    in_node = nengo.Node(lambda t: 2*(t % 1) - 1)

    # make an ensemble with the thresholding configuration
    with thresh_config:
        thresh_ens = nengo.Ensemble(100, 1)

    nengo.Connection(in_node, thresh_ens)
