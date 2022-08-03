FUNCTION getDissipationREBCO(Model, n, arg) RESULT(S)
  ! Frederic Trillaud <ftrillaudp@gmail.com> - October 9, 2020
  !elmerf90 -o electricConductivity-REBCO.so electricConductivity-REBCO.F90

  ! Elmer module
  USE DefUtils

  IMPLICIT NONE
  TYPE(Model_t) :: model
  INTEGER :: n
  REAL(KIND=dp) :: arg(*)
  REAL(KIND=dp) :: S, Sn, Bx, By, Bz, B, Ex, Ey, Ez, E, mu0
  REAL(KIND=dp) :: T, Top, epsi, G, gamma_sc
  REAL(KIND=dp) :: Tc, Jc0, Jc, nValue0, nValue, Ec
  LOGICAL :: gotIt

  ! variables needed inside function
  TYPE(ValueList_t), POINTER :: material, const
  ! get pointer on list for material
  material => GetMaterial()
  IF (.NOT. ASSOCIATED(material)) THEN
    CALL Fatal('getElecCond', 'No material found')
  END IF
  ! read in critical electrical field
  Ec = GetConstReal( material, 'Critical Electrical Field', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getElecCond', 'Critical Electrical Field')
  END IF
  ! read in reference Critical Temperature
  Tc = GetConstReal( material, 'Critical Temperature', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getElecCond', 'Critical Temperature')
  END IF
  ! read in n value
  Jc0 = GetConstReal( material, 'Critical Current Density', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getElecCond', 'Critical Current Density')
  END IF
  ! read in n value
  nValue0 = GetConstReal( material, 'N-Value', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getElecCond', 'N-Value')
  END IF
  ! read in operating temperature
  Top = GetConstReal( material, 'Operating Temperature', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getElecCond', 'Operating Temperature')
  END IF
  ! read in mass density
  gamma_sc = GetConstReal( material, 'Density', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getDissipation', 'Density')
  END IF

  ! Get the variables from the input
  T = arg(1)
  Bx = arg(2)
  By = arg(3)
  Bz = arg(4)
  Ex = arg(5)
  Ey = arg(6)
  Ez = arg(7)

  B = SQRT(Bx**2+By**2+Bz**2)
  E = SQRT(Ex**2+Ey**2+Ez**2)

  IF (E == 0.0) THEN
    epsi = 1.0e-6*Ec
  ELSE
    epsi = 0.0
  END IF
  
  nValue = getNValue(T,B)
  Jc = getJc(T,B)
  Sn = 3.0

  IF (T < Tc) THEN
    S = (Jc/(E+epsi))*(E/Ec)**(1.0/nValue)+Sn
  ELSE
    S = Sn
  END IF

  G = (S*E**2)/gamma_sc

  !PRINT 1, S
  !1  FORMAT(' S: ', EN12.3)

  CONTAINS
    FUNCTION getJc(arg_T,arg_B) RESULT(JJc)
      IMPLICIT NONE
      REAL(KIND=dp) :: arg_T, arg_B, JJc
      REAL(KIND=dp) :: tt, ttop, B0
    
      B0 = 2.1
      tt = arg_T/Tc
      ttop = Top/Tc

      IF (arg_T < Tc) THEN
        JJc = ((1-tt)/(1-ttop))*exp(-B/B0)*Jc0
      ELSE
        JJc = 0.0
      END IF
    END FUNCTION getJc

    FUNCTION getNValue(arg_T,arg_B) RESULT(nValue)
      IMPLICIT NONE
      REAL(KIND=dp) :: arg_T, arg_B, nValue
      nValue = nValue0
    END FUNCTION getNValue

END FUNCTION getDissipationREBCO
