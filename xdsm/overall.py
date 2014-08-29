from XDSM import XDSM

opt = 'Optimization'
anl = 'Analysis'
dat = 'DataInter'

x = XDSM()
x.addComp('opt', opt, 'Optimizer')
#x.addComp('sol', 'MDA', 'Solver')
x.addComp('geom', anl, 'Geometry')
x.addComp('prop', anl, 'Propeller')
x.addComp('aero', anl, 'Aerodynamics')
x.addComp('struct', anl, 'Structures')
x.addComp('dyn', anl, 'Dynamics')

x.addDep('opt', 'prop', dat, '$Pwr$', False)
x.addDep('opt', 'dyn', dat, '$Disp_{dynamic}$', False)
x.addDep('opt', 'struct', dat, '$stress$', False)



x.addDep('geom', 'opt', dat, '\ThreelineComponent{2.55cm}{$s, c_{prop},$}{$twist_{prop}, D_{Prop}$}{$c_{wing},twist_{wing}$}', False)
x.addDep('prop', 'geom', dat, '$mesh_{prop}$', False)
x.addDep('aero', 'geom', dat, '$mesh_{wing}$', False)
x.addDep('struct', 'geom', dat, '$mesh_{wing}$', False)

x.addDep('prop', 'opt', dat, '$D_{prop}$', False)
x.addDep('aero', 'opt', dat, '\TwolineComponent{2.55cm}{$s, c_{wing},$}{$twist_{wing}, D_{Prop}$}', False)
x.addDep('struct', 'opt', dat, '$Thk$', False)
x.addDep('prop', 'opt', dat, 'RPM', False)

x.addDep('struct', 'aero', dat, '$Loads$', False)
x.addDep('aero', 'struct', dat, '$Disp_{static}$', False)
x.addDep('aero', 'prop', dat, '$a_{induced}$', False)
x.addDep('prop', 'aero', dat, '$Drag$', False)

x.addDep('dyn', 'aero', dat, '$Loads$', False)

x.addDep('dyn', 'struct', dat, '$Disp_{static}$', False)



x.write('overall',True)
