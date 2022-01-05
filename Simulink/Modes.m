classdef Modes < Simulink.IntEnumType
  enumeration
    % The rate adaptive modes come after the non-rate adaptive and must
    % start with AOOR
    NO_PACE(0)
    AOO(1)
    AAI(2)
    AOOR(3)
    AAIR(4)
    VOO(5)
    VVI(6)
    VOOR(7)
    VVIR(8)
    DOOR(9)
    DOO(10)
  end
end

