import pyganim

bolt_animation = pyganim.PygAnimation([('Resource/bolt_strike_0001.png', 0.1),
                                 ('Resource/bolt_strike_0002.png', 0.1),
                                 ('Resource/bolt_strike_0003.png', 0.1),
                                 ('Resource/bolt_strike_0004.png', 0.1),
                                 ('Resource/bolt_strike_0005.png', 0.1),
                                 ('Resource/bolt_strike_0006.png', 0.1),
                                 ('Resource/bolt_strike_0007.png', 0.1),
                                 ('Resource/bolt_strike_0008.png', 0.1),
                                 ('Resource/bolt_strike_0009.png', 0.1),
                                 ('Resource/bolt_strike_0010.png', 0.1)])

flame_animation = pyganim.PygAnimation([('Resource/flame_a_0001.png', 0.1),
                                 ('Resource/flame_a_0002.png', 0.1),
                                 ('Resource/flame_a_0003.png', 0.1),
                                 ('Resource/flame_a_0004.png', 0.1),
                                 ('Resource/flame_a_0005.png', 0.1),
                                 ('Resource/flame_a_0006.png', 0.1)])

smoke_animation = pyganim.PygAnimation([('Resource/smoke_puff_0001.png', 0.1),
                                 ('Resource/smoke_puff_0002.png', 0.1),
                                 ('Resource/smoke_puff_0003.png', 0.1),
                                 ('Resource/smoke_puff_0004.png', 0.1),
                                 ('Resource/smoke_puff_0005.png', 0.1),
                                 ('Resource/smoke_puff_0006.png', 0.1),
                                 ('Resource/smoke_puff_0007.png', 0.1),
                                 ('Resource/smoke_puff_0008.png', 0.1),
                                 ('Resource/smoke_puff_0009.png', 0.1),
                                 ('Resource/smoke_puff_0010.png', 0.1),])

def getBoltanim():
    return bolt_animation.getCopy()
    
def getFlameanim():
    return flame_animation.getCopy()
    
def getSmokeanim():
    return smoke_animation.getCopy()