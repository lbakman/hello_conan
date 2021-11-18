/****************************************************************
*                                                               *
* Copyright (C) 2019 Saab Danmark A/S                           *
*                                                               *
* The copyright to the computer program(s) and/or documentation *
* herein is the property of Saab Danmark A/S. The program(s)    *
* and/or documentation may be used and/or copied only with the  *
* written permission of Saab Danmark A/S, or in accordance with *
* the terms and conditions stipulated in the agreement/contract *
* under which the program(s) and/or documentation have been     *
* supplied.                                                     *
*                                                               *
*****************************************************************
*                                                               *
* Information classifications: Not export controlled            *
*                              Company restricted               *
*                              Defence unclassified             *
*                                                               *
****************************************************************/
#include "world.h"
#include <gtest/gtest.h>

TEST(MyWorld, construct) {
	auto test = new MyWorld();
	EXPECT_NE(test, nullptr);
	delete test;
}

TEST(MyWorld, string_not_empty) {
	MyWorld test;
	EXPECT_FALSE(test.toString().empty());
}
