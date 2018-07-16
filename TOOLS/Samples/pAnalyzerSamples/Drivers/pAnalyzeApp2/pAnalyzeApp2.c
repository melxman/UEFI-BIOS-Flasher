
#include  <Uefi.h>
#include  <Library/UefiLib.h>
#include <Library/UefiBootServicesTableLib.h>
#include  <Library/ShellCEntryLib.h>

#include <Protocol/pAnalyze.h>

INTN
EFIAPI
ShellAppMain (
  IN UINTN Argc,
  IN CHAR16 **Argv
  )
{

  UINT64      Count;
  EFI_STATUS  Status;
  EFIPY_PANALYZE_TEST_PROTOCOL *pAnalyzeProtocol;

  Status = gBS->LocateProtocol (&gEfiPypAnalyzeTestProtocol, NULL, &pAnalyzeProtocol);
  if (EFI_ERROR (Status)) {
    Print(L"Locate EFIPY_PANALYZE_TEST_PROTOCOL Error %r\n", Status);
    return Status;
  }

  Print(L"pAnalyzer Protocol version:%X\n", pAnalyzeProtocol->Version);

  while (1) {

    gBS->Stall (100 * 1000);
    pAnalyzeProtocol->TestFunc(&Count);
    Print(L"pAnalyzer Protocol count:%X\n", Count);

    if (Count > 10)
      break;
  }


  Print(L"This is pAnalyzer application test\n");

  return(0);
}
