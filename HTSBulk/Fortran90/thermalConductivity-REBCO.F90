SUBROUTINE getTherCondREBCO(Model, n, arg, Conductivity)
  ! Frederic Trillaud <ftrillaudp@gmail.com> - October 11, 2020
  !elmerf90 -o thermalConductivity-REBCO.so thermalConductivity-REBCO.F90

  ! Elmer module
  USE DefUtils

  IMPLICIT NONE
  TYPE(Model_t) :: model
  INTEGER :: n
  REAL(KIND=dp) :: arg(*)
  REAL(KIND=dp) :: T, Top, k_ab, k_c
  REAL(KIND=dp), POINTER ::  Conductivity(:,:)
  LOGICAL :: gotIt, visu

  ! variables needed inside function
  TYPE(ValueList_t), POINTER :: material, const
  ! get pointer on list for material
  material => GetMaterial()
  IF (.NOT. ASSOCIATED(material)) THEN
    CALL Fatal('getTherCondREBCO', 'No material found')
  END IF

  Top = GetConstReal( material, 'Operating Temperature', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getTherCondREBCO', 'Operating Temperature')
  END IF

  visu = .FALSE.

  ! Get the variables from the input
  T = ABS(arg(1))

  ! Patch on the temperature
  IF (T < Top) THEN
    T = Top
  ELSE IF (T > 299.0) THEN
    T = 299.0
  END IF

  Conductivity = 0.0D00
  Conductivity(1,1) = getk_ab(T)
  Conductivity(2,2) = getk_ab(T)
  Conductivity(3,3) = getk_c(T)

  IF (visu) THEN
    PRINT 1, Conductivity(1,1),Conductivity(2,2),Conductivity(3,3)
    1  FORMAT(' k_11: ', EN12.3,' k_22: ', EN12.3,' k_33: ', EN12.3)
  END IF

  CONTAINS
    FUNCTION getk_ab(arg_T) RESULT(k_ab)
      IMPLICIT NONE
      REAL(KIND=dp) :: arg_T, k_ab
      REAL(KIND=dp) :: a0, a1, a2, a3, a4, a5

      a0 = (-1)*0.150152692773719
      a1 = 0.591108829048331
      a2 = 0.000540769939534348
      a3 = (-1)*0.000223922859241501
      a4 = 2.56756043483941e-06
      a5 = (-1)*8.517833095668e-09

      IF (arg_T < 100.0) THEN
        k_ab = a0+a1*arg_T+a2*arg_T**2+a3*arg_T**3+a4*arg_T**4+a5*arg_T**5
      ELSE
        k_ab = a0+a1*100+a2*100.0**2+a3*100.0**3+a4*100.0**4+a5*100.0**5
      END IF

      IF (visu) THEN
        2  FORMAT(' k_11: ', EN12.3)
        PRINT 2, k_ab
      END IF
    END FUNCTION getk_ab
    
    FUNCTION getk_c(arg_T) RESULT(k_c)
      IMPLICIT NONE
      REAL(KIND=dp) :: arg_T, k_c
      REAL(KIND=dp) :: a0, a1, a2, a3, a4, a5

      a0 = (-1)*2.06497213456219
      a1 = 0.407955438664907
      a2 = (-1)*0.00726450383620069
      a3 = 4.08165109438415e-05
      a4 = 7.2517312656179e-08
      a5 = (-1)*9.35406181819949e-10

      IF (arg_T < 100.0) THEN
        k_c = a0+a1*arg_T+a2*arg_T**2+a3*arg_T**3+a4*arg_T**4+a5*arg_T**5
      ELSE
        k_c = a0+a1*100+a2*100.0**2+a3*100.0**3+a4*100.0**4+a5*100.0**5
      END IF

      IF (visu) THEN
        2  FORMAT(' k_11: ', EN12.3)
        PRINT 2, k_c
      END IF
    END FUNCTION getk_c

END SUBROUTINE getTherCondREBCO
