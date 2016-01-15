VTABLE(_Main) {
    <empty>
    Main
}

VTABLE(_A) {
    <empty>
    A
    _A.init;
}

VTABLE(_B) {
    <empty>
    B
    _B.init;
}

FUNCTION(_Main_New) {
memo ''
_Main_New:
    _T4 = 4
    parm _T4
    _T5 =  call _Alloc
    _T6 = VTBL <_Main>
    *(_T5 + 0) = _T6
    return _T5
}

FUNCTION(_A_New) {
memo ''
_A_New:
    _T7 = 8
    parm _T7
    _T8 =  call _Alloc
    _T9 = VTBL <_A>
    *(_T8 + 0) = _T9
    return _T8
}

FUNCTION(_B_New) {
memo ''
_B_New:
    _T10 = 8
    parm _T10
    _T11 =  call _Alloc
    _T12 = VTBL <_B>
    *(_T11 + 0) = _T12
    return _T11
}

FUNCTION(main) {
memo ''
main:
_L14:
    _T13 = 1
    if (_T13 == 0) branch _L15
    _T16 =  call _A_New
    _T14 = _T16
    _T17 =  call _B_New
    _T15 = _T17
    parm _T14
    parm _T15
    _T18 = *(_T14 + 0)
    _T19 = *(_T18 + 8)
    call _T19
    parm _T15
    parm _T14
    _T20 = *(_T15 + 0)
    _T21 = *(_T20 + 8)
    call _T21
    branch _L14
_L15:
}

FUNCTION(_A.init) {
memo '_T0:4 _T1:8'
_A.init:
    _T22 = *(_T0 + 4)
    *(_T0 + 4) = _T1
}

FUNCTION(_B.init) {
memo '_T2:4 _T3:8'
_B.init:
    _T23 = *(_T2 + 4)
    *(_T2 + 4) = _T3
}

