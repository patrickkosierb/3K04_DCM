classdef Modes < Simulink.IntEnumType
  enumeration
    % The rate adaptive modes come after the non-rate adaptive and must
    % start with AOOR
    NO_PACE(0)
    AOO(1)
    VOO(2)
    AAI(3)
    VVI(4)
    DOO(5)
    AOOR(6)
    VOOR(7)
    AAIR(8)
    VVIR(9)
    DOOR(10)
  end
end

