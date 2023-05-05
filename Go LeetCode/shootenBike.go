package main

type shotenBike struct {
	On    bool
	Ammo  int
	Power int
}

func (s *shotenBike) Shoot() bool {
	if s.On && s.Ammo > 0 {
		s.Ammo--
		return true
	}
	return false
}

func (s *shotenBike) RideBike() bool {
	if s.On && s.Power > 0 {
		s.Power--
		return true
	}
	return false
}
