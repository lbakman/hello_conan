#pragma once

#include <string>

class MyWorld final {
public:
	MyWorld();
	~MyWorld();

	std::string toString() const;

private:
	std::string _name;
};
