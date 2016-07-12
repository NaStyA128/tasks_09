import BattleField


def func(armies_number_, strategy_, squads_number_):
    print('Input units (soldiers and vehicles) 5 to 10: ')
    soldiers = int(input('soldiers = '))
    vehicles = int(input('vehicles = '))
    if 5 <= soldiers + vehicles <= 10:
        battle = BattleField.BattleField(armies_number=armies_number_,
                                         strategy=strategy_,
                                         squads_number=squads_number_,
                                         soldiers_number=soldiers,
                                         vehicles_number=vehicles)
        print('\033[1m' + "Win army: " + str(battle.start()))
    else:
        print('Incorrect number of units.')
        func(armies_number_, strategy_, squads_number_)


if __name__ == "__main__":
    armies_number = int(input('armies_number = '))
    strategy = input('strategy = ')
    squads_number = int(input('squads_number = '))
    func(armies_number, strategy, squads_number)
