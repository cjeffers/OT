sample0 = [
                {   'input': 'ovea',
                    'output': 'o.ve.a',
                    'violation_vector': {1:0, 2:1, 3:1, 4:0},
                    'optimal': False,
                },

                {
                    'input': 'ovea',
                    'output': 'o.vee',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

        ]

no_rankings = [
                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0},
                    'optimal': False,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True
                }
           ]

apriori_entailments = [
                        {
                            'input': 'i1',
                            'output': 'o1',
                            'violation_vector': {1: 1, 2: 0, 3: 1},
                            'optimal': True
                        },

                        {
                            'input': 'i1',
                            'output': 'o2',
                            'violation_vector': {1: 0, 2: 1, 3: 0},
                            'optimal': False
                        },

                        {
                            'input': 'i2',
                            'output': 'o3',
                            'violation_vector': {1: 1, 2: 1, 3: 0},
                            'optimal': False
                        },

                        {
                            'input': 'i2',
                            'output': 'o4',
                            'violation_vector': {1: 0, 2: 0, 3: 1},
                            'optimal': True
                        }
]

hbounded = [
    {
        'input': 'i1',
        'output': 'o1',
        'violation_vector': {1: 0, 2: 0, 3: 0, 4: 0},
        'optimal': True,
    },
    {
        'input': 'i1',
        'output': 'o2',
        'violation_vector': {1: 1, 2: 1, 3: 1, 4: 1},
        'optimal': False,
    }
]

hbounded_optimal = [
    {
        'input': 'i1',
        'output': 'o1',
        'violation_vector': {1: 1, 2: 0},
        'optimal': True
    },
    {
        'input': 'i1',
        'output': 'o2',
        'violation_vector': {1: 1, 2: 1},
        'optimal': True
    }
]


three_const = [
                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:0, 3:0},
                    'optimal': True,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1},
                    'optimal': False,
                }
           ]

###########################################################################
##  Edge Case Testers  ####  Edge Case Testers  ####  Edge Case Testers  ##
###########################################################################

c0y_c1y_iy_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

c0y_c1y_in_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

c0y_c1n_iy_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1y_iy_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

c0y_c1n_in_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1y_in_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

c0y_c1y_iy_dn = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

c0y_c1n_iy_dn = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1y_iy_dn = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]


############################################################################
##  Error cases  ####  Error cases  ####  Error cases  ####  Error cases  ##
############################################################################

c0n_c1n_iy_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1n_in_dy = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i2',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1n_iy_dn = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

c0n_c1n_in_dn = [

                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': False,
                },

                {   'input': 'i1',
                    'output': 'o2',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

single_opt_cand =[
                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': True,
                }
]

single_non_opt_cand =[
                {   'input': 'i1',
                    'output': 'o1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1},
                    'optimal': False,
                }
]

############################################################################

voweldset = [
                {   'input': 'ovea',
                    'output': 'o-ve-a',
                    'violation_vector': {1:0, 2:1, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'ovea',
                    'output': 'o-vee',
                    'violation_vector': {1:0, 2:0, 3:0, 4:1},
                    'optimal': True,
                },

                {
                    'input': 'idea',
                    'output': 'i-de-a',
                    'violation_vector': {1:0, 2:1, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'idea',
                    'output': 'i-dee',
                    'violation_vector': {1:1, 2:0, 3:0, 4:1},
                    'optimal': False,
                },

                {
                    'input': 'lasi-a',
                    'output': 'la-si-a',
                    'violation_vector': {1:0, 2:0, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'lasi-a',
                    'output': 'la-sii',
                    'violation_vector': {1:0, 2:0, 3:0, 4:1},
                    'optimal': True,
                },

                {
                    'input': 'rasia',
                    'output': 'ra-si-a',
                    'violation_vector': {1:0, 2:0, 3:1, 4:0},
                    'optimal': True,
                },

                {
                    'input': 'rasia',
                    'output': 'ra-sii',
                    'violation_vector': {1:1, 2:0, 3:0, 4:1},
                    'optimal': False,
                },
        ]

cv_dset = {
    "constraints" : [ "ONSET", "*CODA", "MAX", "DEP" ],
    "candidates" : [
        { "input" : "CV", "output" : "CV",
         "optimal" : True, "violation_vector" : { 1:0, 2:0, 3:0, 4:0 } },
        { "input" : "CV", "output" : "CVC",
         "optimal" : False, "violation_vector" : { 1:0, 2:1, 3:0, 4:1 } },
        { "input" : "CV", "output" : "VC",
         "optimal" : False, "violation_vector" : { 1:1, 2:1, 3:1, 4:1 } },
        { "input" : "CV", "output" : "V",
         "optimal" : False, "violation_vector" : { 1:1, 2:0, 3:1, 4:0 } },
        { "input" : "CVC", "output" : "CV",
         "optimal" : True, "violation_vector" : { 1:0, 2:0, 3:1, 4:0 } },
        { "input" : "CVC", "output" : "CVC",
         "optimal" : False, "violation_vector" : { 1:0, 2:1, 3:0, 4:0 } },
        { "input" : "CVC", "output" : "VC",
         "optimal" : False, "violation_vector" : { 1:1, 2:1, 3:1, 4:0 } },
        { "input" : "CVC", "output" : "V",
         "optimal" : False, "violation_vector" : { 1:1, 2:0, 3:2, 4:0 } },
        { "input" : "VC", "output" : "CV",
         "optimal" : True, "violation_vector" : { 1:0, 2:0, 3:1, 4:1 } },
        { "input" : "VC", "output" : "CVC",
         "optimal" : False, "violation_vector" : { 1:0, 2:1, 3:0, 4:1 } },
        { "input" : "VC", "output" : "VC",
         "optimal" : False, "violation_vector" : { 1:1, 2:1, 3:0, 4:0 } },
        { "input" : "VC", "output" : "V",
         "optimal" : False, "violation_vector" : { 1:1, 2:0, 3:1, 4:0 } },
        { "input" : "V", "output" : "CV",
         "optimal" : True, "violation_vector" : { 1:0, 2:0, 3:0, 4:1 } },
        { "input" : "V", "output" : "CVC",
         "optimal" : False, "violation_vector" : { 1:0, 2:1, 3:0, 4:2 } },
        { "input" : "V", "output" : "VC",
         "optimal" : False, "violation_vector" : { 1:1, 2:1, 3:0, 4:1 } },
        { "input" : "V", "output" : "V",
         "optimal" : False, "violation_vector" : { 1:1, 2:0, 3:0, 4:0 } }
    ]
}

trivial_cot_6 = [
    {"input": "a", "output": "b", "optimal": True, "violation_vector": {1:0, 2:1, 3:1, 4:1, 5:1, 6:1 }},
    {"input": "a", "output": "c", "optimal": False, "violation_vector": {1:1, 2:0, 3:0, 4:0, 5:0, 6:0 }},
    {"input": "b", "output": "c", "optimal": True, "violation_vector": {1:0, 2:0, 3:1, 4:1, 5:1, 6:1 }},
    {"input": "b", "output": "e", "optimal": False, "violation_vector": {1:0, 2:1, 3:0, 4:0, 5:0, 6:0 }},
    {"input": "c", "output": "f", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:1, 6:1 }},
    {"input": "c", "output": "g", "optimal": False, "violation_vector": {1:0, 2:0, 3:1, 4:0, 5:0, 6:0 }},
    {"input": "d", "output": "f", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:1 }},
    {"input": "d", "output": "f", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:0, 6:0 }},
    {"input": "e", "output": "g", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:1 }},
    {"input": "e", "output": "g", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:0 }}
]

trivial_cot_7 = [
    {"input": "a", "output": "b", "optimal": True, "violation_vector": {1:0, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1 }},
    {"input": "a", "output": "c", "optimal": False, "violation_vector": {1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0 }},
    {"input": "b", "output": "c", "optimal": True, "violation_vector": {1:0, 2:0, 3:1, 4:1, 5:1, 6:1, 7:1}},
    {"input": "b", "output": "e", "optimal": False, "violation_vector": {1:0, 2:1, 3:0, 4:0, 5:0, 6:0, 7:0 }},
    {"input": "c", "output": "f", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:1}},
    {"input": "c", "output": "g", "optimal": False, "violation_vector": {1:0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0 }},
    {"input": "d", "output": "h", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1}},
    {"input": "d", "output": "i", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:0, 6:0, 7:0 }},
    {"input": "e", "output": "j", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1}},
    {"input": "e", "output": "k", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:0, 7:0 }},
    {"input": "f", "output": "l", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1}},
    {"input": "f", "output": "m", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:0 }}
]

trivial_cot_8 = [
    {"input": "a", "output": "b", "optimal": True, "violation_vector": {1:0, 2:1, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1 }},
    {"input": "a", "output": "c", "optimal": False, "violation_vector": {1:1, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }},
    {"input": "b", "output": "c", "optimal": True, "violation_vector": {1:0, 2:0, 3:1, 4:1, 5:1, 6:1, 7:1, 8:1 }},
    {"input": "b", "output": "e", "optimal": False, "violation_vector": {1:0, 2:1, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0 }},
    {"input": "c", "output": "f", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:1, 6:1, 7:1, 8:1 }},
    {"input": "c", "output": "g", "optimal": False, "violation_vector": {1:0, 2:0, 3:1, 4:0, 5:0, 6:0, 7:0, 8:0 }},
    {"input": "d", "output": "h", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:1, 7:1, 8:1 }},
    {"input": "d", "output": "i", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:1, 5:0, 6:0, 7:0, 8:0 }},
    {"input": "e", "output": "j", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:1, 8:1 }},
    {"input": "e", "output": "k", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:1, 6:0, 7:0, 8:0 }},
    {"input": "f", "output": "l", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:1 }},
    {"input": "f", "output": "m", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:1, 7:0, 8:0 }},
    {"input": "g", "output": "1", "optimal": True, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:1 }},
    {"input": "g", "output": "o", "optimal": False, "violation_vector": {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:1, 8:0 }}
]


# Finnish Case Dataset
casedset = [

                {
                    'input': 'act[trans]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD1',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:1, 3:2, 4:2, 5:3, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD3',
                    'violation_vector': {1:1, 2:1, 3:1, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD4',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD5',
                    'violation_vector': {1:1, 2:1, 3:1, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD6',
                    'violation_vector': {1:0, 2:1, 3:2, 4:2, 5:3, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[trans]',
                    'output': 'BAD7',
                    'violation_vector': {1:1, 2:1, 3:1, 4:2, 5:2, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[exist]',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1, 5:2, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD3',
                    'violation_vector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD4',
                    'violation_vector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD5',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[exist]',
                    'output': 'BAD6',
                    'violation_vector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'act[pred]',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:2, 3:2, 4:3, 5:3, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:1, 3:1, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD3',
                    'violation_vector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD4',
                    'violation_vector': {1:0, 2:1, 3:1, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD5',
                    'violation_vector': {1:0, 2:2, 3:2, 4:3, 5:3, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'act[pred]',
                    'output': 'BAD6',
                    'violation_vector': {1:0, 2:1, 3:1, 4:2, 5:2, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'NOM',
                    'violation_vector': {1:1, 2:1, 3:0, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[trans]',
                    'output': 'BAD2',
                    'violation_vector': {1:1, 2:1, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:1, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[exist]',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:1, 6:1},
                    'optimal': True,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:2, 3:0, 4:2, 5:2, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pass[pred]',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:1, 3:0, 4:1, 5:1, 6:2},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'GEN',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'trans',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:0, 3:1, 4:0, 5:0, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:0, 3:1, 4:1, 5:2, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'trans',
                    'output': 'BAD3',
                    'violation_vector': {1:0, 2:0, 3:0, 4:1, 5:1, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'exist',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                    'optimal': True,
                },

                {
                    'output': 'exist',
                    'input': 'BAD1',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:0},
                    'optimal': False,
                },

                {
                    'input': 'pred',
                    'output': 'NOM',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:0, 6:0},
                    'optimal': True,
                },

                {
                    'input': 'pred',
                    'output': 'BAD1',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:1, 6:1},
                    'optimal': False,
                },

                {
                    'input': 'pred',
                    'output': 'BAD2',
                    'violation_vector': {1:0, 2:0, 3:0, 4:0, 5:2, 6:2},
                    'optimal': False,
                },
        ]
