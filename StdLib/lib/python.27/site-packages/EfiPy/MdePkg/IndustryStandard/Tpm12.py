#
# Tpm12.py
#
# Copyright (C) 2015 efipy.core@gmail.com All rights reserved.
#
# Tpm12.py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, version 2 of the License.
#
# EfiPy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with EfiPy.  If not, see <http://www.gnu.org/licenses/>.
#

from EfiPy.MdePkg.IndustryStandard import *

class TPM_KEY (EFIPY_INDUSTRY_STRUCTURE):
  pass

TPM_BASE                    = 0
TPM_AUTH_DATA_USAGE                 = UINT8
TPM_PAYLOAD_TYPE                    = UINT8
TPM_VERSION_BYTE                    = UINT8
TPM_DA_STATE                        = UINT8
TPM_TAG                             = UINT16
TPM_PROTOCOL_ID                     = UINT16
TPM_STARTUP_TYPE                    = UINT16
TPM_ENC_SCHEME                      = UINT16
TPM_SIG_SCHEME                      = UINT16
TPM_MIGRATE_SCHEME                  = UINT16
TPM_PHYSICAL_PRESENCE               = UINT16
TPM_ENTITY_TYPE                     = UINT16
TPM_KEY_USAGE                       = UINT16
TPM_EK_TYPE                         = UINT16
TPM_STRUCTURE_TAG                   = UINT16
TPM_PLATFORM_SPECIFIC               = UINT16
TPM_COMMAND_CODE                    = UINT32
TPM_CAPABILITY_AREA                 = UINT32
TPM_KEY_FLAGS                       = UINT32
TPM_ALGORITHM_ID                    = UINT32
TPM_MODIFIER_INDICATOR              = UINT32
TPM_ACTUAL_COUNT                    = UINT32
TPM_TRANSPORT_ATTRIBUTES            = UINT32
TPM_AUTHHANDLE                      = UINT32
TPM_DIRINDEX                        = UINT32
TPM_KEY_HANDLE                      = UINT32
TPM_PCRINDEX                        = UINT32
TPM_RESULT                          = UINT32
TPM_RESOURCE_TYPE                   = UINT32
TPM_KEY_CONTROL                     = UINT32
TPM_NV_INDEX                        = UINT32
TPM_FAMILY_ID                       = UINT32
TPM_FAMILY_VERIFICATION             = UINT32
TPM_STARTUP_EFFECTS                 = UINT32
TPM_SYM_MODE                        = UINT32
TPM_FAMILY_FLAGS                    = UINT32
TPM_DELEGATE_INDEX                  = UINT32
TPM_CMK_DELEGATE                    = UINT32
TPM_COUNT_ID                        = UINT32
TPM_REDIT_COMMAND                   = UINT32
TPM_TRANSHANDLE                     = UINT32
TPM_HANDLE                          = UINT32
TPM_FAMILY_OPERATION                = UINT32

TPM_Vendor_Specific32       = UINT32(0x00000400).value
TPM_Vendor_Specific8        = UINT8(0x80).value
TPM_TAG_CONTEXTBLOB         = TPM_STRUCTURE_TAG(0x0001).value
TPM_TAG_CONTEXT_SENSITIVE   = TPM_STRUCTURE_TAG(0x0002).value
TPM_TAG_CONTEXTPOINTER      = TPM_STRUCTURE_TAG(0x0003).value
TPM_TAG_CONTEXTLIST         = TPM_STRUCTURE_TAG(0x0004).value
TPM_TAG_SIGNINFO            = TPM_STRUCTURE_TAG(0x0005).value
TPM_TAG_PCR_INFO_LONG       = TPM_STRUCTURE_TAG(0x0006).value
TPM_TAG_PERSISTENT_FLAGS    = TPM_STRUCTURE_TAG(0x0007).value
TPM_TAG_VOLATILE_FLAGS      = TPM_STRUCTURE_TAG(0x0008).value
TPM_TAG_PERSISTENT_DATA     = TPM_STRUCTURE_TAG(0x0009).value
TPM_TAG_VOLATILE_DATA       = TPM_STRUCTURE_TAG(0x000A).value
TPM_TAG_SV_DATA             = TPM_STRUCTURE_TAG(0x000B).value
TPM_TAG_EK_BLOB             = TPM_STRUCTURE_TAG(0x000C).value
TPM_TAG_EK_BLOB_AUTH        = TPM_STRUCTURE_TAG(0x000D).value
TPM_TAG_COUNTER_VALUE       = TPM_STRUCTURE_TAG(0x000E).value
TPM_TAG_TRANSPORT_INTERNAL  = TPM_STRUCTURE_TAG(0x000F).value
TPM_TAG_TRANSPORT_LOG_IN    = TPM_STRUCTURE_TAG(0x0010).value
TPM_TAG_TRANSPORT_LOG_OUT   = TPM_STRUCTURE_TAG(0x0011).value
TPM_TAG_AUDIT_EVENT_IN      = TPM_STRUCTURE_TAG(0x0012).value
TPM_TAG_AUDIT_EVENT_OUT     = TPM_STRUCTURE_TAG(0x0013).value
TPM_TAG_CURRENT_TICKS       = TPM_STRUCTURE_TAG(0x0014).value
TPM_TAG_KEY                 = TPM_STRUCTURE_TAG(0x0015).value
TPM_TAG_STORED_DATA12       = TPM_STRUCTURE_TAG(0x0016).value
TPM_TAG_NV_ATTRIBUTES       = TPM_STRUCTURE_TAG(0x0017).value
TPM_TAG_NV_DATA_PUBLIC      = TPM_STRUCTURE_TAG(0x0018).value
TPM_TAG_NV_DATA_SENSITIVE   = TPM_STRUCTURE_TAG(0x0019).value
TPM_TAG_DELEGATIONS         = TPM_STRUCTURE_TAG(0x001A).value
TPM_TAG_DELEGATE_PUBLIC     = TPM_STRUCTURE_TAG(0x001B).value
TPM_TAG_DELEGATE_TABLE_ROW  = TPM_STRUCTURE_TAG(0x001C).value
TPM_TAG_TRANSPORT_AUTH      = TPM_STRUCTURE_TAG(0x001D).value
TPM_TAG_TRANSPORT_PUBLIC    = TPM_STRUCTURE_TAG(0x001E).value
TPM_TAG_PERMANENT_FLAGS     = TPM_STRUCTURE_TAG(0x001F).value
TPM_TAG_STCLEAR_FLAGS       = TPM_STRUCTURE_TAG(0x0020).value
TPM_TAG_STANY_FLAGS         = TPM_STRUCTURE_TAG(0x0021).value
TPM_TAG_PERMANENT_DATA      = TPM_STRUCTURE_TAG(0x0022).value
TPM_TAG_STCLEAR_DATA        = TPM_STRUCTURE_TAG(0x0023).value
TPM_TAG_STANY_DATA          = TPM_STRUCTURE_TAG(0x0024).value
TPM_TAG_FAMILY_TABLE_ENTRY  = TPM_STRUCTURE_TAG(0x0025).value
TPM_TAG_DELEGATE_SENSITIVE  = TPM_STRUCTURE_TAG(0x0026).value
TPM_TAG_DELG_KEY_BLOB       = TPM_STRUCTURE_TAG(0x0027).value
TPM_TAG_KEY12               = TPM_STRUCTURE_TAG(0x0028).value
TPM_TAG_CERTIFY_INFO2       = TPM_STRUCTURE_TAG(0x0029).value
TPM_TAG_DELEGATE_OWNER_BLOB = TPM_STRUCTURE_TAG(0x002A).value
TPM_TAG_EK_BLOB_ACTIVATE    = TPM_STRUCTURE_TAG(0x002B).value
TPM_TAG_DAA_BLOB            = TPM_STRUCTURE_TAG(0x002C).value
TPM_TAG_DAA_CONTEXT         = TPM_STRUCTURE_TAG(0x002D).value
TPM_TAG_DAA_ENFORCE         = TPM_STRUCTURE_TAG(0x002E).value
TPM_TAG_DAA_ISSUER          = TPM_STRUCTURE_TAG(0x002F).value
TPM_TAG_CAP_VERSION_INFO    = TPM_STRUCTURE_TAG(0x0030).value
TPM_TAG_DAA_SENSITIVE       = TPM_STRUCTURE_TAG(0x0031).value
TPM_TAG_DAA_TPM             = TPM_STRUCTURE_TAG(0x0032).value
TPM_TAG_CMK_MIGAUTH         = TPM_STRUCTURE_TAG(0x0033).value
TPM_TAG_CMK_SIGTICKET       = TPM_STRUCTURE_TAG(0x0034).value
TPM_TAG_CMK_MA_APPROVAL     = TPM_STRUCTURE_TAG(0x0035).value
TPM_TAG_QUOTE_INFO2         = TPM_STRUCTURE_TAG(0x0036).value
TPM_TAG_DA_INFO             = TPM_STRUCTURE_TAG(0x0037).value
TPM_TAG_DA_LIMITED          = TPM_STRUCTURE_TAG(0x0038).value
TPM_TAG_DA_ACTION_TYPE      = TPM_STRUCTURE_TAG(0x0039).value
TPM_RT_KEY                  = TPM_RESOURCE_TYPE(0x00000001).value
TPM_RT_AUTH                 = TPM_RESOURCE_TYPE(0x00000002).value
TPM_RT_HASH                 = TPM_RESOURCE_TYPE(0x00000003).value
TPM_RT_TRANS                = TPM_RESOURCE_TYPE(0x00000004).value
TPM_RT_CONTEXT              = TPM_RESOURCE_TYPE(0x00000005).value
TPM_RT_COUNTER              = TPM_RESOURCE_TYPE(0x00000006).value
TPM_RT_DELEGATE             = TPM_RESOURCE_TYPE(0x00000007).value
TPM_RT_DAA_TPM              = TPM_RESOURCE_TYPE(0x00000008).value
TPM_RT_DAA_V0               = TPM_RESOURCE_TYPE(0x00000009).value
TPM_RT_DAA_V1               = TPM_RESOURCE_TYPE(0x0000000A).value

TPM_PT_ASYM                 = TPM_PAYLOAD_TYPE(0x01).value
TPM_PT_BIND                 = TPM_PAYLOAD_TYPE(0x02).value
TPM_PT_MIGRATE              = TPM_PAYLOAD_TYPE(0x03).value
TPM_PT_MAINT                = TPM_PAYLOAD_TYPE(0x04).value
TPM_PT_SEAL                 = TPM_PAYLOAD_TYPE(0x05).value
TPM_PT_MIGRATE_RESTRICTED   = TPM_PAYLOAD_TYPE(0x06).value
TPM_PT_MIGRATE_EXTERNAL     = TPM_PAYLOAD_TYPE(0x07).value
TPM_PT_CMK_MIGRATE          = TPM_PAYLOAD_TYPE(0x08).value
TPM_PT_VENDOR_SPECIFIC      = TPM_PAYLOAD_TYPE(0x80).value

TPM_ET_KEYHANDLE            = UINT16(0x0001).value
TPM_ET_OWNER                = UINT16(0x0002).value
TPM_ET_DATA                 = UINT16(0x0003).value
TPM_ET_SRK                  = UINT16(0x0004).value
TPM_ET_KEY                  = UINT16(0x0005).value
TPM_ET_REVOKE               = UINT16(0x0006).value
TPM_ET_DEL_OWNER_BLOB       = UINT16(0x0007).value
TPM_ET_DEL_ROW              = UINT16(0x0008).value
TPM_ET_DEL_KEY_BLOB         = UINT16(0x0009).value
TPM_ET_COUNTER              = UINT16(0x000A).value
TPM_ET_NV                   = UINT16(0x000B).value
TPM_ET_OPERATOR             = UINT16(0x000C).value
TPM_ET_RESERVED_HANDLE      = UINT16(0x0040).value

TPM_ET_XOR                  = UINT16(0x0000).value
TPM_ET_AES128               = UINT16(0x0006).value
TPM_KH_SRK                  = TPM_KEY_HANDLE(0x40000000).value
TPM_KH_OWNER                = TPM_KEY_HANDLE(0x40000001).value
TPM_KH_REVOKE               = TPM_KEY_HANDLE(0x40000002).value
TPM_KH_TRANSPORT            = TPM_KEY_HANDLE(0x40000003).value
TPM_KH_OPERATOR             = TPM_KEY_HANDLE(0x40000004).value
TPM_KH_ADMIN                = TPM_KEY_HANDLE(0x40000005).value
TPM_KH_EK                   = TPM_KEY_HANDLE(0x40000006).value

TPM_ST_CLEAR                = TPM_STARTUP_TYPE(0x0001).value
TPM_ST_STATE                = TPM_STARTUP_TYPE(0x0002).value
TPM_ST_DEACTIVATED          = TPM_STARTUP_TYPE(0x0003).value

TPM_PID_OIAP                = TPM_PROTOCOL_ID(0x0001).value
TPM_PID_OSAP                = TPM_PROTOCOL_ID(0x0002).value
TPM_PID_ADIP                = TPM_PROTOCOL_ID(0x0003).value
TPM_PID_ADCP                = TPM_PROTOCOL_ID(0x0004).value
TPM_PID_OWNER               = TPM_PROTOCOL_ID(0x0005).value
TPM_PID_DSAP                = TPM_PROTOCOL_ID(0x0006).value
TPM_PID_TRANSPORT           = TPM_PROTOCOL_ID(0x0007).value

TPM_ALG_RSA                 = TPM_ALGORITHM_ID(0x00000001).value
TPM_ALG_DES                 = TPM_ALGORITHM_ID(0x00000002).value
TPM_ALG_3DES                = TPM_ALGORITHM_ID(0x00000003).value
TPM_ALG_SHA                 = TPM_ALGORITHM_ID(0x00000004).value
TPM_ALG_HMAC                = TPM_ALGORITHM_ID(0x00000005).value
TPM_ALG_AES128              = TPM_ALGORITHM_ID(0x00000006).value
TPM_ALG_MGF1                = TPM_ALGORITHM_ID(0x00000007).value
TPM_ALG_AES192              = TPM_ALGORITHM_ID(0x00000008).value
TPM_ALG_AES256              = TPM_ALGORITHM_ID(0x00000009).value
TPM_ALG_XOR                 = TPM_ALGORITHM_ID(0x0000000A).value

TPM_PHYSICAL_PRESENCE_HW_DISABLE    = TPM_PHYSICAL_PRESENCE(0x0200).value
TPM_PHYSICAL_PRESENCE_CMD_DISABLE   = TPM_PHYSICAL_PRESENCE(0x0100).value
TPM_PHYSICAL_PRESENCE_LIFETIME_LOCK = TPM_PHYSICAL_PRESENCE(0x0080).value
TPM_PHYSICAL_PRESENCE_HW_ENABLE     = TPM_PHYSICAL_PRESENCE(0x0040).value
TPM_PHYSICAL_PRESENCE_CMD_ENABLE    = TPM_PHYSICAL_PRESENCE(0x0020).value
TPM_PHYSICAL_PRESENCE_NOTPRESENT    = TPM_PHYSICAL_PRESENCE(0x0010).value
TPM_PHYSICAL_PRESENCE_PRESENT       = TPM_PHYSICAL_PRESENCE(0x0008).value
TPM_PHYSICAL_PRESENCE_LOCK          = TPM_PHYSICAL_PRESENCE(0x0004).value

TPM_MS_MIGRATE                      = TPM_MIGRATE_SCHEME(0x0001).value
TPM_MS_REWRAP                       = TPM_MIGRATE_SCHEME(0x0002).value
TPM_MS_MAINT                        = TPM_MIGRATE_SCHEME(0x0003).value
TPM_MS_RESTRICT_MIGRATE             = TPM_MIGRATE_SCHEME(0x0004).value
TPM_MS_RESTRICT_APPROVE_DOUBLE      = TPM_MIGRATE_SCHEME(0x0005).value

TPM_EK_TYPE_ACTIVATE        = TPM_EK_TYPE(0x0001).value
TPM_EK_TYPE_AUTH            = TPM_EK_TYPE(0x0002).value

TPM_PS_PC_11                = TPM_PLATFORM_SPECIFIC(0x0001).value
TPM_PS_PC_12                = TPM_PLATFORM_SPECIFIC(0x0002).value
TPM_PS_PDA_12               = TPM_PLATFORM_SPECIFIC(0x0003).value
TPM_PS_Server_12            = TPM_PLATFORM_SPECIFIC(0x0004).value
TPM_PS_Mobile_12            = TPM_PLATFORM_SPECIFIC(0x0005).value

class TPM_STRUCT_VER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     UINT8),
    ("minor",     UINT8),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

class TPM_VERSION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",     TPM_VERSION_BYTE),
    ("minor",     TPM_VERSION_BYTE),
    ("revMajor",  UINT8),
    ("revMinor",  UINT8)
  ]

TPM_SHA1_160_HASH_LEN       = 0x14
TPM_SHA1BASED_NONCE_LEN     = TPM_SHA1_160_HASH_LEN

class TPM_DIGEST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("digest",  UINT8 * TPM_SHA1_160_HASH_LEN)
  ]

TPM_CHOSENID_HASH                   = TPM_DIGEST
TPM_COMPOSITE_HASH                  = TPM_DIGEST
TPM_DIRVALUE                        = TPM_DIGEST
TPM_HMAC                            = TPM_DIGEST
TPM_PCRVALUE                        = TPM_DIGEST
TPM_AUDITDIGEST                     = TPM_DIGEST

class TPM_NONCE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("nonce",  UINT8 * 20)
  ]

TPM_DAA_TPM_SEED                  = TPM_NONCE
TPM_DAA_CONTEXT_SEED              = TPM_NONCE

tdTPM_AUTHDATA                    = UINT8 * 20
TPM_AUTHDATA                      = tdTPM_AUTHDATA
TPM_SECRET                        = TPM_AUTHDATA
TPM_ENCAUTH                       = TPM_AUTHDATA

class TPM_KEY_HANDLE_LIST (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("loaded",  UINT16),
    ("handle",  TPM_KEY_HANDLE * 1)
  ]

TPM_KEY_SIGNING             = UINT16(0x0010).value
TPM_KEY_STORAGE             = UINT16(0x0011).value
TPM_KEY_IDENTITY            = UINT16(0x0012).value
TPM_KEY_AUTHCHANGE          = UINT16(0x0013).value
TPM_KEY_BIND                = UINT16(0x0014).value
TPM_KEY_LEGACY              = UINT16(0x0015).value
TPM_KEY_MIGRATE             = UINT16(0x0016).value
TPM_ES_NONE                 = TPM_ENC_SCHEME(0x0001).value
TPM_ES_RSAESPKCSv15         = TPM_ENC_SCHEME(0x0002).value
TPM_ES_RSAESOAEP_SHA1_MGF1  = TPM_ENC_SCHEME(0x0003).value
TPM_ES_SYM_CNT              = TPM_ENC_SCHEME(0x0004).value
TPM_ES_SYM_CTR              = TPM_ENC_SCHEME(0x0004).value
TPM_ES_SYM_OFB              = TPM_ENC_SCHEME(0x0005).value

TPM_SS_NONE                 = TPM_SIG_SCHEME(0x0001).value
TPM_SS_RSASSAPKCS1v15_SHA1  = TPM_SIG_SCHEME(0x0002).value
TPM_SS_RSASSAPKCS1v15_DER   = TPM_SIG_SCHEME(0x0003).value
TPM_SS_RSASSAPKCS1v15_INFO  = TPM_SIG_SCHEME(0x0004).value

TPM_AUTH_NEVER              = TPM_AUTH_DATA_USAGE(0x00).value
TPM_AUTH_ALWAYS             = TPM_AUTH_DATA_USAGE(0x01).value
TPM_AUTH_PRIV_USE_ONLY      = TPM_AUTH_DATA_USAGE(0x03).value

redirection                       = 0x00000001
migratable                        = 0x00000002
isVolatile                        = 0x00000004
pcrIgnoredOnRead                  = 0x00000008
migrateAuthority                  = 0x00000010
TPM_KEY_FLAGS_BITS = ENUM

class TPM_CHANGEAUTH_VALIDATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("newAuthSecret", TPM_SECRET),
    ("n1",            TPM_NONCE)
  ]

class TPM_KEY_PARMS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmID", TPM_ALGORITHM_ID),
    ("encScheme",   TPM_ENC_SCHEME),
    ("sigScheme",   TPM_SIG_SCHEME),
    ("parmSize",    UINT32),
    ("parms",       POINTER (UINT8))
  ]

class TPM_STORE_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       UINT8 * 1)
  ]

class TPM_PUBKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubKey",          TPM_STORE_PUBKEY)
  ]

class TPM_MIGRATIONKEYAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationKey",    TPM_PUBKEY),
    ("migrationScheme", TPM_MIGRATE_SCHEME),
    ("digest",          TPM_DIGEST)
  ]

class TPM_COUNTER_VALUE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("label",   UINT8 * 4),
    ("counter", TPM_ACTUAL_COUNT)
  ]

class TPM_SIGN_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("fixed",   UINT8 * 4),
    ("replay",  TPM_NONCE),
    ("dataLen", UINT32),
    ("data",    POINTER (UINT8))
  ]

class TPM_MSA_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("MSAlist",       UINT32),
    ("migAuthDigest", TPM_DIGEST * 1)
  ]

class TPM_CMK_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("migrationAuthorityDigest",  TPM_DIGEST),
    ("destinationKeyDigest",      TPM_DIGEST),
    ("sourceKeyDigest",           TPM_DIGEST)
  ]

TPM_CMK_DELEGATE_SIGNING    = TPM_CMK_DELEGATE(BIT31).value
TPM_CMK_DELEGATE_STORAGE    = TPM_CMK_DELEGATE(BIT30).value
TPM_CMK_DELEGATE_BIND       = TPM_CMK_DELEGATE(BIT29).value
TPM_CMK_DELEGATE_LEGACY     = TPM_CMK_DELEGATE(BIT28).value
TPM_CMK_DELEGATE_MIGRATE    = TPM_CMK_DELEGATE(BIT27).value

class TPM_SELECT_SIZE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("major",   UINT8),
    ("minor",   UINT8),
    ("reqSize", UINT16)
  ]

class TPM_CMK_MIGAUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("msaDigest",     TPM_DIGEST),
    ("pubKeyDigest",  TPM_DIGEST)
  ]

class TPM_CMK_SIGTICKET (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("verKeyDigest",  TPM_DIGEST),
    ("signedData",    TPM_DIGEST)
  ]

class TPM_CMK_MA_APPROVAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("migrationAuthorityDigest",  TPM_DIGEST)
  ]

TPM_TAG_RQU_COMMAND         = TPM_STRUCTURE_TAG(0x00C1).value
TPM_TAG_RQU_AUTH1_COMMAND   = TPM_STRUCTURE_TAG(0x00C2).value
TPM_TAG_RQU_AUTH2_COMMAND   = TPM_STRUCTURE_TAG(0x00C3).value
TPM_TAG_RSP_COMMAND         = TPM_STRUCTURE_TAG(0x00C4).value
TPM_TAG_RSP_AUTH1_COMMAND   = TPM_STRUCTURE_TAG(0x00C5).value
TPM_TAG_RSP_AUTH2_COMMAND   = TPM_STRUCTURE_TAG(0x00C6).value

class TPM_PERMANENT_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                           TPM_STRUCTURE_TAG),
    ("disable",                       BOOLEAN),
    ("ownership",                     BOOLEAN),
    ("deactivated",                   BOOLEAN),
    ("readPubek",                     BOOLEAN),
    ("disableOwnerClear",             BOOLEAN),
    ("allowMaintenance",              BOOLEAN),
    ("physicalPresenceLifetimeLock",  BOOLEAN),
    ("physicalPresenceHWEnable",      BOOLEAN),
    ("physicalPresenceCMDEnable",     BOOLEAN),
    ("CEKPUsed",                      BOOLEAN),
    ("TPMpost",                       BOOLEAN),
    ("TPMpostLock",                   BOOLEAN),
    ("FIPS",                          BOOLEAN),
    ("operator",                      BOOLEAN),
    ("enableRevokeEK",                BOOLEAN),
    ("nvLocked",                      BOOLEAN),
    ("readSRKPub",                    BOOLEAN),
    ("tpmEstablished",                BOOLEAN),
    ("maintenanceDone",               BOOLEAN),
    ("disableFullDALogicInfo",        BOOLEAN)
  ]

TPM_PF_DISABLE                      = TPM_CAPABILITY_AREA(1).value
TPM_PF_OWNERSHIP                    = TPM_CAPABILITY_AREA(2).value
TPM_PF_DEACTIVATED                  = TPM_CAPABILITY_AREA(3).value
TPM_PF_READPUBEK                    = TPM_CAPABILITY_AREA(4).value
TPM_PF_DISABLEOWNERCLEAR            = TPM_CAPABILITY_AREA(5).value
TPM_PF_ALLOWMAINTENANCE             = TPM_CAPABILITY_AREA(6).value
TPM_PF_PHYSICALPRESENCELIFETIMELOCK = TPM_CAPABILITY_AREA(7).value
TPM_PF_PHYSICALPRESENCEHWENABLE     = TPM_CAPABILITY_AREA(8).value
TPM_PF_PHYSICALPRESENCECMDENABLE    = TPM_CAPABILITY_AREA(9).value
TPM_PF_CEKPUSED                     = TPM_CAPABILITY_AREA(10).value
TPM_PF_TPMPOST                      = TPM_CAPABILITY_AREA(11).value
TPM_PF_TPMPOSTLOCK                  = TPM_CAPABILITY_AREA(12).value
TPM_PF_FIPS                         = TPM_CAPABILITY_AREA(13).value
TPM_PF_OPERATOR                     = TPM_CAPABILITY_AREA(14).value
TPM_PF_ENABLEREVOKEEK               = TPM_CAPABILITY_AREA(15).value
TPM_PF_NV_LOCKED                    = TPM_CAPABILITY_AREA(16).value
TPM_PF_READSRKPUB                   = TPM_CAPABILITY_AREA(17).value
TPM_PF_TPMESTABLISHED               = TPM_CAPABILITY_AREA(18).value
TPM_PF_MAINTENANCEDONE              = TPM_CAPABILITY_AREA(19).value
TPM_PF_DISABLEFULLDALOGICINFO       = TPM_CAPABILITY_AREA(20).value

class TPM_STCLEAR_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("deactivated",           BOOLEAN),
    ("disableForceClear",     BOOLEAN),
    ("physicalPresence",      BOOLEAN),
    ("physicalPresenceLock",  BOOLEAN),
    ("bGlobalLock",           BOOLEAN)
  ]

TPM_SF_DEACTIVATED          = TPM_CAPABILITY_AREA(1).value
TPM_SF_DISABLEFORCECLEAR    = TPM_CAPABILITY_AREA(2).value
TPM_SF_PHYSICALPRESENCE     = TPM_CAPABILITY_AREA(3).value
TPM_SF_PHYSICALPRESENCELOCK = TPM_CAPABILITY_AREA(4).value
TPM_SF_BGLOBALLOCK          = TPM_CAPABILITY_AREA(5).value

class TPM_STANY_FLAGS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("postInitialise",      BOOLEAN),
    ("localityModifier",    TPM_MODIFIER_INDICATOR),
    ("transportExclusive",  BOOLEAN),
    ("TOSPresent",          BOOLEAN)
  ]

TPM_AF_POSTINITIALISE       = TPM_CAPABILITY_AREA(1).value
TPM_AF_LOCALITYMODIFIER     = TPM_CAPABILITY_AREA(2).value
TPM_AF_TRANSPORTEXCLUSIVE   = TPM_CAPABILITY_AREA(3).value
TPM_AF_TOSPRESENT           = TPM_CAPABILITY_AREA(4).value

TPM_MIN_COUNTERS            = 4
TPM_DELEGATE_KEY            = TPM_KEY
TPM_NUM_PCR                 = 16
TPM_MAX_NV_WRITE_NOOWNER    = 64

TPM_PD_REVMAJOR               = TPM_CAPABILITY_AREA(1).value
TPM_PD_REVMINOR               = TPM_CAPABILITY_AREA(2).value
TPM_PD_TPMPROOF               = TPM_CAPABILITY_AREA(3).value
TPM_PD_OWNERAUTH              = TPM_CAPABILITY_AREA(4).value
TPM_PD_OPERATORAUTH           = TPM_CAPABILITY_AREA(5).value
TPM_PD_MANUMAINTPUB           = TPM_CAPABILITY_AREA(6).value
TPM_PD_ENDORSEMENTKEY         = TPM_CAPABILITY_AREA(7).value
TPM_PD_SRK                    = TPM_CAPABILITY_AREA(8).value
TPM_PD_DELEGATEKEY            = TPM_CAPABILITY_AREA(9).value
TPM_PD_CONTEXTKEY             = TPM_CAPABILITY_AREA(10).value
TPM_PD_AUDITMONOTONICCOUNTER  = TPM_CAPABILITY_AREA(11).value
TPM_PD_MONOTONICCOUNTER       = TPM_CAPABILITY_AREA(12).value
TPM_PD_PCRATTRIB              = TPM_CAPABILITY_AREA(13).value
TPM_PD_ORDINALAUDITSTATUS     = TPM_CAPABILITY_AREA(14).value
TPM_PD_AUTHDIR                = TPM_CAPABILITY_AREA(15).value
TPM_PD_RNGSTATE               = TPM_CAPABILITY_AREA(16).value
TPM_PD_FAMILYTABLE            = TPM_CAPABILITY_AREA(17).value
TPM_DELEGATETABLE             = TPM_CAPABILITY_AREA(18).value
TPM_PD_EKRESET                = TPM_CAPABILITY_AREA(19).value
TPM_PD_MAXNVBUFSIZE           = TPM_CAPABILITY_AREA(20).value
TPM_PD_LASTFAMILYID           = TPM_CAPABILITY_AREA(21).value
TPM_PD_NOOWNERNVWRITE         = TPM_CAPABILITY_AREA(22).value
TPM_PD_RESTRICTDELEGATE       = TPM_CAPABILITY_AREA(23).value
TPM_PD_TPMDAASEED             = TPM_CAPABILITY_AREA(24).value
TPM_PD_DAAPROOF               = TPM_CAPABILITY_AREA(25).value

class TPM_STCLEAR_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                       TPM_STRUCTURE_TAG),
    ("contextNonceKey",           TPM_NONCE),
    ("countID",                   TPM_COUNT_ID),
    ("ownerReference",            UINT32),
    ("disableResetLock",          BOOLEAN),
    ("PCR",                       TPM_PCRVALUE * TPM_NUM_PCR),
    ("deferredPhysicalPresence",  UINT32)
  ]

TPM_SD_CONTEXTNONCEKEY            = TPM_CAPABILITY_AREA(0x00000001).value
TPM_SD_COUNTID                    = TPM_CAPABILITY_AREA(0x00000002).value
TPM_SD_OWNERREFERENCE             = TPM_CAPABILITY_AREA(0x00000003).value
TPM_SD_DISABLERESETLOCK           = TPM_CAPABILITY_AREA(0x00000004).value
TPM_SD_PCR                        = TPM_CAPABILITY_AREA(0x00000005).value
TPM_SD_DEFERREDPHYSICALPRESENCE   = TPM_CAPABILITY_AREA(0x00000006).value

TPM_AD_CONTEXTNONCESESSION        = TPM_CAPABILITY_AREA(1).value
TPM_AD_AUDITDIGEST                = TPM_CAPABILITY_AREA(2).value
TPM_AD_CURRENTTICKS               = TPM_CAPABILITY_AREA(3).value
TPM_AD_CONTEXTCOUNT               = TPM_CAPABILITY_AREA(4).value
TPM_AD_CONTEXTLIST                = TPM_CAPABILITY_AREA(5).value
TPM_AD_SESSIONS                   = TPM_CAPABILITY_AREA(6).value

class TPM_PCR_SELECTION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sizeOfSelect",  UINT16),
    ("pcrSelect",     UINT8 * 1)
  ]

class TPM_PCR_COMPOSITE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("select",    TPM_PCR_SELECTION),
    ("valueSize", UINT32),
    ("pcrValue",  TPM_PCRVALUE * 1)
  ]

class TPM_PCR_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH),
    ("digestAtCreation",  TPM_COMPOSITE_HASH)
  ]

TPM_LOCALITY_SELECTION = UINT8

TPM_LOC_FOUR                = UINT8(0x10).value
TPM_LOC_THREE               = UINT8(0x08).value
TPM_LOC_TWO                 = UINT8(0x04).value
TPM_LOC_ONE                 = UINT8(0x02).value
TPM_LOC_ZERO                = UINT8(0x01).value

class TPM_PCR_INFO_LONG (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                   TPM_STRUCTURE_TAG),
    ("localityAtCreation",    TPM_LOCALITY_SELECTION),
    ("localityAtRelease",     TPM_LOCALITY_SELECTION),
    ("creationPCRSelection",  TPM_PCR_SELECTION),
    ("releasePCRSelection",   TPM_PCR_SELECTION),
    ("digestAtCreation",      TPM_COMPOSITE_HASH),
    ("digestAtRelease",       TPM_COMPOSITE_HASH)
  ]

class TPM_PCR_INFO_SHORT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrSelection",      TPM_PCR_SELECTION),
    ("localityAtRelease", TPM_LOCALITY_SELECTION),
    ("digestAtRelease",   TPM_COMPOSITE_HASH)
  ]

class TPM_PCR_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("pcrReset",        BOOLEAN),
    ("pcrExtendLocal",  TPM_LOCALITY_SELECTION),
    ("pcrResetLocal",   TPM_LOCALITY_SELECTION)
  ]

class TPM_STORED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",           TPM_STRUCT_VER),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

class TPM_STORED_DATA12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("et",            TPM_ENTITY_TYPE),
    ("sealInfoSize",  UINT32),
    ("sealInfo",      POINTER (UINT8)),
    ("encDataSize",   UINT32),
    ("encData",       POINTER (UINT8))
  ]

class TPM_SEALED_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("authData",      TPM_SECRET),
    ("tpmProof",      TPM_NONCE),
    ("storedDigest",  TPM_DIGEST),
    ("dataSize",      UINT32),
    ("data",          POINTER (UINT8))
  ]

class TPM_SYMMETRIC_KEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("algId",     TPM_ALGORITHM_ID),
    ("encScheme", TPM_ENC_SCHEME),
    ("dataSize",  UINT16),
    ("data",      POINTER (UINT8))
  ]

class TPM_BOUND_DATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",         TPM_STRUCT_VER),
    ("payload",     TPM_PAYLOAD_TYPE),
    ("payloadData", UINT8 * 1)
  ]


TPM_KEY._fields_ = [
    ("ver",             TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

class TPM_KEY12 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("fill",            UINT16),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8)),
    ("pubKey",          TPM_STORE_PUBKEY),
    ("encDataSize",     UINT32),
    ("encData",         POINTER (UINT8))
  ]

class TPM_STORE_PRIVKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("keyLength", UINT32),
    ("key",       POINTER (UINT8))
  ]

class TPM_STORE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",       TPM_PAYLOAD_TYPE),
    ("usageAuth",     TPM_SECRET),
    ("migrationAuth", TPM_SECRET),
    ("pubDataDigest", TPM_DIGEST),
    ("privKey",       TPM_STORE_PRIVKEY)
  ]

class TPM_MIGRATE_ASYMKEY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("payload",         TPM_PAYLOAD_TYPE),
    ("usageAuth",       TPM_SECRET),
    ("pubDataDigest",   TPM_DIGEST),
    ("partPrivKeyLen",  UINT32),
    ("partPrivKey",     POINTER (UINT8))
  ]

TPM_KEY_CONTROL_OWNER_EVICT = UINT32(0x00000001).value

class TPM_CERTIFY_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",         TPM_STRUCT_VER),
    ("keyUsage",        TPM_KEY_USAGE),
    ("keyFlags",        TPM_KEY_FLAGS),
    ("authDataUsage",   TPM_AUTH_DATA_USAGE),
    ("algorithmParms",  TPM_KEY_PARMS),
    ("pubkeyDigest",    TPM_DIGEST),
    ("data",            TPM_NONCE),
    ("parentPCRStatus", BOOLEAN),
    ("PCRInfoSize",     UINT32),
    ("PCRInfo",         POINTER (UINT8))
  ]

class TPM_CERTIFY_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                     TPM_STRUCTURE_TAG),
    ("fill",                    UINT8),
    ("payloadType",             TPM_PAYLOAD_TYPE),
    ("keyUsage",                TPM_KEY_USAGE),
    ("keyFlags",                TPM_KEY_FLAGS),
    ("authDataUsage",           TPM_AUTH_DATA_USAGE),
    ("algorithmParms",          TPM_KEY_PARMS),
    ("pubkeyDigest",            TPM_DIGEST),
    ("data",                    TPM_NONCE),
    ("parentPCRStatus",         BOOLEAN),
    ("PCRInfoSize",             UINT32),
    ("PCRInfo",                 POINTER(UINT8)),
    ("migrationAuthoritySize",  UINT32),
    ("migrationAuthority",      POINTER (UINT8))
  ]

class TPM_QUOTE_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("version",       TPM_STRUCT_VER),
    ("fixed",         UINT8 * 4),
    ("digestValue",   TPM_COMPOSITE_HASH),
    ("externalData",  TPM_NONCE)
  ]

class TPM_QUOTE_INFO2 (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("fixed",         UINT8 * 4),
    ("externalData",  TPM_NONCE),
    ("infoShort",     TPM_PCR_INFO_SHORT)
  ]

class TPM_EK_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("ekType",    TPM_EK_TYPE),
    ("blobSize",  UINT32),
    ("blob",      POINTER (UINT8))
  ]

class TPM_EK_BLOB_ACTIVATE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST),
    ("pcrInfo",     TPM_PCR_INFO_SHORT)
  ]

class TPM_EK_BLOB_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("authValue",   TPM_SECRET)
  ]

class TPM_IDENTITY_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",               TPM_STRUCT_VER),
    ("ordinal",           UINT32),
    ("labelPrivCADigest", TPM_CHOSENID_HASH),
    ("identityPubKey",    TPM_PUBKEY)
  ]

class TPM_IDENTITY_REQ (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("asymSize",      UINT32),
    ("symSize",       UINT32),
    ("asymAlgorithm", TPM_KEY_PARMS),
    ("symAlgorithm",  TPM_KEY_PARMS),
    ("asymBlob",      POINTER (UINT8)),
    ("symBlob",       POINTER (UINT8))
  ]

class TPM_IDENTITY_PROOF (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("ver",                   TPM_STRUCT_VER),
    ("labelSize",             UINT32),
    ("identityBindingSize",   UINT32),
    ("endorsementSize",       UINT32),
    ("platformSize",          UINT32),
    ("conformanceSize",       UINT32),
    ("identityKey",           TPM_PUBKEY),
    ("labelArea",             POINTER (UINT8)),
    ("identityBinding",       POINTER (UINT8)),
    ("endorsementCredential", POINTER (UINT8)),
    ("platformCredential",    POINTER (UINT8)),
    ("conformanceCredential", POINTER (UINT8))
  ]

class TPM_ASYM_CA_CONTENTS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("sessionKey",  TPM_SYMMETRIC_KEY),
    ("idDigest",    TPM_DIGEST)
  ]

class TPM_SYM_CA_ATTESTATION (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("credSize",    UINT32),
    ("algorithm",   TPM_KEY_PARMS),
    ("credential",  POINTER (UINT8))
  ]

class TPM_CURRENT_TICKS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("currentTicks",  UINT64),
    ("tickRate",      UINT16),
    ("tickNonce",     TPM_NONCE)
  ]

class TPM_TRANSPORT_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("transAttributes", TPM_TRANSPORT_ATTRIBUTES),
    ("algId",           TPM_ALGORITHM_ID),
    ("encScheme",       TPM_ENC_SCHEME)
  ]

TPM_TRANSPORT_ENCRYPT       = UINT32(BIT0).value
TPM_TRANSPORT_LOG           = UINT32(BIT1).value
TPM_TRANSPORT_EXCLUSIVE     = UINT32(BIT2).value

class TPM_TRANSPORT_INTERNAL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("authData",        TPM_AUTHDATA),
    ("transPublic",     TPM_TRANSPORT_PUBLIC),
    ("transHandle",     TPM_TRANSHANDLE),
    ("transNonceEven",  TPM_NONCE),
    ("transDigest",     TPM_DIGEST)
  ]

class TPM_TRANSPORT_LOG_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("parameters",      TPM_DIGEST),
    ("pubKeyHash",      TPM_DIGEST)
  ]

class TPM_TRANSPORT_LOG_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("currentTicks",    TPM_CURRENT_TICKS),
    ("parameters",      TPM_DIGEST),
    ("locality",        TPM_MODIFIER_INDICATOR)
  ]

class TPM_TRANSPORT_AUTH (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authData",  TPM_AUTHDATA)
  ]

class TPM_AUDIT_EVENT_IN (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("inputParms",  TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE)
  ]

class TPM_AUDIT_EVENT_OUT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("ordinal",     TPM_COMMAND_CODE),
    ("outputParms", TPM_DIGEST),
    ("auditCount",  TPM_COUNTER_VALUE),
    ("returnCode",  TPM_RESULT)
  ]

TPM_VENDOR_ERROR            = TPM_Vendor_Specific32
TPM_NON_FATAL               = 0x00000800
TPM_SUCCESS                 = TPM_RESULT(TPM_BASE).value
TPM_AUTHFAIL                = TPM_RESULT(TPM_BASE + 1).value
TPM_BADINDEX                = TPM_RESULT(TPM_BASE + 2).value
TPM_BAD_PARAMETER           = TPM_RESULT(TPM_BASE + 3).value
TPM_AUDITFAILURE            = TPM_RESULT(TPM_BASE + 4).value
TPM_CLEAR_DISABLED          = TPM_RESULT(TPM_BASE + 5).value
TPM_DEACTIVATED             = TPM_RESULT(TPM_BASE + 6).value
TPM_DISABLED                = TPM_RESULT(TPM_BASE + 7).value
TPM_DISABLED_CMD            = TPM_RESULT(TPM_BASE + 8).value
TPM_FAIL                    = TPM_RESULT(TPM_BASE + 9).value
TPM_BAD_ORDINAL             = TPM_RESULT(TPM_BASE + 10).value
TPM_INSTALL_DISABLED        = TPM_RESULT(TPM_BASE + 11).value
TPM_INVALID_KEYHANDLE       = TPM_RESULT(TPM_BASE + 12).value
TPM_KEYNOTFOUND             = TPM_RESULT(TPM_BASE + 13).value
TPM_INAPPROPRIATE_ENC       = TPM_RESULT(TPM_BASE + 14).value
TPM_MIGRATEFAIL             = TPM_RESULT(TPM_BASE + 15).value
TPM_INVALID_PCR_INFO        = TPM_RESULT(TPM_BASE + 16).value
TPM_NOSPACE                 = TPM_RESULT(TPM_BASE + 17).value
TPM_NOSRK                   = TPM_RESULT(TPM_BASE + 18).value
TPM_NOTSEALED_BLOB          = TPM_RESULT(TPM_BASE + 19).value
TPM_OWNER_SET               = TPM_RESULT(TPM_BASE + 20).value
TPM_RESOURCES               = TPM_RESULT(TPM_BASE + 21).value
TPM_SHORTRANDOM             = TPM_RESULT(TPM_BASE + 22).value
TPM_SIZE                    = TPM_RESULT(TPM_BASE + 23).value
TPM_WRONGPCRVAL             = TPM_RESULT(TPM_BASE + 24).value
TPM_BAD_PARAM_SIZE          = TPM_RESULT(TPM_BASE + 25).value
TPM_SHA_THREAD              = TPM_RESULT(TPM_BASE + 26).value
TPM_SHA_ERROR               = TPM_RESULT(TPM_BASE + 27).value
TPM_FAILEDSELFTEST          = TPM_RESULT(TPM_BASE + 28).value
TPM_AUTH2FAIL               = TPM_RESULT(TPM_BASE + 29).value
TPM_BADTAG                  = TPM_RESULT(TPM_BASE + 30).value
TPM_IOERROR                 = TPM_RESULT(TPM_BASE + 31).value
TPM_ENCRYPT_ERROR           = TPM_RESULT(TPM_BASE + 32).value
TPM_DECRYPT_ERROR           = TPM_RESULT(TPM_BASE + 33).value
TPM_INVALID_AUTHHANDLE      = TPM_RESULT(TPM_BASE + 34).value
TPM_NO_ENDORSEMENT          = TPM_RESULT(TPM_BASE + 35).value
TPM_INVALID_KEYUSAGE        = TPM_RESULT(TPM_BASE + 36).value
TPM_WRONG_ENTITYTYPE        = TPM_RESULT(TPM_BASE + 37).value
TPM_INVALID_POSTINIT        = TPM_RESULT(TPM_BASE + 38).value
TPM_INAPPROPRIATE_SIG       = TPM_RESULT(TPM_BASE + 39).value
TPM_BAD_KEY_PROPERTY        = TPM_RESULT(TPM_BASE + 40).value
TPM_BAD_MIGRATION           = TPM_RESULT(TPM_BASE + 41).value
TPM_BAD_SCHEME              = TPM_RESULT(TPM_BASE + 42).value
TPM_BAD_DATASIZE            = TPM_RESULT(TPM_BASE + 43).value
TPM_BAD_MODE                = TPM_RESULT(TPM_BASE + 44).value
TPM_BAD_PRESENCE            = TPM_RESULT(TPM_BASE + 45).value
TPM_BAD_VERSION             = TPM_RESULT(TPM_BASE + 46).value
TPM_NO_WRAP_TRANSPORT       = TPM_RESULT(TPM_BASE + 47).value
TPM_AUDITFAIL_UNSUCCESSFUL  = TPM_RESULT(TPM_BASE + 48).value
TPM_AUDITFAIL_SUCCESSFUL    = TPM_RESULT(TPM_BASE + 49).value
TPM_NOTRESETABLE            = TPM_RESULT(TPM_BASE + 50).value
TPM_NOTLOCAL                = TPM_RESULT(TPM_BASE + 51).value
TPM_BAD_TYPE                = TPM_RESULT(TPM_BASE + 52).value
TPM_INVALID_RESOURCE        = TPM_RESULT(TPM_BASE + 53).value
TPM_NOTFIPS                 = TPM_RESULT(TPM_BASE + 54).value
TPM_INVALID_FAMILY          = TPM_RESULT(TPM_BASE + 55).value
TPM_NO_NV_PERMISSION        = TPM_RESULT(TPM_BASE + 56).value
TPM_REQUIRES_SIGN           = TPM_RESULT(TPM_BASE + 57).value
TPM_KEY_NOTSUPPORTED        = TPM_RESULT(TPM_BASE + 58).value
TPM_AUTH_CONFLICT           = TPM_RESULT(TPM_BASE + 59).value
TPM_AREA_LOCKED             = TPM_RESULT(TPM_BASE + 60).value
TPM_BAD_LOCALITY            = TPM_RESULT(TPM_BASE + 61).value
TPM_READ_ONLY               = TPM_RESULT(TPM_BASE + 62).value
TPM_PER_NOWRITE             = TPM_RESULT(TPM_BASE + 63).value
TPM_FAMILYCOUNT             = TPM_RESULT(TPM_BASE + 64).value
TPM_WRITE_LOCKED            = TPM_RESULT(TPM_BASE + 65).value
TPM_BAD_ATTRIBUTES          = TPM_RESULT(TPM_BASE + 66).value
TPM_INVALID_STRUCTURE       = TPM_RESULT(TPM_BASE + 67).value
TPM_KEY_OWNER_CONTROL       = TPM_RESULT(TPM_BASE + 68).value
TPM_BAD_COUNTER             = TPM_RESULT(TPM_BASE + 69).value
TPM_NOT_FULLWRITE           = TPM_RESULT(TPM_BASE + 70).value
TPM_CONTEXT_GAP             = TPM_RESULT(TPM_BASE + 71).value
TPM_MAXNVWRITES             = TPM_RESULT(TPM_BASE + 72).value
TPM_NOOPERATOR              = TPM_RESULT(TPM_BASE + 73).value
TPM_RESOURCEMISSING         = TPM_RESULT(TPM_BASE + 74).value
TPM_DELEGATE_LOCK           = TPM_RESULT(TPM_BASE + 75).value
TPM_DELEGATE_FAMILY         = TPM_RESULT(TPM_BASE + 76).value
TPM_DELEGATE_ADMIN          = TPM_RESULT(TPM_BASE + 77).value
TPM_TRANSPORT_NOTEXCLUSIVE  = TPM_RESULT(TPM_BASE + 78).value
TPM_OWNER_CONTROL           = TPM_RESULT(TPM_BASE + 79).value
TPM_DAA_RESOURCES           = TPM_RESULT(TPM_BASE + 80).value
TPM_DAA_INPUT_DATA0         = TPM_RESULT(TPM_BASE + 81).value
TPM_DAA_INPUT_DATA1         = TPM_RESULT(TPM_BASE + 82).value
TPM_DAA_ISSUER_SETTINGS     = TPM_RESULT(TPM_BASE + 83).value
TPM_DAA_TPM_SETTINGS        = TPM_RESULT(TPM_BASE + 84).value
TPM_DAA_STAGE               = TPM_RESULT(TPM_BASE + 85).value
TPM_DAA_ISSUER_VALIDITY     = TPM_RESULT(TPM_BASE + 86).value
TPM_DAA_WRONG_W             = TPM_RESULT(TPM_BASE + 87).value
TPM_BAD_HANDLE              = TPM_RESULT(TPM_BASE + 88).value
TPM_BAD_DELEGATE            = TPM_RESULT(TPM_BASE + 89).value
TPM_BADCONTEXT              = TPM_RESULT(TPM_BASE + 90).value
TPM_TOOMANYCONTEXTS         = TPM_RESULT(TPM_BASE + 91).value
TPM_MA_TICKET_SIGNATURE     = TPM_RESULT(TPM_BASE + 92).value
TPM_MA_DESTINATION          = TPM_RESULT(TPM_BASE + 93).value
TPM_MA_SOURCE               = TPM_RESULT(TPM_BASE + 94).value
TPM_MA_AUTHORITY            = TPM_RESULT(TPM_BASE + 95).value
TPM_PERMANENTEK             = TPM_RESULT(TPM_BASE + 97).value
TPM_BAD_SIGNATURE           = TPM_RESULT(TPM_BASE + 98).value
TPM_NOCONTEXTSPACE          = TPM_RESULT(TPM_BASE + 99).value

TPM_RETRY                   = TPM_RESULT(TPM_BASE + TPM_NON_FATAL).value
TPM_NEEDS_SELFTEST          = TPM_RESULT(TPM_BASE + TPM_NON_FATAL + 1).value
TPM_DOING_SELFTEST          = TPM_RESULT(TPM_BASE + TPM_NON_FATAL + 2).value
TPM_DEFEND_LOCK_RUNNING     = TPM_RESULT(TPM_BASE + TPM_NON_FATAL + 3).value

TPM_ORD_ActivateIdentity                  = TPM_COMMAND_CODE(0x0000007A).value
TPM_ORD_AuthorizeMigrationKey             = TPM_COMMAND_CODE(0x0000002B).value
TPM_ORD_CertifyKey                        = TPM_COMMAND_CODE(0x00000032).value
TPM_ORD_CertifyKey2                       = TPM_COMMAND_CODE(0x00000033).value
TPM_ORD_CertifySelfTest                   = TPM_COMMAND_CODE(0x00000052).value
TPM_ORD_ChangeAuth                        = TPM_COMMAND_CODE(0x0000000C).value
TPM_ORD_ChangeAuthAsymFinish              = TPM_COMMAND_CODE(0x0000000F).value
TPM_ORD_ChangeAuthAsymStart               = TPM_COMMAND_CODE(0x0000000E).value
TPM_ORD_ChangeAuthOwner                   = TPM_COMMAND_CODE(0x00000010).value
TPM_ORD_CMK_ApproveMA                     = TPM_COMMAND_CODE(0x0000001D).value
TPM_ORD_CMK_ConvertMigration              = TPM_COMMAND_CODE(0x00000024).value
TPM_ORD_CMK_CreateBlob                    = TPM_COMMAND_CODE(0x0000001B).value
TPM_ORD_CMK_CreateKey                     = TPM_COMMAND_CODE(0x00000013).value
TPM_ORD_CMK_CreateTicket                  = TPM_COMMAND_CODE(0x00000012).value
TPM_ORD_CMK_SetRestrictions               = TPM_COMMAND_CODE(0x0000001C).value
TPM_ORD_ContinueSelfTest                  = TPM_COMMAND_CODE(0x00000053).value
TPM_ORD_ConvertMigrationBlob              = TPM_COMMAND_CODE(0x0000002A).value
TPM_ORD_CreateCounter                     = TPM_COMMAND_CODE(0x000000DC).value
TPM_ORD_CreateEndorsementKeyPair          = TPM_COMMAND_CODE(0x00000078).value
TPM_ORD_CreateMaintenanceArchive          = TPM_COMMAND_CODE(0x0000002C).value
TPM_ORD_CreateMigrationBlob               = TPM_COMMAND_CODE(0x00000028).value
TPM_ORD_CreateRevocableEK                 = TPM_COMMAND_CODE(0x0000007F).value
TPM_ORD_CreateWrapKey                     = TPM_COMMAND_CODE(0x0000001F).value
TPM_ORD_DAA_JOIN                          = TPM_COMMAND_CODE(0x00000029).value
TPM_ORD_DAA_SIGN                          = TPM_COMMAND_CODE(0x00000031).value
TPM_ORD_Delegate_CreateKeyDelegation      = TPM_COMMAND_CODE(0x000000D4).value
TPM_ORD_Delegate_CreateOwnerDelegation    = TPM_COMMAND_CODE(0x000000D5).value
TPM_ORD_Delegate_LoadOwnerDelegation      = TPM_COMMAND_CODE(0x000000D8).value
TPM_ORD_Delegate_Manage                   = TPM_COMMAND_CODE(0x000000D2).value
TPM_ORD_Delegate_ReadTable                = TPM_COMMAND_CODE(0x000000DB).value
TPM_ORD_Delegate_UpdateVerification       = TPM_COMMAND_CODE(0x000000D1).value
TPM_ORD_Delegate_VerifyDelegation         = TPM_COMMAND_CODE(0x000000D6).value
TPM_ORD_DirRead                           = TPM_COMMAND_CODE(0x0000001A).value
TPM_ORD_DirWriteAuth                      = TPM_COMMAND_CODE(0x00000019).value
TPM_ORD_DisableForceClear                 = TPM_COMMAND_CODE(0x0000005E).value
TPM_ORD_DisableOwnerClear                 = TPM_COMMAND_CODE(0x0000005C).value
TPM_ORD_DisablePubekRead                  = TPM_COMMAND_CODE(0x0000007E).value
TPM_ORD_DSAP                              = TPM_COMMAND_CODE(0x00000011).value
TPM_ORD_EstablishTransport                = TPM_COMMAND_CODE(0x000000E6).value
TPM_ORD_EvictKey                          = TPM_COMMAND_CODE(0x00000022).value
TPM_ORD_ExecuteTransport                  = TPM_COMMAND_CODE(0x000000E7).value
TPM_ORD_Extend                            = TPM_COMMAND_CODE(0x00000014).value
TPM_ORD_FieldUpgrade                      = TPM_COMMAND_CODE(0x000000AA).value
TPM_ORD_FlushSpecific                     = TPM_COMMAND_CODE(0x000000BA).value
TPM_ORD_ForceClear                        = TPM_COMMAND_CODE(0x0000005D).value
TPM_ORD_GetAuditDigest                    = TPM_COMMAND_CODE(0x00000085).value
TPM_ORD_GetAuditDigestSigned              = TPM_COMMAND_CODE(0x00000086).value
TPM_ORD_GetAuditEvent                     = TPM_COMMAND_CODE(0x00000082).value
TPM_ORD_GetAuditEventSigned               = TPM_COMMAND_CODE(0x00000083).value
TPM_ORD_GetCapability                     = TPM_COMMAND_CODE(0x00000065).value
TPM_ORD_GetCapabilityOwner                = TPM_COMMAND_CODE(0x00000066).value
TPM_ORD_GetCapabilitySigned               = TPM_COMMAND_CODE(0x00000064).value
TPM_ORD_GetOrdinalAuditStatus             = TPM_COMMAND_CODE(0x0000008C).value
TPM_ORD_GetPubKey                         = TPM_COMMAND_CODE(0x00000021).value
TPM_ORD_GetRandom                         = TPM_COMMAND_CODE(0x00000046).value
TPM_ORD_GetTestResult                     = TPM_COMMAND_CODE(0x00000054).value
TPM_ORD_GetTicks                          = TPM_COMMAND_CODE(0x000000F1).value
TPM_ORD_IncrementCounter                  = TPM_COMMAND_CODE(0x000000DD).value
TPM_ORD_Init                              = TPM_COMMAND_CODE(0x00000097).value
TPM_ORD_KeyControlOwner                   = TPM_COMMAND_CODE(0x00000023).value
TPM_ORD_KillMaintenanceFeature            = TPM_COMMAND_CODE(0x0000002E).value
TPM_ORD_LoadAuthContext                   = TPM_COMMAND_CODE(0x000000B7).value
TPM_ORD_LoadContext                       = TPM_COMMAND_CODE(0x000000B9).value
TPM_ORD_LoadKey                           = TPM_COMMAND_CODE(0x00000020).value
TPM_ORD_LoadKey2                          = TPM_COMMAND_CODE(0x00000041).value
TPM_ORD_LoadKeyContext                    = TPM_COMMAND_CODE(0x000000B5).value
TPM_ORD_LoadMaintenanceArchive            = TPM_COMMAND_CODE(0x0000002D).value
TPM_ORD_LoadManuMaintPub                  = TPM_COMMAND_CODE(0x0000002F).value
TPM_ORD_MakeIdentity                      = TPM_COMMAND_CODE(0x00000079).value
TPM_ORD_MigrateKey                        = TPM_COMMAND_CODE(0x00000025).value
TPM_ORD_NV_DefineSpace                    = TPM_COMMAND_CODE(0x000000CC).value
TPM_ORD_NV_ReadValue                      = TPM_COMMAND_CODE(0x000000CF).value
TPM_ORD_NV_ReadValueAuth                  = TPM_COMMAND_CODE(0x000000D0).value
TPM_ORD_NV_WriteValue                     = TPM_COMMAND_CODE(0x000000CD).value
TPM_ORD_NV_WriteValueAuth                 = TPM_COMMAND_CODE(0x000000CE).value
TPM_ORD_OIAP                              = TPM_COMMAND_CODE(0x0000000A).value
TPM_ORD_OSAP                              = TPM_COMMAND_CODE(0x0000000B).value
TPM_ORD_OwnerClear                        = TPM_COMMAND_CODE(0x0000005B).value
TPM_ORD_OwnerReadInternalPub              = TPM_COMMAND_CODE(0x00000081).value
TPM_ORD_OwnerReadPubek                    = TPM_COMMAND_CODE(0x0000007D).value
TPM_ORD_OwnerSetDisable                   = TPM_COMMAND_CODE(0x0000006E).value
TPM_ORD_PCR_Reset                         = TPM_COMMAND_CODE(0x000000C8).value
TPM_ORD_PcrRead                           = TPM_COMMAND_CODE(0x00000015).value
TPM_ORD_PhysicalDisable                   = TPM_COMMAND_CODE(0x00000070).value
TPM_ORD_PhysicalEnable                    = TPM_COMMAND_CODE(0x0000006F).value
TPM_ORD_PhysicalSetDeactivated            = TPM_COMMAND_CODE(0x00000072).value
TPM_ORD_Quote                             = TPM_COMMAND_CODE(0x00000016).value
TPM_ORD_Quote2                            = TPM_COMMAND_CODE(0x0000003E).value
TPM_ORD_ReadCounter                       = TPM_COMMAND_CODE(0x000000DE).value
TPM_ORD_ReadManuMaintPub                  = TPM_COMMAND_CODE(0x00000030).value
TPM_ORD_ReadPubek                         = TPM_COMMAND_CODE(0x0000007C).value
TPM_ORD_ReleaseCounter                    = TPM_COMMAND_CODE(0x000000DF).value
TPM_ORD_ReleaseCounterOwner               = TPM_COMMAND_CODE(0x000000E0).value
TPM_ORD_ReleaseTransportSigned            = TPM_COMMAND_CODE(0x000000E8).value
TPM_ORD_Reset                             = TPM_COMMAND_CODE(0x0000005A).value
TPM_ORD_ResetLockValue                    = TPM_COMMAND_CODE(0x00000040).value
TPM_ORD_RevokeTrust                       = TPM_COMMAND_CODE(0x00000080).value
TPM_ORD_SaveAuthContext                   = TPM_COMMAND_CODE(0x000000B6).value
TPM_ORD_SaveContext                       = TPM_COMMAND_CODE(0x000000B8).value
TPM_ORD_SaveKeyContext                    = TPM_COMMAND_CODE(0x000000B4).value
TPM_ORD_SaveState                         = TPM_COMMAND_CODE(0x00000098).value
TPM_ORD_Seal                              = TPM_COMMAND_CODE(0x00000017).value
TPM_ORD_Sealx                             = TPM_COMMAND_CODE(0x0000003D).value
TPM_ORD_SelfTestFull                      = TPM_COMMAND_CODE(0x00000050).value
TPM_ORD_SetCapability                     = TPM_COMMAND_CODE(0x0000003F).value
TPM_ORD_SetOperatorAuth                   = TPM_COMMAND_CODE(0x00000074).value
TPM_ORD_SetOrdinalAuditStatus             = TPM_COMMAND_CODE(0x0000008D).value
TPM_ORD_SetOwnerInstall                   = TPM_COMMAND_CODE(0x00000071).value
TPM_ORD_SetOwnerPointer                   = TPM_COMMAND_CODE(0x00000075).value
TPM_ORD_SetRedirection                    = TPM_COMMAND_CODE(0x0000009A).value
TPM_ORD_SetTempDeactivated                = TPM_COMMAND_CODE(0x00000073).value
TPM_ORD_SHA1Complete                      = TPM_COMMAND_CODE(0x000000A2).value
TPM_ORD_SHA1CompleteExtend                = TPM_COMMAND_CODE(0x000000A3).value
TPM_ORD_SHA1Start                         = TPM_COMMAND_CODE(0x000000A0).value
TPM_ORD_SHA1Update                        = TPM_COMMAND_CODE(0x000000A1).value
TPM_ORD_Sign                              = TPM_COMMAND_CODE(0x0000003C).value
TPM_ORD_Startup                           = TPM_COMMAND_CODE(0x00000099).value
TPM_ORD_StirRandom                        = TPM_COMMAND_CODE(0x00000047).value
TPM_ORD_TakeOwnership                     = TPM_COMMAND_CODE(0x0000000D).value
TPM_ORD_Terminate_Handle                  = TPM_COMMAND_CODE(0x00000096).value
TPM_ORD_TickStampBlob                     = TPM_COMMAND_CODE(0x000000F2).value
TPM_ORD_UnBind                            = TPM_COMMAND_CODE(0x0000001E).value
TPM_ORD_Unseal                            = TPM_COMMAND_CODE(0x00000018).value
TSC_ORD_PhysicalPresence                  = TPM_COMMAND_CODE(0x4000000A).value
TSC_ORD_ResetEstablishmentBit             = TPM_COMMAND_CODE(0x4000000B).value

class TPM_CONTEXT_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("handle",          TPM_HANDLE),
    ("label",           UINT8 * 16),
    ("contextCount",    UINT32),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

class TPM_CONTEXT_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("contextNonce",  TPM_NONCE),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

TPM_NV_INDEX_LOCK              = UINT32(0xffffffff).value
TPM_NV_INDEX0                  = UINT32(0x00000000).value
TPM_NV_INDEX_DIR               = UINT32(0x10000001).value
TPM_NV_INDEX_EKCert            = UINT32(0x0000f000).value
TPM_NV_INDEX_TPM_CC            = UINT32(0x0000f001).value
TPM_NV_INDEX_PlatformCert      = UINT32(0x0000f002).value
TPM_NV_INDEX_Platform_CC       = UINT32(0x0000f003).value

TPM_NV_INDEX_TSS_BASE          = UINT32(0x00011100).value
TPM_NV_INDEX_PC_BASE           = UINT32(0x00011200).value
TPM_NV_INDEX_SERVER_BASE       = UINT32(0x00011300).value
TPM_NV_INDEX_MOBILE_BASE       = UINT32(0x00011400).value
TPM_NV_INDEX_PERIPHERAL_BASE   = UINT32(0x00011500).value
TPM_NV_INDEX_GROUP_RESV_BASE   = UINT32(0x00010000).value

class TPM_NV_ATTRIBUTES (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("attributes",  UINT32)
  ]

TPM_NV_PER_READ_STCLEAR        = (BIT31)
TPM_NV_PER_AUTHREAD            = (BIT18)
TPM_NV_PER_OWNERREAD           = (BIT17)
TPM_NV_PER_PPREAD              = (BIT16)
TPM_NV_PER_GLOBALLOCK          = (BIT15)
TPM_NV_PER_WRITE_STCLEAR       = (BIT14)
TPM_NV_PER_WRITEDEFINE         = (BIT13)
TPM_NV_PER_WRITEALL            = (BIT12)
TPM_NV_PER_AUTHWRITE           = (BIT2)
TPM_NV_PER_OWNERWRITE          = (BIT1)
TPM_NV_PER_PPWRITE             = (BIT0)

class TPM_NV_DATA_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("nvIndex",       TPM_NV_INDEX),
    ("pcrInfoRead",   TPM_PCR_INFO_SHORT),
    ("pcrInfoWrite",  TPM_PCR_INFO_SHORT),
    ("permission",    TPM_NV_ATTRIBUTES),
    ("bReadSTClear",  BOOLEAN),
    ("bWriteSTClear", BOOLEAN),
    ("bWriteDefine",  BOOLEAN),
    ("dataSize",      UINT32)
  ]

TPM_DEL_OWNER_BITS          = UINT32(0x00000001).value
TPM_DEL_KEY_BITS            = UINT32(0x00000002).value

class TPM_DELEGATIONS (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("delegateType",  UINT32),
    ("per1",          UINT32),
    ("per2",          UINT32)
  ]

TPM_DELEGATE_SetOrdinalAuditStatus          = BIT30
TPM_DELEGATE_DirWriteAuth                   = BIT29
TPM_DELEGATE_CMK_ApproveMA                  = BIT28
TPM_DELEGATE_NV_WriteValue                  = BIT27
TPM_DELEGATE_CMK_CreateTicket               = BIT26
TPM_DELEGATE_NV_ReadValue                   = BIT25
TPM_DELEGATE_Delegate_LoadOwnerDelegation   = BIT24
TPM_DELEGATE_DAA_Join                       = BIT23
TPM_DELEGATE_AuthorizeMigrationKey          = BIT22
TPM_DELEGATE_CreateMaintenanceArchive       = BIT21
TPM_DELEGATE_LoadMaintenanceArchive         = BIT20
TPM_DELEGATE_KillMaintenanceFeature         = BIT19
TPM_DELEGATE_OwnerReadInteralPub            = BIT18
TPM_DELEGATE_ResetLockValue                 = BIT17
TPM_DELEGATE_OwnerClear                     = BIT16
TPM_DELEGATE_DisableOwnerClear              = BIT15
TPM_DELEGATE_NV_DefineSpace                 = BIT14
TPM_DELEGATE_OwnerSetDisable                = BIT13
TPM_DELEGATE_SetCapability                  = BIT12
TPM_DELEGATE_MakeIdentity                   = BIT11
TPM_DELEGATE_ActivateIdentity               = BIT10
TPM_DELEGATE_OwnerReadPubek                 = BIT9
TPM_DELEGATE_DisablePubekRead               = BIT8
TPM_DELEGATE_SetRedirection                 = BIT7
TPM_DELEGATE_FieldUpgrade                   = BIT6
TPM_DELEGATE_Delegate_UpdateVerification    = BIT5
TPM_DELEGATE_CreateCounter                  = BIT4
TPM_DELEGATE_ReleaseCounterOwner            = BIT3
TPM_DELEGATE_DelegateManage                 = BIT2
TPM_DELEGATE_Delegate_CreateOwnerDelegation = BIT1
TPM_DELEGATE_DAA_Sign                       = BIT0

TPM_KEY_DELEGATE_CMK_ConvertMigration       = BIT28
TPM_KEY_DELEGATE_TickStampBlob              = BIT27
TPM_KEY_DELEGATE_ChangeAuthAsymStart        = BIT26
TPM_KEY_DELEGATE_ChangeAuthAsymFinish       = BIT25
TPM_KEY_DELEGATE_CMK_CreateKey              = BIT24
TPM_KEY_DELEGATE_MigrateKey                 = BIT23
TPM_KEY_DELEGATE_LoadKey2                   = BIT22
TPM_KEY_DELEGATE_EstablishTransport         = BIT21
TPM_KEY_DELEGATE_ReleaseTransportSigned     = BIT20
TPM_KEY_DELEGATE_Quote2                     = BIT19
TPM_KEY_DELEGATE_Sealx                      = BIT18
TPM_KEY_DELEGATE_MakeIdentity               = BIT17
TPM_KEY_DELEGATE_ActivateIdentity           = BIT16
TPM_KEY_DELEGATE_GetAuditDigestSigned       = BIT15
TPM_KEY_DELEGATE_Sign                       = BIT14
TPM_KEY_DELEGATE_CertifyKey2                = BIT13
TPM_KEY_DELEGATE_CertifyKey                 = BIT12
TPM_KEY_DELEGATE_CreateWrapKey              = BIT11
TPM_KEY_DELEGATE_CMK_CreateBlob             = BIT10
TPM_KEY_DELEGATE_CreateMigrationBlob        = BIT9
TPM_KEY_DELEGATE_ConvertMigrationBlob       = BIT8
TPM_KEY_DELEGATE_CreateKeyDelegation        = BIT7
TPM_KEY_DELEGATE_ChangeAuth                 = BIT6
TPM_KEY_DELEGATE_GetPubKey                  = BIT5
TPM_KEY_DELEGATE_UnBind                     = BIT4
TPM_KEY_DELEGATE_Quote                      = BIT3
TPM_KEY_DELEGATE_Unseal                     = BIT2
TPM_KEY_DELEGATE_Seal                       = BIT1
TPM_KEY_DELEGATE_LoadKey                    = BIT0

TPM_DELEGATE_ADMIN_LOCK           = BIT1
TPM_FAMFLAG_ENABLE                = BIT0

class TPM_FAMILY_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

class TPM_FAMILY_TABLE_ENTRY (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_FAMILY_LABEL),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
    ("flags",             TPM_FAMILY_FLAGS)
  ]

TPM_NUM_FAMILY_TABLE_ENTRY_MIN = 8

class TPM_FAMILY_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("flfamTableRowags",  TPM_FAMILY_TABLE_ENTRY * TPM_NUM_FAMILY_TABLE_ENTRY_MIN)
  ]

class TPM_DELEGATE_LABEL (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("label", UINT8)
  ]

class TPM_DELEGATE_PUBLIC (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("label",             TPM_DELEGATE_LABEL),
    ("pcrInfo",           TPM_PCR_INFO_SHORT),
    ("permissions",       TPM_DELEGATIONS),
    ("familyID",          TPM_FAMILY_ID),
    ("verificationCount", TPM_FAMILY_VERIFICATION),
  ]

class TPM_DELEGATE_TABLE_ROW (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("pub",       TPM_DELEGATE_PUBLIC),
    ("authValue", TPM_SECRET)
  ]

TPM_NUM_DELEGATE_TABLE_ENTRY_MIN = 2
class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("delRow", TPM_DELEGATE_TABLE_ROW * TPM_NUM_DELEGATE_TABLE_ENTRY_MIN)
  ]

class TPM_DELEGATE_TABLE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("authValue", TPM_SECRET)
  ]

class TPM_DELEGATE_OWNER_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

class TPM_DELEGATE_KEY_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("pub",             TPM_DELEGATE_PUBLIC),
    ("integrityDigest", TPM_DIGEST),
    ("pubKeyDigest",    TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalArea",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveArea",   POINTER (UINT8))
  ]

TPM_FAMILY_CREATE                 = UINT32(0x00000001).value
TPM_FAMILY_ENABLE                 = UINT32(0x00000002).value
TPM_FAMILY_ADMIN                  = UINT32(0x00000003).value
TPM_FAMILY_INVALIDATE             = UINT32(0x00000004).value

TPM_CAP_ORD                     = TPM_CAPABILITY_AREA(0x00000001).value
TPM_CAP_ALG                     = TPM_CAPABILITY_AREA(0x00000002).value
TPM_CAP_PID                     = TPM_CAPABILITY_AREA(0x00000003).value
TPM_CAP_FLAG                    = TPM_CAPABILITY_AREA(0x00000004).value
TPM_CAP_PROPERTY                = TPM_CAPABILITY_AREA(0x00000005).value
TPM_CAP_VERSION                 = TPM_CAPABILITY_AREA(0x00000006).value
TPM_CAP_KEY_HANDLE              = TPM_CAPABILITY_AREA(0x00000007).value
TPM_CAP_CHECK_LOADED            = TPM_CAPABILITY_AREA(0x00000008).value
TPM_CAP_SYM_MODE                = TPM_CAPABILITY_AREA(0x00000009).value
TPM_CAP_KEY_STATUS              = TPM_CAPABILITY_AREA(0x0000000C).value
TPM_CAP_NV_LIST                 = TPM_CAPABILITY_AREA(0x0000000D).value
TPM_CAP_MFR                     = TPM_CAPABILITY_AREA(0x00000010).value
TPM_CAP_NV_INDEX                = TPM_CAPABILITY_AREA(0x00000011).value
TPM_CAP_TRANS_ALG               = TPM_CAPABILITY_AREA(0x00000012).value
TPM_CAP_HANDLE                  = TPM_CAPABILITY_AREA(0x00000014).value
TPM_CAP_TRANS_ES                = TPM_CAPABILITY_AREA(0x00000015).value
TPM_CAP_AUTH_ENCRYPT            = TPM_CAPABILITY_AREA(0x00000017).value
TPM_CAP_SELECT_SIZE             = TPM_CAPABILITY_AREA(0x00000018).value
TPM_CAP_VERSION_VAL             = TPM_CAPABILITY_AREA(0x0000001A).value

TPM_CAP_FLAG_PERMANENT          = TPM_CAPABILITY_AREA(0x00000108).value
TPM_CAP_FLAG_VOLATILE           = TPM_CAPABILITY_AREA(0x00000109).value

TPM_CAP_PROP_PCR                = TPM_CAPABILITY_AREA(0x00000101).value
TPM_CAP_PROP_DIR                = TPM_CAPABILITY_AREA(0x00000102).value
TPM_CAP_PROP_MANUFACTURER       = TPM_CAPABILITY_AREA(0x00000103).value
TPM_CAP_PROP_KEYS               = TPM_CAPABILITY_AREA(0x00000104).value
TPM_CAP_PROP_MIN_COUNTER        = TPM_CAPABILITY_AREA(0x00000107).value
TPM_CAP_PROP_AUTHSESS           = TPM_CAPABILITY_AREA(0x0000010A).value
TPM_CAP_PROP_TRANSESS           = TPM_CAPABILITY_AREA(0x0000010B).value
TPM_CAP_PROP_COUNTERS           = TPM_CAPABILITY_AREA(0x0000010C).value
TPM_CAP_PROP_MAX_AUTHSESS       = TPM_CAPABILITY_AREA(0x0000010D).value
TPM_CAP_PROP_MAX_TRANSESS       = TPM_CAPABILITY_AREA(0x0000010E).value
TPM_CAP_PROP_MAX_COUNTERS       = TPM_CAPABILITY_AREA(0x0000010F).value
TPM_CAP_PROP_MAX_KEYS           = TPM_CAPABILITY_AREA(0x00000110).value
TPM_CAP_PROP_OWNER              = TPM_CAPABILITY_AREA(0x00000111).value
TPM_CAP_PROP_CONTEXT            = TPM_CAPABILITY_AREA(0x00000112).value
TPM_CAP_PROP_MAX_CONTEXT        = TPM_CAPABILITY_AREA(0x00000113).value
TPM_CAP_PROP_FAMILYROWS         = TPM_CAPABILITY_AREA(0x00000114).value
TPM_CAP_PROP_TIS_TIMEOUT        = TPM_CAPABILITY_AREA(0x00000115).value
TPM_CAP_PROP_STARTUP_EFFECT     = TPM_CAPABILITY_AREA(0x00000116).value
TPM_CAP_PROP_DELEGATE_ROW       = TPM_CAPABILITY_AREA(0x00000117).value
TPM_CAP_PROP_DAA_MAX            = TPM_CAPABILITY_AREA(0x00000119).value
CAP_PROP_SESSION_DAA            = TPM_CAPABILITY_AREA(0x0000011A).value
TPM_CAP_PROP_CONTEXT_DIST       = TPM_CAPABILITY_AREA(0x0000011B).value
TPM_CAP_PROP_DAA_INTERRUPT      = TPM_CAPABILITY_AREA(0x0000011C).value
TPM_CAP_PROP_SESSIONS           = TPM_CAPABILITY_AREA(0x0000011D).value
TPM_CAP_PROP_MAX_SESSIONS       = TPM_CAPABILITY_AREA(0x0000011E).value
TPM_CAP_PROP_CMK_RESTRICTION    = TPM_CAPABILITY_AREA(0x0000011F).value
TPM_CAP_PROP_DURATION           = TPM_CAPABILITY_AREA(0x00000120).value
TPM_CAP_PROP_ACTIVE_COUNTER     = TPM_CAPABILITY_AREA(0x00000122).value
TPM_CAP_PROP_MAX_NV_AVAILABLE   = TPM_CAPABILITY_AREA(0x00000123).value
TPM_CAP_PROP_INPUT_BUFFER       = TPM_CAPABILITY_AREA(0x00000124).value

TPM_SET_PERM_FLAGS              = TPM_CAPABILITY_AREA(0x00000001).value
TPM_SET_PERM_DATA               = TPM_CAPABILITY_AREA(0x00000002).value
TPM_SET_STCLEAR_FLAGS           = TPM_CAPABILITY_AREA(0x00000003).value
TPM_SET_STCLEAR_DATA            = TPM_CAPABILITY_AREA(0x00000004).value
TPM_SET_STANY_FLAGS             = TPM_CAPABILITY_AREA(0x00000005).value
TPM_SET_STANY_DATA              = TPM_CAPABILITY_AREA(0x00000006).value

class TPM_CAP_VERSION_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",                 TPM_STRUCTURE_TAG),
    ("version",             TPM_VERSION),
    ("specLevel",           UINT16),
    ("errataRev",           UINT8),
    ("tpmVendorID",         UINT8 * 4),
    ("vendorSpecificSize",  UINT16),
    ("vendorSpecific",      POINTER (UINT8))
  ]

class TPM_DA_ACTION_TYPE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",     TPM_STRUCTURE_TAG),
    ("actions", UINT32)
  ]

TPM_DA_ACTION_FAILURE_MODE     = UINT32(1).value << 3
TPM_DA_ACTION_DEACTIVATE       = UINT32(1).value << 2
TPM_DA_ACTION_DISABLE          = UINT32(1).value << 1
TPM_DA_ACTION_TIMEOUT          = UINT32(1).value << 0

class TPM_DA_INFO (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("currentCount",      UINT16),
    ("thresholdCount",    UINT16),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("actionDependValue", UINT32),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

class TPM_DA_INFO_LIMITED (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("state",             TPM_DA_STATE),
    ("actionAtThreshold", TPM_DA_ACTION_TYPE),
    ("vendorDataSize",    UINT32),
    ("vendorData",        POINTER (UINT8))
  ]

TPM_DA_STATE_INACTIVE          = UINT8(0x00).value
TPM_DA_STATE_ACTIVE            = UINT8(0x01).value

TPM_DAA_SIZE_r0                = 43
TPM_DAA_SIZE_r1                = 43
TPM_DAA_SIZE_r2                = 128
TPM_DAA_SIZE_r3                = 168
TPM_DAA_SIZE_r4                = 219
TPM_DAA_SIZE_NT                = 20
TPM_DAA_SIZE_v0                = 128
TPM_DAA_SIZE_v1                = 192
TPM_DAA_SIZE_NE                = 256
TPM_DAA_SIZE_w                 = 256
TPM_DAA_SIZE_issuerModulus     = 256

TPM_DAA_power0                 = 104
TPM_DAA_power1                 = 1024

class TPM_DAA_ISSUER (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digest_R0",     TPM_DIGEST),
    ("DAA_digest_R1",     TPM_DIGEST),
    ("DAA_digest_S0",     TPM_DIGEST),
    ("DAA_digest_S1",     TPM_DIGEST),
    ("DAA_digest_n",      TPM_DIGEST),
    ("DAA_digest_gamma",  TPM_DIGEST),
    ("DAA_generic_q",     UINT8 * 26)
  ]

class TPM_DAA_TPM (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestIssuer",  TPM_DIGEST),
    ("DAA_digest_v0",     TPM_DIGEST),
    ("DAA_digest_v1",     TPM_DIGEST),
    ("DAA_rekey",         TPM_DIGEST),
    ("DAA_count",         UINT32)
  ]

class TPM_DAA_CONTEXT (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",               TPM_STRUCTURE_TAG),
    ("DAA_digestContext", TPM_DIGEST),
    ("DAA_digest",        TPM_DIGEST),
    ("DAA_contextSeed",   TPM_DAA_CONTEXT_SEED),
    ("DAA_scratch",       UINT8 * 256),
    ("DAA_stage",         UINT8)
  ]

class TPM_DAA_JOINDATA (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("DAA_join_u0",   UINT8 * 128),
    ("DAA_join_u1",   UINT8 * 138),
    ("DAA_digest_n0", TPM_DIGEST)
  ]

class TPM_DAA_BLOB (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",             TPM_STRUCTURE_TAG),
    ("resourceType",    TPM_RESOURCE_TYPE),
    ("label",           UINT8 * 16),
    ("blobIntegrity",   TPM_DIGEST),
    ("additionalSize",  UINT32),
    ("additionalData",  POINTER (UINT8)),
    ("sensitiveSize",   UINT32),
    ("sensitiveData",   POINTER (UINT8))
  ]

class TPM_DAA_SENSITIVE (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",           TPM_STRUCTURE_TAG),
    ("internalSize",  UINT32),
    ("internalData",  POINTER (UINT8))
  ]

TPM_REDIR_GPIO              = 0x00000001

class TPM_RQU_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",       TPM_STRUCTURE_TAG),
    ("paramSize", UINT32),
    ("ordinal",   TPM_COMMAND_CODE)
  ]

class TPM_RSP_COMMAND_HDR (EFIPY_INDUSTRY_STRUCTURE):
  _fields_ = [
    ("tag",         TPM_STRUCTURE_TAG),
    ("paramSize",   UINT32),
    ("returnCode",  TPM_RESULT)
  ]

