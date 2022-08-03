SUBROUTINE getRegularizationSolverQ(Model, Solver)
  ! Frederic Trillaud <ftrillaudp@gmail.com> - October 25, 2020
  !elmerf90 -o regularization-Q.so regularization-Q.F90

  ! Elmer module
  USE DefUtils

  IMPLICIT NONE
  TYPE(Solver_t) :: Solver
  TYPE(Model_t) :: Model
  TYPE(Variable_t), POINTER :: QVar
  INTEGER, POINTER :: QPerm(:), NodeIndexes
  REAL(KIND=dp), POINTER :: JouleHeating(:)
  INTEGER :: ElementNo, N, idn
  REAL(KIND=dp), ALLOCATABLE :: localQ(:)
  TYPE(Element_t), POINTER :: Element
  TYPE(ValueList_t), POINTER :: params
  REAL(KIND=dp) :: Qmin
  LOGICAL :: gotIt, visu
  ALLOCATE(localQ(CurrentModel % MaxElementNodes))

  params => GetSolverParams()
  IF (.NOT. ASSOCIATED(params)) THEN
    CALL Fatal('getRegularizationSolverQ', 'No Parameter found')
  END IF
  Qmin = GetConstReal( params, 'Minimum Joule Heating', gotIt)
  IF (.NOT. gotIt) THEN
    CALL Fatal('getRegularizationSolverQ', 'Minimum Joule Heating')
  END IF
  
  visu = .TRUE.
  IF (visu) THEN
    PRINT 1, Qmin
    1  FORMAT(' Q_min (W): ', EN12.3)
  END IF

  QVar => VariableGet( Solver % Mesh % Variables, 'Joule Heating' )
  IF ( ASSOCIATED( QVar) ) THEN
    QPerm => QVar % Perm
    JouleHeating => QVar % Values
    ! stop if Joule Heating field has not been found !!!!
  ELSE
    CALL Fatal('regularizationSolver-Q', 'No variable Joule Heating found')
  END IF

  DO ElementNo = 1,Solver % NumberOfActiveElements
    Element => GetActiveElement(ElementNo)
    N = GetElementNOFNodes()
    localQ(1:N) = JouleHeating(QPerm(Element % NodeIndexes))
    DO idn = 1, N
      IF (localQ(idn) <= Qmin) THEN
        localQ(idn) = Qmin
      END IF
    END DO
    ! how to reassign in the element the temperature at the node according to the node index. Just doing the way arround seems to work rather well
    JouleHeating(QPerm(Element % NodeIndexes)) = localQ(1:N)
  END DO

END SUBROUTINE getRegularizationSolverQ
