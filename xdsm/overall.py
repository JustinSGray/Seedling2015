from XDSM import XDSM

opt = 'Optimization'
anl = 'Analysis'
dat = 'DataInter'

x = XDSM()
x.addComp('opt', opt, 'Optimizer')
#x.addComp('sol', 'MDA', 'Solver')
x.addComp('prop', anl, 'Propeller')
x.addComp('aero', anl, 'Aerodynamics')
x.addComp('struct', anl, 'Structures')


x.addDep('prop', 'opt', dat, '$D_{prop}$', False)
x.addDep('aero', 'opt', dat, '\TwolineComponent{2.55cm}{$s, c_{wing},$}{$twist_{wing}, D_{Prop}$}', False)
x.addDep('struct', 'opt', dat, '$Thk$', False)
x.addDep('prop', 'opt', dat, '\TwolineComponent{2.55cm}{$RPM, D_{Prop},$}{$twist_{prop}, c_{prop}$}', False)


x.addDep('struct', 'aero', dat, '$Loads$', False)
x.addDep('aero', 'struct', dat, '$Disp.$', False)
x.addDep('aero', 'prop', dat, '$a_{induced}$', False)
x.addDep('prop', 'aero', dat, '$Drag$', False)

x.addDep('opt', 'prop', dat, '$Pwr$', False)



x.write('overall',True)
