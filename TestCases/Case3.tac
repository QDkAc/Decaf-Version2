VTABLE(_Main) {
    <empty>
    Main
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T0 = 4
    parm _T0
    _T1 =  call _Alloc
    _T2 = VTBL <_Main>
    *(_T1 + 0) = _T2
    return _T1
}

FUNCTION(main) {
memo ''
main:
    _T4 = 15000000
    _T5 = 0
    _T6 = (_T4 < _T5)
    if (_T6 == 0) branch _L10
    _T7 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T7
    call _PrintString
    call _Halt
_L10:
    _T8 = 4
    _T9 = (_T8 * _T4)
    _T10 = (_T8 + _T9)
    parm _T10
    _T11 =  call _Alloc
    *(_T11 + 0) = _T4
    _T3 = _T11
    _T12 = 1
    _T13 = 0
    _T14 = (_T12 < _T13)
    if (_T14 == 0) branch _L11
    _T15 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T15
    call _PrintString
    call _Halt
_L11:
    _T16 = 4
    _T17 = (_T16 * _T12)
    _T18 = (_T16 + _T17)
    parm _T18
    _T19 =  call _Alloc
    *(_T19 + 0) = _T12
    _T3 = _T19
    _T21 = 15000000
    _T22 = 0
    _T23 = (_T21 < _T22)
    if (_T23 == 0) branch _L12
    _T24 = "Decaf runtime error: Cannot create negative-sized array\n"
    parm _T24
    call _PrintString
    call _Halt
_L12:
    _T25 = 4
    _T26 = (_T25 * _T21)
    _T27 = (_T25 + _T26)
    parm _T27
    _T28 =  call _Alloc
    *(_T28 + 0) = _T21
    _T20 = _T28
}

