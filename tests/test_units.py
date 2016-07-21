from Battle.Units import Solder, Unit, Vehicles
from mock import Mock, patch


class TestUnit:

    def test_get_variables(self):
        unit = Unit()
        assert unit.get_health is None
        assert unit.get_recharge is None
        assert unit.get_next_attack_time == 0
        assert unit.prev_time is None

    def test_set_variables(self):
        unit = Unit()
        unit.set_health(50)
        assert unit.get_health == 50
        unit.set_recharge(200.0)
        assert unit.get_recharge == 200.0
        unit.set_next_attack_time(0.5)
        assert unit.get_next_attack_time == 0.5

    def test_check_attack(self):
        unit = Unit()
        assert unit.check_attack() == True


class TestSolder:

    def test_set_experience(self):
        solder = Solder()
        solder.set_experience()
        assert solder.get_experience <= 50

    @patch('Battle.Units.random')
    def test_do_attack(self, mock_random):
        solder = Solder()
        solder.check_attack = Mock(return_value=True)
        mock_random.randint = Mock(return_value=1)
        assert solder.do_attack == 0.505
        solder.set_health(0)
        assert solder.do_attack == 0
