import nengo
from nengo import spa

D = 32

vocab = spa.Vocabulary(D)

vocab.add("CALI", vocab.parse("0.1*WHITE + 0.9*HISPANIC"))
vocab.add("KANSAS", vocab.parse("0.7*WHITE + 0.3*HISPANIC"))

with spa.SPA(vocabs=[vocab]) as model:

    model.us_state = spa.State(D)
    model.ethnicity = spa.State(D)

    # use this compare output to find out which ethnicity is 
    # more strongly associated with which state
    model.compare = spa.Compare(D)

    # you could also do this with spa.Actions
    nengo.Connection(model.us_state.output, model.compare.inputA)
    nengo.Connection(model.ethnicity.output, model.compare.inputB)