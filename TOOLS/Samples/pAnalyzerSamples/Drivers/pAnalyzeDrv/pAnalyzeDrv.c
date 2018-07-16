
#include <Uefi.h>
#include <Library/UefiLib.h>
#include <Library/UefiBootServicesTableLib.h>
#include <Library/BaseLib.h>

#include <Protocol/SimplePointer.h>
#include <Protocol/pAnalyze.h>

static UINT64 cnt;
EFI_HANDLE  pAnalyzeHandle;
EFI_HANDLE  mHandles;
EFI_SIMPLE_POINTER_PROTOCOL *PrtProtocol;

UINT64
SimplePointerGetStatus (
  EFI_SIMPLE_POINTER_PROTOCOL *PrtProtocol
  )
{
  EFI_SIMPLE_POINTER_STATE    State;

  if (PrtProtocol == NULL) {
    return 0;
  }

  PrtProtocol->GetState (PrtProtocol, &State);

  if ((State.RelativeMovementX != 0) ||
      (State.RelativeMovementY != 0) ||
      (State.RelativeMovementZ != 0) ||
      (State.LeftButton != 0) ||
      (State.RightButton != 0)) {
    return 1;
  }

  return 0;

} // SimplePointerGetStatus

EFI_STATUS
EfiPyTestFunction (
  IN OUT UINT64 *Count
  )
{

  if (SimplePointerGetStatus (PrtProtocol) != 0) {
    cnt += 1;
  }

  *Count = cnt;

  return EFI_SUCCESS;

} // EfiPyTestFunction

EFI_STATUS
EfiPyTestFunctionA (
  IN OUT UINT64 *Count
  )
{

  if (SimplePointerGetStatus (PrtProtocol) != 0) {
    cnt += 1;
  }

  *Count = cnt * 2;

  return EFI_SUCCESS;

} // EfiPyTestFunction

EFIPY_PANALYZE_TEST_PROTOCOL pAnalyzeProtocol = {
  0x01,
  EfiPyTestFunction
};

EFIPY_PANALYZE_TEST_PROTOCOL pAnalyzeProtocolA = {
  0x02,
  EfiPyTestFunctionA
};

EFIPY_PANALYZE_TEST_PROTOCOL2 pAnalyzeProtocol2 = {
  0x10,
  0x20
};

EFIPY_PANALYZE_TEST_PROTOCOL3 pAnalyzeProtocol3 = {
  0x11
};

EFI_STATUS
LocateProtocol (
  EFI_GUID *Guid,
  VOID **Interface
  )
{
  EFI_STATUS  Status;

  Status = gBS->LocateProtocol (
                  Guid,
                  NULL,
                  Interface
                  );

  return Status;
}

EFI_STATUS
EFIAPI
pAnalyzeDrvEntry (
  IN EFI_HANDLE        ImageHandle,
  IN EFI_SYSTEM_TABLE  *SystemTable
  )
{
  EFI_STATUS  Status;

  Print(L"gEfiSimplePointerProtocolGuid: 0x%X\n", &gEfiSimplePointerProtocolGuid);
  Print(L"PrtProtocol: 0x%X\n", &PrtProtocol);
  Status = gBS->LocateProtocol (&gEfiSimplePointerProtocolGuid, NULL, &PrtProtocol);
  if (EFI_ERROR (Status)) {
    Print(L"Locate EFI_SIMPLE_POINTER_PROTOCOL Error %r\n", Status);
    return Status;
  }
  Print(L"Locate EFI_SIMPLE_POINTER_PROTOCOL Success\n");
  Print(L"gEfiSimplePointerProtocolGuid: 0x%X\n", &gEfiSimplePointerProtocolGuid);
  Print(L"PrtProtocol: 0x%X\n", &PrtProtocol);

  Status = gBS->InstallProtocolInterface (
                  &pAnalyzeHandle,
                  &gEfiPypAnalyzeTestProtocol,
                  EFI_NATIVE_INTERFACE,
                  &pAnalyzeProtocol
                  );

  Print(L"Install EFIPY_PANALYZE_TEST_PROTOCOL Result %r\n", Status);

  Status = gBS->InstallMultipleProtocolInterfaces (
                  &mHandles,
                  &gEfiPypAnalyzeTestProtocol2,
                  &pAnalyzeProtocol2,
                  &gEfiPypAnalyzeTestProtocol3,
                  &pAnalyzeProtocol2,
                  NULL
                  );

  if (EFI_ERROR (Status)) {
    Print(L"InstallMultipleProtocolInterfaces error %r\n", Status);
  }
  Print(L"InstallMultipleProtocolInterfaces Status %r\n", Status);

  Status = gBS->UninstallMultipleProtocolInterfaces (
                  mHandles,
                  &gEfiPypAnalyzeTestProtocol2,
                  &pAnalyzeProtocol2,
                  &gEfiPypAnalyzeTestProtocol3,
                  &pAnalyzeProtocol2,
                  NULL
                  );

  Print(L"UninstallMultipleProtocolInterfaces Status %r\n", Status);

  Status = gBS->ReinstallProtocolInterface (
                  pAnalyzeHandle,
                  &gEfiPypAnalyzeTestProtocol,
                  &pAnalyzeProtocol,
                  &pAnalyzeProtocolA
                  );

  Print(L"ReinstallProtocolInterface Status %r\n", Status);

#if (0)
  Status = gBS->UninstallProtocolInterface (
                  pAnalyzeHandle,
                  &gEfiPypAnalyzeTestProtocol,
                  &pAnalyzeProtocolA
                  );

  Print(L"UninstallProtocolInterface Status %r\n", Status);
#endif

  return(0);
}
