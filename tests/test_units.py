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
        assert unit.check_attack() is True


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

    def test_take_damage(self):
        solder = Solder()
        assert solder.get_experience == 0
        solder.set_health(100)
        solder.take_damage(10)
        assert solder.get_health == 90.05


class TestVehicles:

    def test_get_operators(self):
        vehicle = Vehicles()
        assert isinstance(vehicle.operators[0], Solder)
        assert 1 <= len(vehicle.operators) <= 3

    @patch('Battle.Units.random')
    def test_get_experience(self, mock_random):
        mock_random.randint = Mock(return_value=2)
        vehicle = Vehicles()
        assert len(vehicle.operators) == 2
        assert vehicle.get_experience == 0

    def test_alive(self):
        vehicle = Vehicles()
        units = vehicle.get_operators()
        assert vehicle.alive(units) is True

    @patch('Battle.Units.random')
    def test_do_attack(self, mock_random):
        mock_random.randint = Mock(return_value=1)
        vehicle = Vehicles()
        assert vehicle.do_attack == 0.505

    def test_take_damage(self):
        pass
