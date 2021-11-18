#include <iostream>
#include "world.h"

MyWorld::MyWorld() : _name("my world")
{
}

MyWorld::~MyWorld() = default;

std::string MyWorld::toString() const
{
	return _name;
}
