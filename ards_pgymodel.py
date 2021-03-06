#Using Jupyter live notebook

from IPython.display import Image
Image('images/ards_pgm.png')
#Node model imports

#Define 4 edges to make Bayesian Model

from pgmpy.models import BayesianModel

ards_pgmodel = BayesianModel([('Pneumonia', 'ARDS'),
                              ('Sepsis', 'ARDS'),
                              ('ARDS', 'Ventilator'),
                              ('ARDS', 'Pulmonary Scarring')])
                              
from pgmpy.factors.discrete import TabularCPD

cpd_pneumonia = TabularCPD(variable='Pneumonia', variable_card=5,
                      values=[[0.5], [0.2]])
cpd_sepsis = TabularCPD(variable='Sepsis', variable_card=5,
                       values=[[0.3], [0.7]])
cpd_ards = TabularCPD(variable='ARDS', variable_card=5,
                        values=[[0.9, 0.01, 0.005, 0.03],
                                [0.46, 0.41, 0.40, 0.45]],
                        evidence=['Pneumonia', 'Sepsis'],
                        evidence_card=[5, 5])
cpd_ventilator = TabularCPD(variable='Ventilator', variable_card=5,
                      values=[[0.6, 0.4], [0.3, 0.9]],
                      evidence=['ARDS'], evidence_card=[5])
cpd_pulmonaryscarring = TabularCPD(variable='Pulmonary Scarring', variable_card=5,
                      values=[[0.40, 0.1], [0.19, 0.11]],
                      evidence=['ARDS'], evidence_card=[5])
                      
 ards_pgmodel.add_cpds(cpd_pneumonia, cpd_sepsis, cpd_ards, cpd_ventilator, cpd_pulmonaryscarring)
 
print(ards_pgmodel.is_active_trail('Pneumonia', 'Sepsis'))
print(ards_pgmodel.is_active_trail('Pneumonia', 'Sepsis', observed=['ARDS']))

ards_pgmodel.active_trail_nodes('Pneumonia')
ards_pgmodel.local_independencies('Ventilator')
ards_pgmodel.get_independencies()
