#ifndef __PANALYZE_H__
#define __PANALYZE_H__

#define EFIPY_PANALYZE_TEST_PROTOCOL_GUID \
  { \
    0x82f60aad, 0x45d1, 0x4af7, { 0xba, 0x45, 0xa2, 0x90, 0x84, 0xf6, 0xe4, 0x1b} \
  }

#define EFIPY_PANALYZE_TEST_PROTOCOL2_GUID \
  { \
    0x31e464c5, 0x13f9, 0x4681, { 0x9c, 0x9c, 0xfa, 0x56, 0xd3, 0xbc, 0x89, 0x91} \
  }

#define EFIPY_PANALYZE_TEST_PROTOCOL3_GUID \
  { \
    0x3b4cb5f3, 0x8738, 0x43e6, { 0xae, 0x96, 0x22, 0x2d, 0x8e, 0x56, 0x41, 0xc1} \
  }

typedef struct _EFIPY_PANALYZE_TEST_PROTOCOL    EFIPY_PANALYZE_TEST_PROTOCOL;
typedef struct _EFIPY_PANALYZE_TEST_PROTOCOL2   EFIPY_PANALYZE_TEST_PROTOCOL2;
typedef struct _EFIPY_PANALYZE_TEST_PROTOCOL3   EFIPY_PANALYZE_TEST_PROTOCOL3;

typedef
EFI_STATUS
(EFIAPI *EFIPY_TEST_FUNCTION)(
  IN OUT UINT64 *Count
  );

struct _EFIPY_PANALYZE_TEST_PROTOCOL {
  UINT64                Version;
  EFIPY_TEST_FUNCTION   TestFunc;
};

struct _EFIPY_PANALYZE_TEST_PROTOCOL2 {
  UINT64                MainVersion;
  UINT64                MiniVersion;
};

struct _EFIPY_PANALYZE_TEST_PROTOCOL3 {
  UINT64                Signal;
};

extern EFI_GUID gEfiPypAnalyzeTestProtocol;
extern EFI_GUID gEfiPypAnalyzeTestProtocol2;
extern EFI_GUID gEfiPypAnalyzeTestProtocol3;

#endif // __PANALYZE_H__
