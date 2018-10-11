import maya.cmds as mc

def attr():
    name = mc.ls(sl=True)
    mode = mc.radioCollection(rC, q=True, select=True)
    off = mc.checkBox(of, q=True, v=True)

    if mode == 'pa':
        mc.parentConstraint('{}'.format(name[0]),'{}'.format(name[1]), mo=off)

    elif mode == 'po':
        mc.pointConstraint('{}'.format(name[0]),'{}'.format(name[1]), mo=off)

    elif mode == 'oc':
        mc.orientConstraint('{}'.format(name[0]),'{}'.format(name[1]), mo=off)

    elif mode == 'sc':
        mc.scaleConstraint('{}'.format(name[0]),'{}'.format(name[1]), mo=off)

    elif mode == 'ac':
        mc.aimConstraint('{}'.format(name[0]),'{}'.format(name[1]), mo=off)

win = mc.window(t='ConstraintSet', widthHeight=(400,90))

form = mc.formLayout()

rC = mc.radioCollection()
pa = mc.radioButton('pa', l='Parent', h=10, select=True)
po = mc.radioButton('po', l='Point', h=10)
oc = mc.radioButton('oc', l='Orient', h=10)
sc = mc.radioButton('sc', l='Scale', h=10)
ac = mc.radioButton('ac', l='Aim', h=10)

of = mc.checkBox(l='Maintain offset')
bt = mc.button(l='Constraint', w=400, h=30, c='attr()')

mc.formLayout(form, edit=True, attachForm=[
    (pa, 'top', 10),(pa, 'left', 20),
    (po, 'top', 10),(po, 'left', 100),
    (oc, 'top', 10),(oc, 'left', 180),
    (sc, 'top', 10),(sc, 'left', 260),
    (ac, 'top', 10),(ac, 'left', 340)
])
mc.formLayout(form, edit=True, attachForm=[
    (of, 'top',30),(of,'left', 150)
])
mc.formLayout(form, edit=True, attachForm=[
    (bt, 'bottom', 5)
])

mc.showWindow(win)
