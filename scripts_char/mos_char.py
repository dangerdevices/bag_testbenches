# -*- coding: utf-8 -*-

from bag.core import BagProject

from bag.simulation.core import DesignManager

if __name__ == '__main__':

    config_file = 'specs_mos_char/pch_w0d5.yaml'

    local_dict = locals()
    if 'bprj' not in local_dict:
        print('creating BAG project')
        bprj = BagProject()

    else:
        print('loading BAG project')
        bprj = local_dict['bprj']

    sim = DesignManager(bprj, config_file)
    sim.characterize_designs(generate=True, measure=True, load_from_file=False)
