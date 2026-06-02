# CrowdStrike Falcon Sensor Events

**Total Events:** 931

---

## Table of Contents

- [AcUninstallConfirmation](#acuninstallconfirmation)
- [AcUnloadConfirmation](#acunloadconfirmation)
- [HostInfo](#hostinfo)
- [HookedDriverObject](#hookeddriverobject)
- [WfpFilterTamperingFilterDeleted](#wfpfiltertamperingfilterdeleted)
- [WfpFilterTamperingFilterAdded](#wfpfiltertamperingfilteradded)
- [DeliverLocalFXToCloud](#deliverlocalfxtocloud)
- [UserLogoff](#userlogoff)
- [NeighborListIP4](#neighborlistip4)
- [NeighborListIP6](#neighborlistip6)
- [LocalIpAddressRemovedIP4](#localipaddressremovedip4)
- [LocalIpAddressRemovedIP6](#localipaddressremovedip6)
- [DcUsbEndpointDescriptor](#dcusbendpointdescriptor)
- [DcUsbHIDDescriptor](#dcusbhiddescriptor)
- [DcStatus](#dcstatus)
- [DcUsbConfigurationDescriptor](#dcusbconfigurationdescriptor)
- [DcUsbInterfaceDescriptor](#dcusbinterfacedescriptor)
- [DcUsbDeviceDisconnected](#dcusbdevicedisconnected)
- [DcOnline](#dconline)
- [DcOffline](#dcoffline)
- [DcUsbDeviceWhitelisted](#dcusbdevicewhitelisted)
- [AwsIamAccountAlias](#awsiamaccountalias)
- [FirmwareAnalysisStatus](#firmwareanalysisstatus)
- [FirmwareRegionMeasured](#firmwareregionmeasured)
- [FirmwareAnalysisErrorEvent](#firmwareanalysiserrorevent)
- [FirmwareAnalysisHardwareData](#firmwareanalysishardwaredata)
- [AwsEc2NetworkInterface](#awsec2networkinterface)
- [AwsEc2NetworkInterfacePrivateIP](#awsec2networkinterfaceprivateip)
- [AwsEc2Volume](#awsec2volume)
- [AwsEc2Instance](#awsec2instance)
- [AwsEc2SecurityGroup](#awsec2securitygroup)
- [AwsEc2Subnet](#awsec2subnet)
- [AwsEc2Image](#awsec2image)
- [AwsEc2SecurityGroupRule](#awsec2securitygrouprule)
- [AwsEc2NetworkAcl](#awsec2networkacl)
- [AwsEc2NetworkAclEntry](#awsec2networkaclentry)
- [GroupIdentity](#groupidentity)
- [IOServiceRegister](#ioserviceregister)
- [LocalIpAddressIP4](#localipaddressip4)
- [LocalIpAddressIP6](#localipaddressip6)
- [HostnameChanged](#hostnamechanged)
- [OsVersionInfo](#osversioninfo)
- [APKMetadata](#apkmetadata)
- [MobileAppsManifest](#mobileappsmanifest)
- [UncontainerizeAppResponse](#uncontainerizeappresponse)
- [WiFiConnect](#wificonnect)
- [WiFiDisconnect](#wifidisconnect)
- [MobilePowerStats](#mobilepowerstats)
- [ContainerizationUpdate](#containerizationupdate)
- [FileInfo](#fileinfo)
- [ClipboardCopy](#clipboardcopy)
- [InstalledApplication](#installedapplication)
- [SmbClientShareOpenedEtw](#smbclientshareopenedetw)
- [SmbClientShareClosedEtw](#smbclientshareclosedetw)
- [SmbServerV1AuditEtw](#smbserverv1auditetw)
- [DeactivateMobileSensorResponse](#deactivatemobilesensorresponse)
- [AccessoryConnected](#accessoryconnected)
- [AccessoryDisconnected](#accessorydisconnected)
- [BillingInfo](#billinginfo)
- [EtwErrorEvent](#etwerrorevent)
- [OciContainerTelemetry](#ocicontainertelemetry)
- [OciContainerStarted](#ocicontainerstarted)
- [OciImageHeartbeat](#ociimageheartbeat)
- [OciContainerHeartbeat](#ocicontainerheartbeat)
- [OciContainerStopped](#ocicontainerstopped)
- [AuditCveKmEtw](#auditcvekmetw)
- [CsUmProcessCrashAuxiliaryEvent](#csumprocesscrashauxiliaryevent)
- [FsVolumeMounted](#fsvolumemounted)
- [OciContainerEngineInfo](#ocicontainerengineinfo)
- [AuditCveUmEtw](#auditcveumetw)
- [SystemCapacity](#systemcapacity)
- [AndroidManifestXmlUploaded](#androidmanifestxmluploaded)
- [AndroidManifestFragmentData](#androidmanifestfragmentdata)
- [FileVaultStatus](#filevaultstatus)
- [AmsiRegistrationStatus](#amsiregistrationstatus)
- [PtActivationStatus](#ptactivationstatus)
- [ProvisioningStarted](#provisioningstarted)
- [ProvisioningStatusUpdate](#provisioningstatusupdate)
- [ProvisioningEnded](#provisioningended)
- [K8SCluster](#k8scluster)
- [SpotlightEntityBatchHeader](#spotlightentitybatchheader)
- [RemovableMediaVolumeMounted](#removablemediavolumemounted)
- [FsVolumeUnmounted](#fsvolumeunmounted)
- [RemovableMediaVolumeUnmounted](#removablemediavolumeunmounted)
- [RemovableMediaFileWritten](#removablemediafilewritten)
- [ActiveDirectoryAccountNameUpdate](#activedirectoryaccountnameupdate)
- [ActiveDirectoryAccountOuUpdate](#activedirectoryaccountouupdate)
- [ActiveDirectoryAccountDisabled](#activedirectoryaccountdisabled)
- [ActiveDirectoryAccountLocked](#activedirectoryaccountlocked)
- [ActiveDirectoryAccountUnlocked](#activedirectoryaccountunlocked)
- [ActiveDirectoryAccountCreated](#activedirectoryaccountcreated)
- [ActiveDirectoryAccountPasswordUpdate](#activedirectoryaccountpasswordupdate)
- [ActiveDirectoryAccountEnabled](#activedirectoryaccountenabled)
- [StaticAnalysisContainerTelemetry](#staticanalysiscontainertelemetry)
- [UserInformationEtw](#userinformationetw)
- [TcgPcrInfo](#tcgpcrinfo)
- [DcBluetoothDeviceDisconnected](#dcbluetoothdevicedisconnected)
- [DiskUtilization](#diskutilization)
- [DcBluetoothDeviceConnected](#dcbluetoothdeviceconnected)
- [CidMigrationConfirmation](#cidmigrationconfirmation)
- [CidMigrationComplete](#cidmigrationcomplete)
- [DriverPreventionStatus](#driverpreventionstatus)
- [SensorGroupingTagsUpdate](#sensorgroupingtagsupdate)
- [SysConfigInfo](#sysconfiginfo)
- [IdpPolicyAccountEventRuleMatch](#idppolicyaccounteventrulematch)
- [UserLogon](#userlogon)
- [SensorAntiTamperState](#sensorantitamperstate)
- [UserLogonFailed2](#userlogonfailed2)
- [ServicesStatusInfo](#servicesstatusinfo)
- [OdsCancelRequestReceived](#odscancelrequestreceived)
- [OdsScheduleCancelRequestReceived](#odsschedulecancelrequestreceived)
- [OdsScheduleRequestReceived](#odsschedulerequestreceived)
- [OdsStarted](#odsstarted)
- [OdsProfileReceived](#odsprofilereceived)
- [OdsStartRequestReceived](#odsstartrequestreceived)
- [OdsMaliciousFileFound](#odsmaliciousfilefound)
- [OdsActionStatus](#odsactionstatus)
- [ChannelActive](#channelactive)
- [OdsScheduleCanceled](#odsschedulecanceled)
- [OdsStatus](#odsstatus)
- [DcIdentification](#dcidentification)
- [K8SClusterInfo](#k8sclusterinfo)
- [AgentOnline](#agentonline)
- [SensorHeartbeat](#sensorheartbeat)
- [LocalWindowsUserUpdate](#localwindowsuserupdate)
- [SmbClientShareLogonBruteForceSuspected](#smbclientsharelogonbruteforcesuspected)
- [CsKmCrashSummaryEvent](#cskmcrashsummaryevent)
- [LockdownModeStatus](#lockdownmodestatus)
- [IdpContainerRestarted](#idpcontainerrestarted)
- [AsepValueUpdate](#asepvalueupdate)
- [RansomwareRenameFile](#ransomwarerenamefile)
- [AsepKeyUpdate](#asepkeyupdate)
- [ProcessRollup](#processrollup)
- [PeVersionInfo](#peversioninfo)
- [KernelModeLoadImage](#kernelmodeloadimage)
- [IoSessionConnected](#iosessionconnected)
- [IoSessionLoggedOn](#iosessionloggedon)
- [CreateService](#createservice)
- [ModifyServiceBinary](#modifyservicebinary)
- [UACCredentialCaptureElevation](#uaccredentialcaptureelevation)
- [UACCOMElevation](#uaccomelevation)
- [UACMSIElevation](#uacmsielevation)
- [WroteExeAndGeneratedServiceEvent](#wroteexeandgeneratedserviceevent)
- [UACAxisElevation](#uacaxiselevation)
- [DllInjection](#dllinjection)
- [UnsignedModuleLoad](#unsignedmoduleload)
- [SuspiciousRawDiskRead](#suspiciousrawdiskread)
- [HostedServiceStopped](#hostedservicestopped)
- [WmiCreateProcess](#wmicreateprocess)
- [ExecutableDeleted](#executabledeleted)
- [NewExecutableRenamed](#newexecutablerenamed)
- [SuspiciousDnsRequest](#suspiciousdnsrequest)
- [ProcessSelfDeleted](#processselfdeleted)
- [FlashThreadCreateProcess](#flashthreadcreateprocess)
- [EndOfProcess](#endofprocess)
- [CommandHistory](#commandhistory)
- [BehaviorWhitelisted](#behaviorwhitelisted)
- [UserLogonFailed](#userlogonfailed)
- [FalconHostRegTamperingInfo](#falconhostregtamperinginfo)
- [FalconHostFileTamperingInfo](#falconhostfiletamperinginfo)
- [ScriptControlErrorEvent](#scriptcontrolerrorevent)
- [SuspiciousRegAsepUpdate](#suspiciousregasepupdate)
- [NetworkModuleLoadAttempt](#networkmoduleloadattempt)
- [RemovableDiskModuleLoadAttempt](#removablediskmoduleloadattempt)
- [SuspiciousEseFileWritten](#suspiciousesefilewritten)
- [FileDeleteInfo](#filedeleteinfo)
- [SystemTokenStolen](#systemtokenstolen)
- [LowILModuleLoadAttempt](#lowilmoduleloadattempt)
- [ImageHash](#imagehash)
- [TerminateProcess](#terminateprocess)
- [ProcessActivitySummary](#processactivitysummary)
- [KextLoad](#kextload)
- [KextUnload](#kextunload)
- [DirectoryCreate](#directorycreate)
- [SyntheticProcessRollup2](#syntheticprocessrollup2)
- [CriticalFileAccessed](#criticalfileaccessed)
- [CriticalFileModified](#criticalfilemodified)
- [PtyCreated](#ptycreated)
- [FileOpenInfo](#fileopeninfo)
- [FirewallDisabled](#firewalldisabled)
- [FirewallEnabled](#firewallenabled)
- [FileCreateInfo](#filecreateinfo)
- [CriticalEnvironmentVariableChanged](#criticalenvironmentvariablechanged)
- [FileDeleted](#filedeleted)
- [ProcessRollup2](#processrollup2)
- [ReflectiveDllLoaded](#reflectivedllloaded)
- [ProtectVmEtw](#protectvmetw)
- [ProcessWitness](#processwitness)
- [ClipboardPaste](#clipboardpaste)
- [AndroidIntentSentIPC](#androidintentsentipc)
- [MobileOsIntegrityStatus](#mobileosintegritystatus)
- [JarFileWritten](#jarfilewritten)
- [RegGenericValueUpdate](#reggenericvalueupdate)
- [ScreenshotTakenEtw](#screenshottakenetw)
- [SetWinEventHookEtw](#setwineventhooketw)
- [RegSystemConfigValueUpdate](#regsystemconfigvalueupdate)
- [SetThreadCtxEtw](#setthreadctxetw)
- [RegisterRawInputDevicesEtw](#registerrawinputdevicesetw)
- [QueueApcEtw](#queueapcetw)
- [SmbClientNamedPipeConnectEtw](#smbclientnamedpipeconnectetw)
- [ProcessExecOnSMBFile](#processexeconsmbfile)
- [TokenImpersonated](#tokenimpersonated)
- [SetWindowsHookExEtw](#setwindowshookexetw)
- [WmiProviderRegistrationEtw](#wmiproviderregistrationetw)
- [MobileDetection](#mobiledetection)
- [DexFileWritten](#dexfilewritten)
- [DeveloperOptionsStatus](#developeroptionsstatus)
- [SELinuxStatus](#selinuxstatus)
- [StorageEncryptionStatus](#storageencryptionstatus)
- [LockScreenStatus](#lockscreenstatus)
- [SystemPartitionStatus](#systempartitionstatus)
- [SafetyNetCompatibilityStatus](#safetynetcompatibilitystatus)
- [DnsRequestResult](#dnsrequestresult)
- [FileSystemAttributesStatus](#filesystemattributesstatus)
- [DebuggableFlagTurnedOn](#debuggableflagturnedon)
- [BootLoaderStatus](#bootloaderstatus)
- [HarmfulAppData](#harmfulappdata)
- [DuplicateInstallFromPlayStore](#duplicateinstallfromplaystore)
- [ScriptControlScanInfo](#scriptcontrolscaninfo)
- [ObjCRuntimeAltered](#objcruntimealtered)
- [UnexpectedDynamicLibraryLoaded](#unexpecteddynamiclibraryloaded)
- [UnexpectedFileFound](#unexpectedfilefound)
- [TrampolineDetected](#trampolinedetected)
- [CertificatePinningCompromised](#certificatepinningcompromised)
- [ProcessTokenStolen](#processtokenstolen)
- [DebuggedState](#debuggedstate)
- [PathUnexpectedlyReadable](#pathunexpectedlyreadable)
- [UnexpectedEnvironmentVariable](#unexpectedenvironmentvariable)
- [CodeSigningAltered](#codesigningaltered)
- [SafetyNetCheckFailed](#safetynetcheckfailed)
- [SystemPartitionAltered](#systempartitionaltered)
- [InstallFromUnknownSourcesStatus](#installfromunknownsourcesstatus)
- [RemoteBruteForceDetectInfo](#remotebruteforcedetectinfo)
- [SensitiveWmiQuery](#sensitivewmiquery)
- [DCSyncAttempted](#dcsyncattempted)
- [RemediationMonitorRegistryRemoval](#remediationmonitorregistryremoval)
- [ThreadBlocked](#threadblocked)
- [VerifyAppsDisabled](#verifyappsdisabled)
- [DNSRequestDetectInfo](#dnsrequestdetectinfo)
- [DnsRequestBlocked](#dnsrequestblocked)
- [UserSetProcessBreakOnTermination](#usersetprocessbreakontermination)
- [SuspiciousPrivilegedProcessHandle](#suspiciousprivilegedprocesshandle)
- [FileWrittenAndExecutedInContainer](#filewrittenandexecutedincontainer)
- [DwmCompositionResourceExploitAttempt](#dwmcompositionresourceexploitattempt)
- [GenericFileWritten](#genericfilewritten)
- [RemediationMonitorScheduledTaskRemoval](#remediationmonitorscheduledtaskremoval)
- [ReflectiveDotnetModuleLoad](#reflectivedotnetmoduleload)
- [HookedAndroidMethodFound](#hookedandroidmethodfound)
- [SuspiciousAndroidStackTraceElementFound](#suspiciousandroidstacktraceelementfound)
- [SuspiciousAndroidActivityFound](#suspiciousandroidactivityfound)
- [SuspiciousAndroidSystemPropertyFound](#suspiciousandroidsystempropertyfound)
- [SuspiciousAppFound](#suspiciousappfound)
- [SuspiciousAndroidLogcatMessageFound](#suspiciousandroidlogcatmessagefound)
- [NtfsQueryEaExploitAttempt](#ntfsqueryeaexploitattempt)
- [NewExecutableWritten](#newexecutablewritten)
- [RemediationMonitorServiceRemoval](#remediationmonitorserviceremoval)
- [AndroidInitServiceRemoved](#androidinitserviceremoved)
- [AndroidInitServiceAdded](#androidinitserviceadded)
- [SystemUpdatesBlockedByDNS](#systemupdatesblockedbydns)
- [SystemUpdatesBlockedByHTTP](#systemupdatesblockedbyhttp)
- [SystemUpdatesBlockedByFilesystem](#systemupdatesblockedbyfilesystem)
- [ProcessExecOnRDPFile](#processexeconrdpfile)
- [SafetyNetVerifyAppsStatus](#safetynetverifyappsstatus)
- [MemoryProtectionUpdated](#memoryprotectionupdated)
- [NamespaceChanged](#namespacechanged)
- [ProcessSessionCreated](#processsessioncreated)
- [FileSetMode](#filesetmode)
- [BMLFeatureData](#bmlfeaturedata)
- [HostTimeModified](#hosttimemodified)
- [KernelServiceStarted](#kernelservicestarted)
- [RootkitDetectionResponse](#rootkitdetectionresponse)
- [MbrOverwriteRawDetectInfo](#mbroverwriterawdetectinfo)
- [RegCredAccessDetectInfo](#regcredaccessdetectinfo)
- [SourceCodeFileWritten](#sourcecodefilewritten)
- [ArchiveFileContent](#archivefilecontent)
- [UnixFileWritten](#unixfilewritten)
- [ScheduledTaskTamperingRegistryOperation](#scheduledtasktamperingregistryoperation)
- [ScriptFileWrittenInfo](#scriptfilewritteninfo)
- [SmtpEmailMessage](#smtpemailmessage)
- [SessionPatternTelemetry](#sessionpatterntelemetry)
- [PacketFilterAttached](#packetfilterattached)
- [FileStatFsInfo](#filestatfsinfo)
- [UnixName](#unixname)
- [Pop3Command](#pop3command)
- [ThreadPreviousModeMismatch](#threadpreviousmodemismatch)
- [SigningIdentity](#signingidentity)
- [ProcessTokenPrivilegesEdited](#processtokenprivilegesedited)
- [SensorTampering](#sensortampering)
- [MobileOsForensicsReport](#mobileosforensicsreport)
- [IntrusivePackageDiscovered](#intrusivepackagediscovered)
- [IntrusiveProcessDiscovered](#intrusiveprocessdiscovered)
- [MotwWritten](#motwwritten)
- [SignInfoWithContext](#signinfowithcontext)
- [SuspiciousCredentialModuleLoad](#suspiciouscredentialmoduleload)
- [SignInfoWithCertAndContext](#signinfowithcertandcontext)
- [InjectedThreadFromUnsignedModule](#injectedthreadfromunsignedmodule)
- [SuspiciousRawDiskReadFromUnsignedModule](#suspiciousrawdiskreadfromunsignedmodule)
- [FileIntegrityMonitorRuleMatched](#fileintegritymonitorrulematched)
- [MacroContentInfo](#macrocontentinfo)
- [SensorSettingsUpdate](#sensorsettingsupdate)
- [IdpConnectionsOverloadNotification](#idpconnectionsoverloadnotification)
- [ProcessTreeCompositionPatternTelemetry](#processtreecompositionpatterntelemetry)
- [K8SAdmissionReviewResult](#k8sadmissionreviewresult)
- [K8SAdmissionReviewResultPrime](#k8sadmissionreviewresultprime)
- [RemoteCommandResponse](#remotecommandresponse)
- [ProcessRollup2Stats](#processrollup2stats)
- [SuspiciousLackOfProcessRollupEvents](#suspiciouslackofprocessrollupevents)
- [AgentConnect](#agentconnect)
- [IsoExtensionFileWritten](#isoextensionfilewritten)
- [ImgExtensionFileWritten](#imgextensionfilewritten)
- [DcBluetoothDeviceConnectedDetails](#dcbluetoothdeviceconnecteddetails)
- [FirmwareImageAnalyzed](#firmwareimageanalyzed)
- [DirectoryTraversalOverSMB](#directorytraversaloversmb)
- [CrashNotification](#crashnotification)
- [OciContainerComplianceInfo](#ocicontainercomplianceinfo)
- [IdpDcPerfReport](#idpdcperfreport)
- [FileRenameInfo](#filerenameinfo)
- [SensorSelfDiagnosticTelemetry](#sensorselfdiagnostictelemetry)
- [SpotlightEntityBatch](#spotlightentitybatch)
- [CustomIOADomainNameDetectionInfoEvent](#customioadomainnamedetectioninfoevent)
- [CustomIOAFileWrittenDetectionInfoEvent](#customioafilewrittendetectioninfoevent)
- [CustomIOABasicProcessDetectionInfoEvent](#customioabasicprocessdetectioninfoevent)
- [CustomIOANetworkConnectionDetectionInfoEvent](#customioanetworkconnectiondetectioninfoevent)
- [RegistryOperationBlocked](#registryoperationblocked)
- [RegistryOperationDetectInfo](#registryoperationdetectinfo)
- [MacroDetectInfo](#macrodetectinfo)
- [UmppcDetectInfo](#umppcdetectinfo)
- [SnapshotVolumeMounted](#snapshotvolumemounted)
- [ImpersonationTokenInfo](#impersonationtokeninfo)
- [UserIdentity](#useridentity)
- [DriverLoad](#driverload)
- [UserAccountDeleted](#useraccountdeleted)
- [ProcessTrace](#processtrace)
- [InstanceMetadata](#instancemetadata)
- [FileAccessOperationOverSMB](#fileaccessoperationoversmb)
- [K8SSnapshot](#k8ssnapshot)
- [K8SWatchStarted](#k8swatchstarted)
- [K8SResource](#k8sresource)
- [K8SWatchStopped](#k8swatchstopped)
- [IdpEntityRiskScoreChange](#idpentityriskscorechange)
- [HostedServiceStarted](#hostedservicestarted)
- [NetShareAdd](#netshareadd)
- [UserAccountCreated](#useraccountcreated)
- [ServiceStarted](#servicestarted)
- [ScheduledTaskDeleted](#scheduledtaskdeleted)
- [FirewallSetRule](#firewallsetrule)
- [FirewallDeleteRule](#firewalldeleterule)
- [FirewallChangeOption](#firewallchangeoption)
- [UserAccountAddedToGroup](#useraccountaddedtogroup)
- [BITSJobCreated](#bitsjobcreated)
- [EventLogCleared](#eventlogcleared)
- [ScheduledTaskRegistered](#scheduledtaskregistered)
- [NetShareDelete](#netsharedelete)
- [NetShareSecurityModify](#netsharesecuritymodify)
- [VolumeSnapshotCreated](#volumesnapshotcreated)
- [VolumeSnapshotDeleted](#volumesnapshotdeleted)
- [VolumeSnapshotOperationBlocked](#volumesnapshotoperationblocked)
- [MemoryScanErrorEvent](#memoryscanerrorevent)
- [ServiceStopped](#servicestopped)
- [SuspiciousPeFileWritten](#suspiciouspefilewritten)
- [PodInfo](#podinfo)
- [DmpFileWritten](#dmpfilewritten)
- [SevenZipFileWritten](#sevenzipfilewritten)
- [PdfFileWritten](#pdffilewritten)
- [OleFileWritten](#olefilewritten)
- [RarFileWritten](#rarfilewritten)
- [OoxmlFileWritten](#ooxmlfilewritten)
- [ZipFileWritten](#zipfilewritten)
- [RtfFileWritten](#rtffilewritten)
- [PeFileWritten](#pefilewritten)
- [XarFileWritten](#xarfilewritten)
- [BZip2FileWritten](#bzip2filewritten)
- [MachOFileWritten](#machofilewritten)
- [IdwFileWritten](#idwfilewritten)
- [DwgFileWritten](#dwgfilewritten)
- [ELFFileWritten](#elffilewritten)
- [GzipFileWritten](#gzipfilewritten)
- [JavaClassFileWritten](#javaclassfilewritten)
- [CabFileWritten](#cabfilewritten)
- [ArcFileWritten](#arcfilewritten)
- [TiffFileWritten](#tifffilewritten)
- [ArjFileWritten](#arjfilewritten)
- [VmdkFileWritten](#vmdkfilewritten)
- [JpegFileWritten](#jpegfilewritten)
- [BmpFileWritten](#bmpfilewritten)
- [GifFileWritten](#giffilewritten)
- [PngFileWritten](#pngfilewritten)
- [MSXlsxFileWritten](#msxlsxfilewritten)
- [MSPptxFileWritten](#mspptxfilewritten)
- [VdiFileWritten](#vdifilewritten)
- [MSDocxFileWritten](#msdocxfilewritten)
- [MSVsdxFileWritten](#msvsdxfilewritten)
- [DxfFileWritten](#dxffilewritten)
- [RpmFileWritten](#rpmfilewritten)
- [DebFileWritten](#debfilewritten)
- [BlfFileWritten](#blffilewritten)
- [MsiFileWritten](#msifilewritten)
- [LnkFileWritten](#lnkfilewritten)
- [DmgFileWritten](#dmgfilewritten)
- [EmailFileWritten](#emailfilewritten)
- [EmailArchiveFileWritten](#emailarchivefilewritten)
- [EseFileWritten](#esefilewritten)
- [RegistryHiveFileWritten](#registryhivefilewritten)
- [ADExplorerFileWritten](#adexplorerfilewritten)
- [WebScriptFileWritten](#webscriptfilewritten)
- [CrxFileWritten](#crxfilewritten)
- [PythonFileWritten](#pythonfilewritten)
- [HttpRequestDetect](#httprequestdetect)
- [HttpRequest](#httprequest)
- [DcBluetoothDeviceProperties](#dcbluetoothdeviceproperties)
- [IdpCloudHealthStatus](#idpcloudhealthstatus)
- [DiskCapacity](#diskcapacity)
- [MemoryMapped](#memorymapped)
- [TlsClientHello](#tlsclienthello)
- [SmtpAttachment](#smtpattachment)
- [SmtpCommand](#smtpcommand)
- [FtpCommand](#ftpcommand)
- [NetworkLinkConfigGetLink](#networklinkconfiggetlink)
- [NetworkLinkConfigGetAddress](#networklinkconfiggetaddress)
- [RansomwareFileAccessPattern](#ransomwarefileaccesspattern)
- [AsepFileChangeScanInfo](#asepfilechangescaninfo)
- [BPFCommandIssued](#bpfcommandissued)
- [FileSystemOperationBlocked](#filesystemoperationblocked)
- [SecureTrafficDecrypted](#securetrafficdecrypted)
- [FileSystemOperationDetectInfo](#filesystemoperationdetectinfo)
- [ModuleBlockedEventWithPatternId](#moduleblockedeventwithpatternid)
- [ModuleBlockedEvent](#moduleblockedevent)
- [ChannelVersionRequired](#channelversionrequired)
- [LfoUploadDataUnneeded](#lfouploaddataunneeded)
- [LfoUploadDataComplete](#lfouploaddatacomplete)
- [LfoUploadDataFailed](#lfouploaddatafailed)
- [ProvisioningChannelVersionRequired](#provisioningchannelversionrequired)
- [LfoUploadStart](#lfouploadstart)
- [NetworkListenIP4](#networklistenip4)
- [NetworkConnectIP6](#networkconnectip6)
- [NetworkReceiveAcceptIP4](#networkreceiveacceptip4)
- [NetworkReceiveAcceptIP6](#networkreceiveacceptip6)
- [NetworkCloseIP4](#networkcloseip4)
- [NetworkConnectIP4](#networkconnectip4)
- [NetworkListenIP6](#networklistenip6)
- [FirewallSetRuleIP6](#firewallsetruleip6)
- [FirewallDeleteRuleIP4](#firewalldeleteruleip4)
- [FirewallDeleteRuleIP6](#firewalldeleteruleip6)
- [FirewallSetRuleIP4](#firewallsetruleip4)
- [NetworkCloseIP6](#networkcloseip6)
- [NetworkConnectIP4Blocked](#networkconnectip4blocked)
- [NetworkConnectIP6Blocked](#networkconnectip6blocked)
- [NetworkConnectIP4DetectInfo](#networkconnectip4detectinfo)
- [NetworkConnectIP6DetectInfo](#networkconnectip6detectinfo)
- [RemediationActionKillIP4Connection](#remediationactionkillip4connection)
- [RemediationActionKillIP6Connection](#remediationactionkillip6connection)
- [CreateSocket](#createsocket)
- [NetworkOutboundPortScanDetectInfo](#networkoutboundportscandetectinfo)
- [RawBindIP6](#rawbindip6)
- [RawBindIP4](#rawbindip4)
- [NewScriptWritten](#newscriptwritten)
- [PatternHandlingError](#patternhandlingerror)
- [ProcessPatternTelemetry](#processpatterntelemetry)
- [ActiveDirectoryIncomingPsExecExecution2](#activedirectoryincomingpsexecexecution2)
- [IdpPolicyAlertRuleMatch](#idppolicyalertrulematch)
- [BrowserInjectedThread](#browserinjectedthread)
- [KernelCallbackTableUpdate](#kernelcallbacktableupdate)
- [FileDetectInfo](#filedetectinfo)
- [IdpPolicyFederatedAccessRuleMatch](#idppolicyfederatedaccessrulematch)
- [BootLoopProtectionTelemetry](#bootloopprotectiontelemetry)
- [LightningUnresponsiveStatus](#lightningunresponsivestatus)
- [AndroidEnterpriseInfo](#androidenterpriseinfo)
- [InjectedThread](#injectedthread)
- [JavaInjectedThread](#javainjectedthread)
- [DocumentProgramInjectedThread](#documentprograminjectedthread)
- [ActiveDirectoryAuthenticationFailure](#activedirectoryauthenticationfailure)
- [ActiveDirectoryInteractiveDomainLogon](#activedirectoryinteractivedomainlogon)
- [SetWindowsHook](#setwindowshook)
- [ScriptControlDetectInfo](#scriptcontroldetectinfo)
- [ActiveDirectoryAuthentication](#activedirectoryauthentication)
- [ActiveDirectoryServiceAccessRequestFailure](#activedirectoryserviceaccessrequestfailure)
- [CloudAssociateTreeIdWithRoot](#cloudassociatetreeidwithroot)
- [K8SProductConfig](#k8sproductconfig)
- [IdpTelemetryData](#idptelemetrydata)
- [IdpPacketDiversionLdapsConnectionsOverloadNotification](#idppacketdiversionldapsconnectionsoverloadnotification)
- [DataProtectionArchiveAssessed](#dataprotectionarchiveassessed)
- [FileTimestampsModified](#filetimestampsmodified)
- [VMClusterInfo](#vmclusterinfo)
- [VmcSensorStatus](#vmcsensorstatus)
- [VmcVmAsset](#vmcvmasset)
- [InboundHttpParsingStatus](#inboundhttpparsingstatus)
- [InstalledBrowserExtension](#installedbrowserextension)
- [BrowserExtensionStatus](#browserextensionstatus)
- [AssociateIndicator](#associateindicator)
- [FirewallRuleIP6Matched](#firewallruleip6matched)
- [FirewallRuleIP4Matched](#firewallruleip4matched)
- [NamedMutantHandleClosedTelemetry](#namedmutanthandleclosedtelemetry)
- [ProcessControl](#processcontrol)
- [ClassifiedModuleLoad](#classifiedmoduleload)
- [ProcessExecOnPackedExecutable](#processexeconpackedexecutable)
- [IdpCloudHealthConfigurationsGetResponse](#idpcloudhealthconfigurationsgetresponse)
- [ModuleDetectInfo](#moduledetectinfo)
- [AppSideLoaded](#appsideloaded)
- [MobileAppIdentifiers](#mobileappidentifiers)
- [RegValueQueryDetectInfo](#regvaluequerydetectinfo)
- [WmiQueryDetectInfo](#wmiquerydetectinfo)
- [DriverLoadedV2DetectInfo](#driverloadedv2detectinfo)
- [DotnetModuleLoadDetectInfo](#dotnetmoduleloaddetectinfo)
- [PtTelemetry](#pttelemetry)
- [ModuleLoadV3DetectInfo](#moduleloadv3detectinfo)
- [IdpDcTiConfiguration](#idpdcticonfiguration)
- [SmbServerShareOpenedEtw](#smbservershareopenedetw)
- [IdpWatchdogRemediationActionTaken](#idpwatchdogremediationactiontaken)
- [IdpWatchdogRemediationActionTakenForMemory](#idpwatchdogremediationactiontakenformemory)
- [DBusMessage](#dbusmessage)
- [FirewallRuleIP4](#firewallruleip4)
- [InboundHttpHeader](#inboundhttpheader)
- [InternetExposureData](#internetexposuredata)
- [SyntheticSystemdServiceCreated](#syntheticsystemdservicecreated)
- [SystemdTimerDeleted](#systemdtimerdeleted)
- [RouteIP6](#routeip6)
- [DnsServer](#dnsserver)
- [BrowserProxyInfo](#browserproxyinfo)
- [SpotlightSearchEntry](#spotlightsearchentry)
- [RegSystemConfigKeyUpdate](#regsystemconfigkeyupdate)
- [SudoCommandAttempt](#sudocommandattempt)
- [NamedPipeDetectInfo](#namedpipedetectinfo)
- [NetworkEndPointDataUsage](#networkendpointdatausage)
- [UsbDeviceInfo](#usbdeviceinfo)
- [UserAccountRemovedFromGroup](#useraccountremovedfromgroup)
- [SensorEnteredSafemode](#sensorenteredsafemode)
- [PtyDetached](#ptydetached)
- [SystemdServiceCreated](#systemdservicecreated)
- [IdpCloudHealthCheck](#idpcloudhealthcheck)
- [SmbServerLocalNamedPipeOpenedEtw](#smbserverlocalnamedpipeopenedetw)
- [OpenDirectoryAttributeSet](#opendirectoryattributeset)
- [OpenDirectoryAttributeRemove](#opendirectoryattributeremove)
- [RegGenericKeyUpdate](#reggenerickeyupdate)
- [TerminalSavedStateInfo](#terminalsavedstateinfo)
- [OpenDirectoryAttributeAdd](#opendirectoryattributeadd)
- [OpenDirectoryGroupSet](#opendirectorygroupset)
- [ActiveDirectoryAuditGpoModified](#activedirectoryauditgpomodified)
- [FirewallRuleIP6](#firewallruleip6)
- [KernelParameter](#kernelparameter)
- [UserGroupCreated](#usergroupcreated)
- [SystemdServiceDeleted](#systemdservicedeleted)
- [ScheduledTaskInfo](#scheduledtaskinfo)
- [ProcessDataUsage](#processdatausage)
- [WSLVMStopping](#wslvmstopping)
- [SyntheticSystemdTimerCreated](#syntheticsystemdtimercreated)
- [NetShareInfo](#netshareinfo)
- [OsUpdateTimestamp](#osupdatetimestamp)
- [NetworkDnsSuffix](#networkdnssuffix)
- [NetworkHostsFileEntry](#networkhostsfileentry)
- [ActiveDirectoryAuditPasswordModificationAttempt](#activedirectoryauditpasswordmodificationattempt)
- [ProcessSignal](#processsignal)
- [ProcessInjection](#processinjection)
- [SpotlightEntitySystemState](#spotlightentitysystemstate)
- [ConfigurationProfileModified](#configurationprofilemodified)
- [OpenDirectoryDeleteUser](#opendirectorydeleteuser)
- [LogonBehaviorCompositionDetectInfo](#logonbehaviorcompositiondetectinfo)
- [OpenDirectoryGroupAdd](#opendirectorygroupadd)
- [DnsCache](#dnscache)
- [WindowsTimelineEntryTimestamp](#windowstimelineentrytimestamp)
- [BrowserAccountInfo](#browseraccountinfo)
- [BrowserHistoryClearInfo](#browserhistoryclearinfo)
- [ForensicsCollectorOffline](#forensicscollectoroffline)
- [ForensicsCollectorOnline](#forensicscollectoronline)
- [WmiQuery](#wmiquery)
- [FilesStatisticInfo](#filesstatisticinfo)
- [BrowserCookieInfo](#browsercookieinfo)
- [WSLDistributionUnregistered](#wsldistributionunregistered)
- [SystemdTimerCreated](#systemdtimercreated)
- [WSLDistributionStopping](#wsldistributionstopping)
- [DriverLoadBlocked](#driverloadblocked)
- [SigningPublicKey](#signingpublickey)
- [FsVolumeReadInfo](#fsvolumereadinfo)
- [IdpWatchdogRemediationActionRequest](#idpwatchdogremediationactionrequest)
- [ActiveDirectoryAuditGroupModified](#activedirectoryauditgroupmodified)
- [ActiveDirectoryIncomingDceRpcRequest](#activedirectoryincomingdcerpcrequest)
- [DcRemovableStorageDeviceConnected](#dcremovablestoragedeviceconnected)
- [DcRemovableStorageDeviceDisconnected](#dcremovablestoragedevicedisconnected)
- [ScriptControlDotNetMetadata](#scriptcontroldotnetmetadata)
- [GroupAccount](#groupaccount)
- [PrefetchFile](#prefetchfile)
- [BrowserHistoryVisit](#browserhistoryvisit)
- [EventTapInfo](#eventtapinfo)
- [LoginItemAdded](#loginitemadded)
- [IdpPolicyCloudAccessRuleMatch](#idppolicycloudaccessrulematch)
- [SuspiciousUserRemoteAPCAttempt](#suspicioususerremoteapcattempt)
- [SuperfetchAppInfo](#superfetchappinfo)
- [ForensicsCollectorLog](#forensicscollectorlog)
- [RuntimeEnvironmentVariable](#runtimeenvironmentvariable)
- [MftBootSector](#mftbootsector)
- [UserAssistAppLaunchInfo](#userassistapplaunchinfo)
- [IdpWatchdogRemediationActionTakenForCpu](#idpwatchdogremediationactiontakenforcpu)
- [GetAsyncKeyStateEtwBatch](#getasynckeystateetwbatch)
- [NamedPipe](#namedpipe)
- [ProcessHandleTableEntry](#processhandletableentry)
- [DataEgress](#dataegress)
- [WSLDistributionStarted](#wsldistributionstarted)
- [FileSignatureStatistics](#filesignaturestatistics)
- [WSLDistributionRegistered](#wsldistributionregistered)
- [SuperfetchAppSchedule](#superfetchappschedule)
- [WSLVMStarted](#wslvmstarted)
- [LocalGroupIdentity](#localgroupidentity)
- [BrowserExtensionInfo](#browserextensioninfo)
- [DcBluetoothAuthorizationStatus](#dcbluetoothauthorizationstatus)
- [UserGroupDeleted](#usergroupdeleted)
- [GcpAsset](#gcpasset)
- [GcpComputeFirewall](#gcpcomputefirewall)
- [AzureVirtualMachineState](#azurevirtualmachinestate)
- [GcpComputeNetworkPeering](#gcpcomputenetworkpeering)
- [GcpComputeInstance](#gcpcomputeinstance)
- [GcpComputeNetwork](#gcpcomputenetwork)
- [GcpComputeDisk](#gcpcomputedisk)
- [GcpComputeSubnetwork](#gcpcomputesubnetwork)
- [AzureIpConfiguration](#azureipconfiguration)
- [AzureVirtualNetwork](#azurevirtualnetwork)
- [GcpIamServiceAccount](#gcpiamserviceaccount)
- [AzureSubscription](#azuresubscription)
- [AzureNetworkInterface](#azurenetworkinterface)
- [GcpComputeImage](#gcpcomputeimage)
- [AzureResourceGroup](#azureresourcegroup)
- [AzureDisk](#azuredisk)
- [AzureVirtualMachine](#azurevirtualmachine)
- [AzureSubnet](#azuresubnet)
- [AzurePublicIpAddress](#azurepublicipaddress)
- [AzureNetworkSecurityGroup](#azurenetworksecuritygroup)
- [AzureVirtualNetworkPeering](#azurevirtualnetworkpeering)
- [AzurePrivateEndpoint](#azureprivateendpoint)
- [EksNodeGroup](#eksnodegroup)
- [EksCluster](#ekscluster)
- [K8SDeployment](#k8sdeployment)
- [K8SReplicaSet](#k8sreplicaset)
- [K8SDaemonSet](#k8sdaemonset)
- [EksFargateProfile](#eksfargateprofile)
- [IdpWatchdogConfigurationsGetResponse](#idpwatchdogconfigurationsgetresponse)
- [FileContentsChanged](#filecontentschanged)
- [SruApplicationTimelineProvider](#sruapplicationtimelineprovider)
- [ShellBagFileTimeStampMetadata](#shellbagfiletimestampmetadata)
- [SyscacheEntry](#syscacheentry)
- [BITSJobMetadata](#bitsjobmetadata)
- [RegCrowdstrikeValueUpdate](#regcrowdstrikevalueupdate)
- [BrowserDownloadStarted](#browserdownloadstarted)
- [BrowserDownloadEnded](#browserdownloadended)
- [OdsScanComplete](#odsscancomplete)
- [AutoRunProcessInfo](#autorunprocessinfo)
- [PeSectionInfo](#pesectioninfo)
- [ShellBagInfo](#shellbaginfo)
- [PeHeaderOptionalInfo](#peheaderoptionalinfo)
- [RemoteThreadCreate](#remotethreadcreate)
- [ActiveDirectoryAuditGroupMemberModified](#activedirectoryauditgroupmembermodified)
- [RouteIP4](#routeip4)
- [PeFileWrittenDetectInfo](#pefilewrittendetectinfo)
- [MachOHeaderParsed](#machoheaderparsed)
- [MemoryLocked](#memorylocked)
- [VulnerableDriverDetectInfo](#vulnerabledriverdetectinfo)
- [DeliverRulesEngineResultsToCloud](#deliverrulesengineresultstocloud)
- [AtJobInfo](#atjobinfo)
- [HttpResponse](#httpresponse)
- [PcaAppLaunchEntry](#pcaapplaunchentry)
- [SyntheticPR2Stats](#syntheticpr2stats)
- [PcaGeneralDbEntry](#pcageneraldbentry)
- [SyntheticVirtualMemoryArea](#syntheticvirtualmemoryarea)
- [VirtualMemoryArea](#virtualmemoryarea)
- [FileOfInterestBasicInfo](#fileofinterestbasicinfo)
- [FalconProcessHandleOpDetectInfo](#falconprocesshandleopdetectinfo)
- [ScriptFileContentsDetectInfo](#scriptfilecontentsdetectinfo)
- [DnsRequest](#dnsrequest)
- [ArchiveMemberInfo](#archivememberinfo)
- [FileSystemContainmentStatus](#filesystemcontainmentstatus)
- [SystemExtension](#systemextension)
- [SharedObjectLoaded](#sharedobjectloaded)
- [SignInfo](#signinfo)
- [MalPaths](#malpaths)
- [AppleScriptFileWritten](#applescriptfilewritten)
- [LzfseFileWritten](#lzfsefilewritten)
- [FileTimestampMetadata](#filetimestampmetadata)
- [BITSJobFileInfo](#bitsjobfileinfo)
- [LinkFileInfo](#linkfileinfo)
- [LogEntry](#logentry)
- [FileEntry](#fileentry)
- [PtyAttached](#ptyattached)
- [PeHeaderInfo](#peheaderinfo)
- [EntropyScan](#entropyscan)
- [LSQuarantineEvent](#lsquarantineevent)
- [PemFileWritten](#pemfilewritten)
- [RecentExecutionTimestamp](#recentexecutiontimestamp)
- [ArchiveInfo](#archiveinfo)
- [FileWrittenWithEntropyHigh](#filewrittenwithentropyhigh)
- [MftRecord](#mftrecord)
- [XzFileWritten](#xzfilewritten)
- [SyntheticSharedObjectLoaded](#syntheticsharedobjectloaded)
- [AmcacheEntry](#amcacheentry)
- [MemoryAdvise](#memoryadvise)
- [WebShellDetected](#webshelldetected)
- [UserEatAccessMonitoring](#usereataccessmonitoring)
- [ClassifiedProcessStart](#classifiedprocessstart)
- [PromiscuousBindIP4](#promiscuousbindip4)
- [DcUsbDevicePolicyViolation](#dcusbdevicepolicyviolation)
- [DcBluetoothDeviceBlocked](#dcbluetoothdeviceblocked)
- [DcBluetoothDevicePolicyViolation](#dcbluetoothdevicepolicyviolation)
- [SruApplicationResourceUsage](#sruapplicationresourceusage)
- [NtfsLinkCreatedDetectInfo](#ntfslinkcreateddetectinfo)
- [IPCDetectInfo](#ipcdetectinfo)
- [MacKnowledgeActivityStart](#macknowledgeactivitystart)
- [MemoryProtectionChanged](#memoryprotectionchanged)
- [ScheduledTaskTemplateDetectInfo](#scheduledtasktemplatedetectinfo)
- [DcRemovableStorageDeviceBlocked](#dcremovablestoragedeviceblocked)
- [DcRemovableStorageDevicePolicyViolation](#dcremovablestoragedevicepolicyviolation)
- [ResourceLimit](#resourcelimit)
- [RegFeatureUsageInfo](#regfeatureusageinfo)
- [HttpRequestV2Detect](#httprequestv2detect)
- [HostedServiceStatusInfo](#hostedservicestatusinfo)
- [RegCrowdstrikeKeyUpdate](#regcrowdstrikekeyupdate)
- [K8SInitContainerStatus](#k8sinitcontainerstatus)
- [AzureNatFirewallRule](#azurenatfirewallrule)
- [ActiveDirectoryIncomingLdapSearchRequest](#activedirectoryincomingldapsearchrequest)
- [AksCluster](#akscluster)
- [AksAgentPool](#aksagentpool)
- [K8SPod](#k8spod)
- [K8SService](#k8sservice)
- [K8SNode](#k8snode)
- [K8SRunningContainer](#k8srunningcontainer)
- [AzureFirewall](#azurefirewall)
- [AzureFirewallRuleCollection](#azurefirewallrulecollection)
- [AzureNetworkSecurityGroupRule](#azurenetworksecuritygrouprule)
- [K8SEphemeralContainer](#k8sephemeralcontainer)
- [K8SRunningContainerStatus](#k8srunningcontainerstatus)
- [AksVMSS](#aksvmss)
- [K8SInitContainer](#k8sinitcontainer)
- [AzureApplicationFirewallRule](#azureapplicationfirewallrule)
- [BamRegAppRunTime](#bamregappruntime)
- [ScriptControlDetectInvalidInfo](#scriptcontroldetectinvalidinfo)
- [UserAccount](#useraccount)
- [JumpListInfo](#jumplistinfo)
- [RegShimCache](#regshimcache)
- [ActiveDirectoryAuditUserModified](#activedirectoryauditusermodified)
- [KernelExtension](#kernelextension)
- [AzureNetworkFirewallRule](#azurenetworkfirewallrule)
- [ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate](#activedirectoryaccountdirectcontaininggroupentitiesupdate)
- [ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate](#activedirectoryaccountflattenedcontaininggroupentitiesupdate)
- [ConfigStateUpdate](#configstateupdate)
- [LFODownloadConfirmation](#lfodownloadconfirmation)
- [ASLRBypassAttempt](#aslrbypassattempt)
- [HeapSprayAttempt](#heapsprayattempt)
- [SEHOverWriteAttempt](#sehoverwriteattempt)
- [SsoUserLogon](#ssouserlogon)
- [SsoUserLogonFailure](#ssouserlogonfailure)
- [SsoApplicationAccess](#ssoapplicationaccess)
- [AdditionalHostInfo](#additionalhostinfo)
- [AndroidModuleStateUpdate](#androidmodulestateupdate)
- [SsoApplicationAccessFailure](#ssoapplicationaccessfailure)
- [UserAccessLogEntry](#useraccesslogentry)
- [FileSignatureMismatch](#filesignaturemismatch)
- [RemoteProcessMemoryWrite](#remoteprocessmemorywrite)
- [FileHashesEvent](#filehashesevent)
- [WindowsTimelineEntry](#windowstimelineentry)
- [OpenDirectoryGroupRemove](#opendirectorygroupremove)
- [RegGenericInfo](#reggenericinfo)
- [MacKnowledgeActivityEnd](#macknowledgeactivityend)
- [MacMRU](#macmru)
- [WlanInterfaceInfo](#wlaninterfaceinfo)
- [ShimDbTag](#shimdbtag)
- [SruNetworkConnectivityUsage](#srunetworkconnectivityusage)
- [FileExtendedAttrOperation](#fileextendedattroperation)
- [USNRecord](#usnrecord)
- [PeCodePageInfo](#pecodepageinfo)
- [RemoteProcessMemoryRead](#remoteprocessmemoryread)
- [XProtectAction](#xprotectaction)
- [AspmCollectionStatusUpdate](#aspmcollectionstatusupdate)
- [ProcessOpenedFileDescriptor](#processopenedfiledescriptor)
- [EddScanStart](#eddscanstart)
- [CreateThreadNoStartImage](#createthreadnostartimage)
- [CreateThreadReflectiveDll](#createthreadreflectivedll)
- [UmppcEntryAnomaly](#umppcentryanomaly)
- [ScriptControlBlocked](#scriptcontrolblocked)
- [ProcessHandleOpDetectInfo](#processhandleopdetectinfo)
- [ReflectiveDllOpenProcess](#reflectivedllopenprocess)
- [ScriptControlScanTelemetry](#scriptcontrolscantelemetry)
- [IdpPolicyAccessRuleMatch](#idppolicyaccessrulematch)
- [CreateThreadKernelNoStartImage](#createthreadkernelnostartimage)
- [IdpWatchdogReEnabled](#idpwatchdogreenabled)
- [SensorSelfDiagnosticAlert](#sensorselfdiagnosticalert)
- [ExtendedExploitMitigationViolatedDetectInfo](#extendedexploitmitigationviolateddetectinfo)
- [ProcessState](#processstate)
- [FfcBytePatternScanResult](#ffcbytepatternscanresult)
- [CSAResultsGenericDetectInfo](#csaresultsgenericdetectinfo)
- [DataProtectionBrowserConnect](#dataprotectionbrowserconnect)
- [ProcessSubstituteUser](#processsubstituteuser)
- [DcUsbDeviceConnected](#dcusbdeviceconnected)
- [GcpComputeNetworkInterface](#gcpcomputenetworkinterface)
- [SuspectCreateThreadStack](#suspectcreatethreadstack)
- [ErrorEvent](#errorevent)
- [ResourceUtilization](#resourceutilization)
- [RecentlyModifiedFileExecutedInContainer](#recentlymodifiedfileexecutedincontainer)
- [DetectionExcluded](#detectionexcluded)
- [ZstdFileWritten](#zstdfilewritten)
- [LhaFileWritten](#lhafilewritten)
- [BcmFileWritten](#bcmfilewritten)
- [FreeArcFileWritten](#freearcfilewritten)
- [Base64PeFileWritten](#base64pefilewritten)
- [LRZipFileWritten](#lrzipfilewritten)
- [BlakHoleFileWritten](#blakholefilewritten)
- [ZpaqFileWritten](#zpaqfilewritten)
- [BrotliFileWritten](#brotlifilewritten)
- [PeaFileWritten](#peafilewritten)
- [Yz1FileWritten](#yz1filewritten)
- [NetworkSummary](#networksummary)
- [LZipFileWritten](#lzipfilewritten)
- [ProcessEnvironmentEmpty](#processenvironmentempty)
- [NetworkStatisticsIP6](#networkstatisticsip6)
- [LzmaFileWritten](#lzmafilewritten)
- [SyntheticProcessTrace](#syntheticprocesstrace)
- [ShellCommandLineInfo](#shellcommandlineinfo)
- [NetworkStatisticsUDP6](#networkstatisticsudp6)
- [LZOFileWritten](#lzofilewritten)
- [NetworkStatisticsTCP4](#networkstatisticstcp4)
- [NetworkStatisticsUDP4](#networkstatisticsudp4)
- [NetworkStatisticsIP4](#networkstatisticsip4)
- [PromiscuousBindIP6](#promiscuousbindip6)
- [LZ4FileWritten](#lz4filewritten)
- [MpThreatWMI](#mpthreatwmi)
- [NetworkStatisticsTCP6](#networkstatisticstcp6)
- [NetworkIcmpDataIP4](#networkicmpdataip4)
- [SensorMetadataUpdate](#sensormetadataupdate)
- [UserExceptionDEP](#userexceptiondep)
- [MpThreatAction](#mpthreataction)
- [ClassifiedSensitiveFileAccess](#classifiedsensitivefileaccess)
- [PhpEvalString](#phpevalstring)
- [PhpExecuteScript](#phpexecutescript)
- [PhpBase64Decode](#phpbase64decode)
- [FileDescriptorMonitor](#filedescriptormonitor)
- [WSLMetadata](#wslmetadata)
- [BITSJobInfo](#bitsjobinfo)
- [MpThreat](#mpthreat)
- [MpThreatDetection](#mpthreatdetection)
- [NetworkIcmpDataIP6](#networkicmpdataip6)
- [MpThreatDetectionWMI](#mpthreatdetectionwmi)
- [DataProtectionPACDiagnostic](#dataprotectionpacdiagnostic)
- [InstallServiceDownloadComplete](#installservicedownloadcomplete)
- [QuarantineActionResult](#quarantineactionresult)
- [UpdateManifestDownloadComplete](#updatemanifestdownloadcomplete)
- [NetworkUncontainmentCompleted](#networkuncontainmentcompleted)
- [QuarantinedFile](#quarantinedfile)
- [InstallBundleDownloadComplete](#installbundledownloadcomplete)
- [NetworkContainmentCompleted](#networkcontainmentcompleted)
- [SAMHashDumpFromUnsignedModule](#samhashdumpfromunsignedmodule)
- [QuarantinedFileState](#quarantinedfilestate)
- [OsfmDownloadComplete](#osfmdownloadcomplete)
- [InstalledUpdates](#installedupdates)
- [UserFontLoad](#userfontload)
- [NullPageUnmapAttempt](#nullpageunmapattempt)
- [UmppaErrorEvent](#umppaerrorevent)
- [NullPageProtectionModificationAttempt](#nullpageprotectionmodificationattempt)
- [RansomwareOpenFile](#ransomwareopenfile)
- [RegNtPostOpenKeyEx](#regntpostopenkeyex)
- [FsPostCreate](#fspostcreate)
- [ManifestDownloadComplete](#manifestdownloadcomplete)
- [ConfigDownloadComplete](#configdownloadcomplete)
- [FsPostOpen](#fspostopen)
- [ModuleDownloadComplete](#moduledownloadcomplete)
- [ECBDownloadComplete](#ecbdownloadcomplete)
- [RegKeySecurityDecreasedFromUnsignedModule](#regkeysecuritydecreasedfromunsignedmodule)
- [ChannelDataDownloadComplete](#channeldatadownloadcomplete)
- [FsPostOpenSnapshotFile](#fspostopensnapshotfile)
- [PrivilegedProcessHandle](#privilegedprocesshandle)
- [FsPostOpenUpImpersonating](#fspostopenupimpersonating)
- [RegNtPostOpenKeyExUpImpersonating](#regntpostopenkeyexupimpersonating)
- [PrivilegedProcessHandleFromUnsignedModule](#privilegedprocesshandlefromunsignedmodule)
- [ConfigurationLoaded](#configurationloaded)
- [OciImageInfo](#ociimageinfo)
- [CsUmProcessCrashSummaryEvent](#csumprocesscrashsummaryevent)
- [FirewallRuleApplicationFailed](#firewallruleapplicationfailed)
- [FalconServiceStatus](#falconservicestatus)
- [RemediationActionServiceRemoval](#remediationactionserviceremoval)
- [CidMigrationError](#cidmigrationerror)
- [CidMigrationManifestDownloadComplete](#cidmigrationmanifestdownloadcomplete)
- [AmsBytePatternScanTelemetry](#amsbytepatternscantelemetry)
- [AmsBytePatternScanResult](#amsbytepatternscanresult)
- [RecoveryActionDeleteFilesComplete](#recoveryactiondeletefilescomplete)
- [RecoveryActionRegistryDeleteValueKeyComplete](#recoveryactionregistrydeletevaluekeycomplete)
- [RecoveryActionRegistryDeleteKeyComplete](#recoveryactionregistrydeletekeycomplete)
- [RecoveryActionRegistryDeleteKeyReply](#recoveryactionregistrydeletekeyreply)
- [RecoveryActionRegistryCreateKeyComplete](#recoveryactionregistrycreatekeycomplete)
- [RecoveryActionManipulateModuleTableComplete](#recoveryactionmanipulatemoduletablecomplete)
- [RecoveryActionKillProcessesComplete](#recoveryactionkillprocessescomplete)
- [RecoveryActionKillProcessesReply](#recoveryactionkillprocessesreply)
- [PackageManagerDownloadComplete](#packagemanagerdownloadcomplete)
- [OciContainerPlumbingSummary](#ocicontainerplumbingsummary)
- [EddScanStatus](#eddscanstatus)
- [LFODownloadComplete](#lfodownloadcomplete)
- [IdpCloudHealthConfigurationsSetResponse](#idpcloudhealthconfigurationssetresponse)
- [IdpWatchdogConfigurationsSetResponse](#idpwatchdogconfigurationssetresponse)
- [RemediationMonitorKillProcess](#remediationmonitorkillprocess)
- [RemediationActionQuarantineMacroFile](#remediationactionquarantinemacrofile)
- [KernelCallbackTablePatch](#kernelcallbacktablepatch)
- [EarlyExploitPivotDetect](#earlyexploitpivotdetect)
- [SuspiciousUserFontLoad](#suspicioususerfontload)
- [CommsLogReset](#commslogreset)
- [RecoveryActionRegistrySetValueKeyReply](#recoveryactionregistrysetvaluekeyreply)
- [RecoveryActionSetRuntimeSystemTagsComplete](#recoveryactionsetruntimesystemtagscomplete)
- [RecoveryActionSetSystemTagsComplete](#recoveryactionsetsystemtagscomplete)
- [RecoveryActionGetSystemTagsComplete](#recoveryactiongetsystemtagscomplete)
- [OpenDirectoryPasswordModification](#opendirectorypasswordmodification)
- [RecoveryActionDeleteFilesReply](#recoveryactiondeletefilesreply)
- [RecoveryActionGetModuleTableRecordComplete](#recoveryactiongetmoduletablerecordcomplete)
- [OciContainerInfo](#ocicontainerinfo)
- [HttpVisibilityStatus](#httpvisibilitystatus)
- [SSHClientAuthenticated](#sshclientauthenticated)
- [RecoveryActionGetRuntimeSystemTagsComplete](#recoveryactiongetruntimesystemtagscomplete)
- [DriverPreventFailed](#driverpreventfailed)
- [RemediationActionKillProcess](#remediationactionkillprocess)
- [RemediationActionQuarantineFile](#remediationactionquarantinefile)
- [RemediationMonitorQuarantineFile](#remediationmonitorquarantinefile)
- [CreateProcessArgs](#createprocessargs)
- [CloudScanControl](#cloudscancontrol)
- [RemediationActionRegistryRemoval](#remediationactionregistryremoval)
- [BlockThreadFailed](#blockthreadfailed)
- [KillProcessError](#killprocesserror)
- [MacFsEventRecord](#macfseventrecord)
- [ExcelDocumentOpened](#exceldocumentopened)
- [QuarantineXattribute](#quarantinexattribute)
- [AppProtocolDetected](#appprotocoldetected)
- [RemediationActionQuarantineOfficeMacroFile](#remediationactionquarantineofficemacrofile)
- [OpenDirectoryCreateUser](#opendirectorycreateuser)
- [ZerologonExploitAttempt](#zerologonexploitattempt)
- [PeLanguageId](#pelanguageid)
- [MsiTransactionExecuted](#msitransactionexecuted)
- [RecoveryActionRegistryDeleteValueKeyReply](#recoveryactionregistrydeletevaluekeyreply)
- [RecoveryActionRegistrySetValueKeyComplete](#recoveryactionregistrysetvaluekeycomplete)
- [EtwComponentResponse](#etwcomponentresponse)
- [SuspendProcessError](#suspendprocesserror)
- [RemediationActionScheduledTaskRemoval](#remediationactionscheduledtaskremoval)
- [RecoveryActionRegistryCreateKeyReply](#recoveryactionregistrycreatekeyreply)

---

## Summary Table

| Header | Description | Platforms |
|--------|-------------|------------|
| AcUninstallConfirmation | This event is generated when a Falcon sensor is uninstalled from a host. Important: The Falcon senso... | Windows, macOS, Linux |
| AcUnloadConfirmation | The cloud will respond with this event as acknowledgement that a sensor was uninstalled. | Windows, macOS, Linux |
| HostInfo | This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a ... | Windows, macOS, iOS, Windows Legacy |
| HookedDriverObject | This event describes the presence of a hooked pointer in a DRIVER_OBJECT structure. | Windows |
| WfpFilterTamperingFilterDeleted | This event is created whenever WFP indicates to our callout driver that a filter that references one... | Windows |
| WfpFilterTamperingFilterAdded | This event is created whenever WFP indicates to our callout driver that a new filter that references... | Windows |
| DeliverLocalFXToCloud | DeliverLocalFXToCloud conveys feature extraction (FX) data to the cloud from the sensor. `DeliverLoc... | Windows, macOS, Linux |
| UserLogoff | This event is generated when a user logs off from a host. | Windows, macOS, Linux, ChromeOS |
| NeighborListIP4 | This event shows the IPv4 network addresses and MAC addresses of other devices on the host's network... | Windows, macOS, Linux, Falcon Container, Forensics |
| NeighborListIP6 | This event shows the MAC addresses and IPv6 network addresses of other devices on the host's network... | Windows, macOS, Linux, Falcon Container, Forensics |
| LocalIpAddressRemovedIP4 | This event is generated when a host loses its IPv4 network address. | Windows, macOS, Linux, Falcon Container, iOS, Android |
| LocalIpAddressRemovedIP6 | This event is generated when a host loses its IPv6 network address. | Windows, macOS, Linux, Falcon Container, iOS, Android |
| DcUsbEndpointDescriptor | An event that describes an endpoint descriptor extracted from the firmware of a USB device. An inter... | Windows, macOS, Linux |
| DcUsbHIDDescriptor | This event describes a HID (Human Interface Device) descriptor extracted from the firmware of a USB ... | Windows, macOS, Linux |
| DcStatus | An event that contains the status information for the Device Control plug-and-play driver. It is sen... | Windows, macOS, Linux |
| DcUsbConfigurationDescriptor | An event that describes a configuration descriptor extracted from the firmware of a USB device. This... | Windows, macOS, Linux |
| DcUsbInterfaceDescriptor | An event that describes an interface descriptor extracted from the firmware of a USB device. There a... | Windows, macOS, Linux |
| DcUsbDeviceDisconnected | An event that describes a disconnected USB device to which Device Control has previously attached. I... | Windows, macOS, Linux |
| DcOnline | An event that indicates the Device Control plug-and-play driver interface has come online. It is sen... | Windows, macOS, Linux |
| DcOffline | An event that indicates the Device Control plug-and-play driver interface has gone offline. It is se... | Windows, macOS, Linux |
| DcUsbDeviceWhitelisted | An event that indicates a USB device was added to an allowlist by a Device Control policy. The Devic... | Windows, macOS, Linux |
| AwsIamAccountAlias | Information from AWS API call ListAccountAliases. | Windows, Public Cloud |
| FirmwareAnalysisStatus | This event contains status of the FPnP filter driver. | Windows, macOS |
| FirmwareRegionMeasured | Indicates that a certain region of a firmware image was measured. | Windows, macOS |
| FirmwareAnalysisErrorEvent | Indicates an occurrence of error associated with the Firmware Analysis feature. | Windows, macOS |
| FirmwareAnalysisHardwareData | This event contains hardware data collected by Firmware Analysis. | Windows, macOS |
| AwsEc2NetworkInterface | This event provides key metadata regarding network interfaces in AWS. CrowdStrike retrieves this inf... | Windows, Public Cloud |
| AwsEc2NetworkInterfacePrivateIP | This event provides key metadata regarding private IP addresses in AWS. CrowdStrike retrieves this i... | Windows, Public Cloud |
| AwsEc2Volume | This event provides key metadata regarding EBS volumes configured in AWS. CrowdStrike retrieves this... | Windows, Public Cloud |
| AwsEc2Instance | This event provides key metadata regarding EC2 instances in AWS. CrowdStrike retrieves this informat... | Windows, Public Cloud |
| AwsEc2SecurityGroup | This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this inform... | Windows, Public Cloud, Windows, Public Cloud |
| AwsEc2Subnet | This event provides key metadata regarding subnets configured in AWS. CrowdStrike retrieves this inf... | Windows, Public Cloud |
| AwsEc2Image | This event provides key metadata regarding images (AMIs, AKIs, and ARIs) available in AWS. CrowdStri... | Windows, Public Cloud |
| AwsEc2SecurityGroupRule | This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this inform... | Windows, Public Cloud |
| AwsEc2NetworkAcl |  | Windows, Public Cloud |
| AwsEc2NetworkAclEntry | Information from AWS API call DescribeNetworkAcls. | Windows, Public Cloud |
| GroupIdentity | Provides the sensor boot unique mapping between GID, AuthenticationId, UserPrincipal, and UserSid. | macOS, Forensics |
| IOServiceRegister | This event describes an IOService being registered with a notification handler. | macOS |
| LocalIpAddressIP4 | This event is generated when a host uses a new IPv4 network address. | Linux, Falcon Container, iOS, Android, macOS, Windows, Forensics |
| LocalIpAddressIP6 | This event is generated when a host uses a new IPv6 network address. | Linux, Falcon Container, iOS, Android, macOS, Windows, Forensics |
| HostnameChanged | Sent by the hostname awareness actor to communicate change in hostname. | Linux, Falcon Container, macOS |
| OsVersionInfo | This event is generated during any one of the following scenarios: A host is turned on or rebooted A... | Android, iOS, Windows, macOS, Linux, Falcon Container, Forensics, Windows Legacy, Vmcluster, Kubernetes |
| APKMetadata | Sent from mobile sensor in PlayStore mode when a new APK file is present on the device, as a result ... | Android |
| MobileAppsManifest | Delivers information about apps. Fields: Android | Android |
| UncontainerizeAppResponse | Sent in response to UncontainerizeApp, containing response information for the operation. Fields: An... | Android |
| WiFiConnect | Sent when a device connects to a WiFi network. This event is only sent if the Connected Wi-Fi networ... | Android, iOS |
| WiFiDisconnect | Sent when a device disconnects from a WiFi network. This event is only sent if the Connected Wi-Fi n... | Android, iOS |
| MobilePowerStats | Sent when power level in a mobile device changes, also contains duration when the sensor is in foreg... | Android, iOS |
| ContainerizationUpdate | Sent following an LFODownload of a new APK to be installed or updated in the container, containing r... | Android |
| FileInfo | Error event for FileInfo response. FileInfo response with information about a file. Fields: Forensic... | Forensics, macOS |
| ClipboardCopy | Sent when content is copied to the clipboard. | iOS, Android |
| InstalledApplication | An event that describes a single application. E.g. representing a newly installed application, one j... | Windows, macOS, Linux, Forensics |
| SmbClientShareOpenedEtw | An event that indicates when a machine connects to a remote share. This event is supported on all Wi... | Windows |
| SmbClientShareClosedEtw | An event that indicates when a machine disconnects from a remote share. This event is supported on a... | Windows |
| SmbServerV1AuditEtw | An event that indicates that a client attempted to connect to this machine using the Server Message ... | Windows |
| DeactivateMobileSensorResponse | Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. On Android, container... | Android, iOS |
| AccessoryConnected | Sent when the device connects to an external accessory. This event will only be sent if the Connecte... | Android, iOS |
| AccessoryDisconnected | Sent when a device disconnects from an external accessory. This event will only be sent if the Conne... | Android, iOS |
| BillingInfo | Sensor sends this event to inform the cloud about the sensor billing type. | Windows, Linux, Falcon Container, macOS |
| EtwErrorEvent | An event that indicates that an error occurred which associated is with the ETW consumer. | Windows |
| OciContainerTelemetry | An event that contains telemetry information on a container. | Linux, Falcon Container |
| OciContainerStarted | An event that is sent by the sensor to indicate a container has started when the container is create... | Linux, Falcon Container |
| OciImageHeartbeat | An event that is sent by the sensor to indicate this image is still being used. | Linux, Falcon Container |
| OciContainerHeartbeat | An event that is sent by the sensor to indicate this container engine is still being used. This even... | Linux, Falcon Container |
| OciContainerStopped | An event sent to indicate a container has stopped when the container is deleted. | Linux, Falcon Container |
| AuditCveKmEtw | An event that indicates that a driver or the kernel reported a known CVE (Common Vulnerabilities and... | Windows |
| CsUmProcessCrashAuxiliaryEvent | An event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field... | Windows |
| FsVolumeMounted | Provides information about a mounted volume. Fields: Forensics | Forensics, iOS, Windows, Linux, Falcon Container, macOS |
| OciContainerEngineInfo | An event that contains information about this container engine. | Linux, Falcon Container |
| AuditCveUmEtw | An event that indicates that an application reported a known CVE (Common Vulnerabilities and Exposur... | Windows |
| SystemCapacity | An event that describes the CPU and RAM capacity of the system. The event is sent when the sensor co... | Windows, macOS, Linux |
| AndroidManifestXmlUploaded | An event that indicates the LFO upload of the AndroidManifest of an android application package was ... | Android |
| AndroidManifestFragmentData | An event that's sent by the sensor along with AndroidManifestXmlUploaded that contains a logical por... | Android, Windows |
| FileVaultStatus | Contains information regarding the system FileVault (encrypted) state. | macOS |
| AmsiRegistrationStatus | Event to record status in AMSI module. | Windows |
| PtActivationStatus | Reports host's compatibility with the Processor Trace feature. | Windows |
| ProvisioningStarted | Sent when sensor begins provisioning. | Windows |
| ProvisioningStatusUpdate | Sent every 2 minutes during provisioning. | Windows |
| ProvisioningEnded | Sent when provisioning is completed. | Windows |
| K8SCluster | Snapshot of Kubernetes cluster for mapping Kubernetes cluster id and name. Fields: Public Cloud | Public Cloud |
| SpotlightEntityBatchHeader | Spotlight Batch header to indicate all required metadata of incoming batch along with information to... | Windows, macOS, Linux |
| RemovableMediaVolumeMounted | This event provides information about a removable media volume that was just mounted. Fields: Androi... | Android, Windows |
| FsVolumeUnmounted | Provides information about an unmounted volume. | iOS, Windows, macOS, Linux, Falcon Container |
| RemovableMediaVolumeUnmounted | An event that contains information about a removable media volume that was just unmounted. Fields: A... | Android |
| RemovableMediaFileWritten | An event that is emitted for files written to removable media on Android devices. Fields: Android | Android |
| ActiveDirectoryAccountNameUpdate | Indicates a change to the subject account's SAM account name. | Windows |
| ActiveDirectoryAccountOuUpdate | Indicates a change to the subject account's organizational unit. | Windows |
| ActiveDirectoryAccountDisabled | Indicates the subject account has been disabled. | Windows |
| ActiveDirectoryAccountLocked | Indicates the subject account has been locked. | Windows |
| ActiveDirectoryAccountUnlocked | Indicates the subject account has been unlocked. | Windows, Windows |
| ActiveDirectoryAccountCreated | Indicates the creation of the subject account. | Windows |
| ActiveDirectoryAccountPasswordUpdate | Indicates a change to the subject account's password. | Windows |
| ActiveDirectoryAccountEnabled | Indicates the subject account has been enabled. | Windows |
| StaticAnalysisContainerTelemetry | Cloudable event in response to a telemetry query for the static analysis containers. | Windows |
| UserInformationEtw | An event that indicates the password of a user was changed or set and other user information taken f... | Windows |
| TcgPcrInfo | An event that contains the Platform Configuration Register (PCR) values. | Windows |
| DcBluetoothDeviceDisconnected | This event represents a disconnected Bluetooth device. | Windows, macOS |
| DiskUtilization | An event that contains the used and available storage space for each mounted logical drive or volume... | Linux, Forensics |
| DcBluetoothDeviceConnected | This event represents a connected Bluetooth device. | Windows, macOS |
| CidMigrationConfirmation |  | macOS, Linux, Windows |
| CidMigrationComplete |  | macOS, Windows, Linux, Android |
| DriverPreventionStatus |  | Windows |
| SensorGroupingTagsUpdate |  | Windows |
| SysConfigInfo |  | Linux, Falcon Container |
| IdpPolicyAccountEventRuleMatch | Fields: Public Cloud | Public Cloud |
| UserLogon | This event is generated when a user logs on to a host. | Linux, Windows, macOS, ChromeOS |
| SensorAntiTamperState |  | Windows |
| UserLogonFailed2 | An event that indicates that a local user attempted to logon, but failed due to bad password. LogonT... | Linux, ChromeOS, macOS, Windows, Windows |
| ServicesStatusInfo | Detailed information and status of a windows service. | Windows, Forensics |
| OdsCancelRequestReceived |  | Windows, macOS |
| OdsScheduleCancelRequestReceived |  | Windows, macOS |
| OdsScheduleRequestReceived |  | Windows, macOS |
| OdsStarted |  | Windows, macOS |
| OdsProfileReceived |  | Windows, macOS |
| OdsStartRequestReceived |  | Windows, macOS |
| OdsMaliciousFileFound |  | Windows, macOS |
| OdsActionStatus |  | Windows, macOS |
| ChannelActive |  | Windows |
| OdsScheduleCanceled |  | Windows, macOS |
| OdsStatus |  | Windows, macOS |
| DcIdentification | This event enables monitoring of domain controllers (DCs) and the passing of identifying information... | Windows |
| K8SClusterInfo | Fields: Kubernetes | Kubernetes |
| AgentOnline | This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor ... | ChromeOS, macOS, Windows, Linux, Falcon Container, Android, Kubernetes, iOS, Windows Legacy, Vmcluster |
| SensorHeartbeat | Sent periodically to inform the cloud that the sensor is active. Sent periodically to inform the clo... | ChromeOS, Windows Legacy, Vmcluster, Android, iOS, macOS, Windows, Linux, Falcon Container, Kubernetes |
| LocalWindowsUserUpdate |  | Windows |
| SmbClientShareLogonBruteForceSuspected |  | Windows, Windows |
| CsKmCrashSummaryEvent |  | Windows |
| LockdownModeStatus |  | iOS |
| IdpContainerRestarted |  | Windows |
| AsepValueUpdate | This event is generated when a Microsoft Auto Start Execution Point registry key has been updated. | Windows, Windows, macOS, Linux, Falcon Container |
| RansomwareRenameFile | A reified LocalFsPostRename event so the cloud can route these events for ransomware support. | Windows |
| AsepKeyUpdate | Generated when an Auto Start Execution Point registry key is updated. | Windows |
| ProcessRollup | An event that contains information from several sources and combines it into one event. The event de... | Windows |
| PeVersionInfo | An event that describes file version information from a Portable Executable file resource location, ... | Windows |
| KernelModeLoadImage | Indicates a kernel-mode module has been loaded into memory. | Windows, macOS, Linux, Falcon Container, Forensics |
| IoSessionConnected | An event that is emitted when an IO session has been connected. | Windows |
| IoSessionLoggedOn | An event that is emitted when an IO session has been logged off. | Windows |
| CreateService | Generated when a Windows service is created. | Windows |
| ModifyServiceBinary | Indicates a Windows service's binary was changed. | Windows |
| UACCredentialCaptureElevation | This UAC event indicates the UAC consent.exe application was used by Windows to refresh the smart ca... | Windows |
| UACCOMElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target COM... | Windows |
| UACMSIElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target MSI... | Windows |
| WroteExeAndGeneratedServiceEvent | Indicates a process both wrote an executable and generated a service event. | Windows, Windows |
| UACAxisElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target Act... | Windows |
| DllInjection | This event indicates that DLL injection occurred in the target process. | Windows |
| UnsignedModuleLoad | This event contains information about an unsigned module that was loaded into a target process. It c... | Windows |
| SuspiciousRawDiskRead | This event indicates a process successfully read a target file using raw disk access. | Windows |
| HostedServiceStopped | This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is stop... | Windows |
| WmiCreateProcess | Windows Management Instrumentation (WMI) is a default service installed on machines with Windows XP ... | Windows |
| ExecutableDeleted | This event indicates that an executable was deleted from the host. | Windows, macOS, Linux |
| NewExecutableRenamed | This event is generated when an executable is renamed. | Windows, macOS |
| SuspiciousDnsRequest | This event is generated when the sensor detects a suspicious DNS request. A request is suspicious if... | Windows, Linux, macOS |
| ProcessSelfDeleted | This event indicates when a process self-delete situation is detected. It will be thrown when a proc... | Windows, macOS, Linux |
| FlashThreadCreateProcess | Thread associated with Flash activity created a process. | Windows, macOS |
| EndOfProcess | When a process that’s running on a host finishes, the sensor will count all of the events that were ... | Windows, macOS, Linux, Falcon Container |
| CommandHistory | This event includes the full command history associated with one of the consoles in a process that h... | Windows |
| BehaviorWhitelisted | Indicates that a behavior has been whitelisted. | Windows, macOS, Linux |
| UserLogonFailed | This event is generated when a user logon fails. | Windows |
| FalconHostRegTamperingInfo | An event that describes the registry event that triggered a Falcon sensor tampering indicator. | Windows |
| FalconHostFileTamperingInfo | An event that describes the file event that triggered a Falcon sensor tampering indicator. | Windows |
| ScriptControlErrorEvent | An event that contains telemetry data containing up to 56 KB ScriptContent field data from AMSI (Ant... | Windows |
| SuspiciousRegAsepUpdate | An event that describes the registry activity that triggered a suspicious registry ASEP (Autostart E... | Windows |
| NetworkModuleLoadAttempt | An event that indicates that a process whose primary image was not on a network attempted to load a ... | Windows |
| RemovableDiskModuleLoadAttempt | An event that indicates that a process with a primary image that is not on a removable disk attempte... | Windows |
| SuspiciousEseFileWritten | This event indicates that a possible domain credential file (NTDS.dit) was copied from a volume snap... | Windows |
| FileDeleteInfo | This event is generated when a file deletion for a full file occurs. ADS deletions are not currently... | Windows, macOS, Linux |
| SystemTokenStolen | An event that indicates that system token stealing was detected. | Windows |
| LowILModuleLoadAttempt | An event that indicates that a non-LowIL process attempted to load an untrusted LowIL module. | Windows |
| ImageHash | This event is generated for each DLL or executable loaded into a process’ memory. | macOS, Linux, Falcon Container, Windows |
| TerminateProcess | This event is thrown when a process exits normally or is forcibly terminated. | macOS, Linux, Falcon Container, Windows, ChromeOS |
| ProcessActivitySummary | A rollup event created when a process terminates. Includes statistical information about what a proc... | macOS, Windows |
| KextLoad | Signals a Kernel Extension (KEXT) Load, triggered via a MAC hook. | macOS |
| KextUnload | Signals a Kernel Extension (KEXT) Unload, triggered via a MAC hook. | macOS |
| DirectoryCreate | This event is generated when a process creates a new folder. | macOS, Windows, Linux |
| SyntheticProcessRollup2 | This event provides data similar to what is available in a ProcessRollup2. SyntheticProcessRollup2 e... | macOS, Windows, Linux, Falcon Container, ChromeOS |
| CriticalFileAccessed | A critical file was accessed. | macOS, Linux, Falcon Container, ChromeOS |
| CriticalFileModified | A critical file was modified. | macOS, Linux, Falcon Container, ChromeOS |
| PtyCreated | An event that notifies that a pty has been created. | macOS |
| FileOpenInfo | This event is generated when a file is opened by a process. | macOS, Linux, Falcon Container, Windows |
| FirewallDisabled | An event that is sent from the sensor when packet filter is disabled. | macOS |
| FirewallEnabled | An event that is sent from the sensor when packet filter is enabled. | macOS |
| FileCreateInfo | This event is generated when a file is created by a process. | macOS, Linux, Falcon Container, Windows, Linux, Falcon Container, Windows, macOS, Windows Legacy |
| CriticalEnvironmentVariableChanged | A process set a critical environment variable. | Linux, Falcon Container |
| FileDeleted | This event is generated when a file deletion for a full file occurs. ADS deletions are not currently... | Android, Windows, Forensics |
| ProcessRollup2 | This event (often called "PR2" for short) is generated for a process that is running or has finished... | Android, Linux, Falcon Container, ChromeOS, Forensics, Windows Legacy, macOS, Windows |
| ReflectiveDllLoaded | An event that indicates that a user space thread reflectively loaded DLL. | Windows, Windows |
| ProtectVmEtw | A virtual memory protect event generated from ETW data. | Windows |
| ProcessWitness | Emitted when the sensor witnesses a process is running. This event is not an indication that a proce... | iOS |
| ClipboardPaste | Sent when content is pasted from the clipboard. Fields: Android | Android |
| AndroidIntentSentIPC | This event is sent when an Android Intent is fired from the container Fields: Android | Android |
| MobileOsIntegrityStatus | Describes the integrity of the mobile OS (eg. jailbroken/rooted) | iOS, Android |
| JarFileWritten | This event is generated when a Java executable archive (.jar) file type is written to disk. Fields: ... | Android, Windows, macOS, Linux |
| RegGenericValueUpdate | An event that indicates that a registry value has been updated. | Windows |
| ScreenshotTakenEtw | An event that indicates that partial or full screenshot has been taken. Captured using the ETW consu... | Windows |
| SetWinEventHookEtw | An event that indicates that an application called the SetWinEventHook API. Captured using the ETW c... | Windows |
| RegSystemConfigValueUpdate | An event that indicates that a registry value related to system configuration or security has been u... | Windows |
| SetThreadCtxEtw |  | Windows |
| RegisterRawInputDevicesEtw | An event that indicates that an application called the RegisterRawInputDevices API. Captured using t... | Windows |
| QueueApcEtw |  | Windows |
| SmbClientNamedPipeConnectEtw | An event that indicates when a machine connects to a remote SMB (Server Message Block) named pipe. T... | Windows, Windows |
| ProcessExecOnSMBFile | An event that contains telemetry data emitted on execution of a PE file which was written by SMB. | Windows |
| TokenImpersonated | An event that contains detailed before and after impersonation information for detection telemetry. | Windows |
| SetWindowsHookExEtw | An event that indicates that an application called SetWinEventHookEx API. Captured using the ETW con... | Windows |
| WmiProviderRegistrationEtw | An event that is emitted when a WMI (Windows Management Instrumentation) provider gets registered. C... | Windows |
| MobileDetection | An event that's sent by the sensor when a sensor-level detection occurs. Fields: Android, iOS | Android, iOS |
| DexFileWritten | Emitted when a file has been written that contains a real Dex image header. Fields: Android | Android |
| DeveloperOptionsStatus | An event that contains info about developer-related settings on the device. Fields: Android, iOS | Android, iOS |
| SELinuxStatus | An event that contains info about the SELinus status. Fields: Android | Android |
| StorageEncryptionStatus | An event that contains information about the Device Storage encryption. Fields: Android | Android |
| LockScreenStatus | An event that contains info about the device lock screen mechanism. Fields: Android, iOS | Android, iOS |
| SystemPartitionStatus | An event that contains information about the device system partition. This event is deprecated as of... | Android |
| SafetyNetCompatibilityStatus | An event that contains the SafetyNet compatibility status obtained via the Google SafetyNet API. Fie... | Android |
| DnsRequestResult | An event that contains DNS request results after a DNS request. Fields: Android, iOS | Android, iOS |
| FileSystemAttributesStatus | An event that contains info about the Filesystem attributes of the device. | iOS |
| DebuggableFlagTurnedOn | An event that indicates a debuggable flag has been turned on for a non-dev build of an app. Fields: ... | Android |
| BootLoaderStatus | An event that contains info about the device's bootloader. Fields: Android | Android |
| HarmfulAppData | An event that contains the name, hash, and category of the harmful app. Fields: Android | Android |
| DuplicateInstallFromPlayStore | An event that indicates a containerized app is also installed outside the container. Fields: Android | Android, Windows |
| ScriptControlScanInfo |  | Windows, macOS, Linux |
| ObjCRuntimeAltered | An event that indicates an Obj-C method has been tampered with. MethodSignature indicates which Obj-... | iOS |
| UnexpectedDynamicLibraryLoaded | An event that indicates that an unexpected dynamic library was loaded at runtime. | iOS |
| UnexpectedFileFound | An event that indicates a file that should not exist on the device has been found. An event that ind... | iOS, Android |
| TrampolineDetected | An event that indicates a C function has been tampered with. In iOS jailbreak, functions are modifie... | iOS |
| CertificatePinningCompromised | An event that indicates that the certificate pinning methods/functions on the device have been tampe... | iOS |
| ProcessTokenStolen | An event that describes a process token stealing detection. ContextProcessId has been detected steal... | Windows |
| DebuggedState | An event that indicates a process is in the state of being debugged (i.e., has a debugger attached t... | iOS |
| PathUnexpectedlyReadable | An event that indicates a system file or directory can be opened for reading. On a non-jailbroken sy... | iOS |
| UnexpectedEnvironmentVariable | An event that indicates some dangerous environment variables have made it to the app at runtime. | iOS |
| CodeSigningAltered | An event that indicates the code signing flags of the current application have unexpected flags or a... | iOS |
| SafetyNetCheckFailed | An event that indicates the SafetyNet check could not be completed. Fields: Android | Android |
| SystemPartitionAltered | An event that indicates a system partition has been altered and is in an unexpected state. | iOS |
| InstallFromUnknownSourcesStatus | An event that contains info about third-party app installers on Android. Fields: Android | Android |
| RemoteBruteForceDetectInfo | An event that describes a remote brute force detection. | Windows |
| SensitiveWmiQuery | An event that indicates that a client process executed a sensitive WMI query. | Windows |
| DCSyncAttempted | Directory Services changes were replicated. If the source host is not a Domain Controller, this coul... | Windows |
| RemediationMonitorRegistryRemoval | Notification of a registry persistence removal remediation action that would have been attempted by ... | Windows |
| ThreadBlocked | Reports the status of a block thread attempt. | Windows |
| VerifyAppsDisabled | This event has been deprecated. Fields: Android | Android |
| DNSRequestDetectInfo | This event is sent whenever a malicious DnsRequest is detected. Fields: Android, iOS | Android, iOS, Linux |
| DnsRequestBlocked | This event is sent whenever a DnsRequest is blocked. Connection to either the IP or the domain in th... | Android, iOS |
| UserSetProcessBreakOnTermination |  | Windows |
| SuspiciousPrivilegedProcessHandle | Indicates a process has opened a handle to a privileged process with special access rights. | Windows |
| FileWrittenAndExecutedInContainer | A file was written and later executed in a container. | Linux, Falcon Container |
| DwmCompositionResourceExploitAttempt |  | Windows |
| GenericFileWritten | An event that is emitted when a process is done writing to a file that doesn't match a more specific... | macOS, Windows |
| RemediationMonitorScheduledTaskRemoval | Notification of a scheduled task persistence removal remediation action that would have been attempt... | Windows |
| ReflectiveDotnetModuleLoad | Event generated when .NET module is reflectively (e.g. from a byte array) loaded in a process. | Windows |
| HookedAndroidMethodFound | An event that indicates that a hooking framework such as Xposed has been found to have been loaded b... | Android |
| SuspiciousAndroidStackTraceElementFound | An event that indicates that a hooking framework has been found via stacktrace analysis and that the... | Android |
| SuspiciousAndroidActivityFound | An event that indicates that a currently installed application on the device has been found providin... | Android |
| SuspiciousAndroidSystemPropertyFound | An event that indicates that a suspicious system property has been found. This might indicate the OS... | Android |
| SuspiciousAppFound | An event that indicates that a suspicious application has been found to be installed on the device. ... | Android |
| SuspiciousAndroidLogcatMessageFound | An event that indicates that an application log message originating from a suspicious source has bee... | Android |
| NtfsQueryEaExploitAttempt |  | Windows |
| NewExecutableWritten | This event is generated when an executable file extension is written, whether or not it is truly an ... | Linux, macOS, Windows |
| RemediationMonitorServiceRemoval | Notification of a service persistence removal remediation action that would have been attempted by t... | Windows |
| AndroidInitServiceRemoved | An event that indicates that an init (boot) service has been removed from the system configuration. ... | Android |
| AndroidInitServiceAdded | An event that indicates that a new init (boot) service has been added to the system configuration. T... | Android |
| SystemUpdatesBlockedByDNS | Indicates that OS updates have been blocked via DNS. | iOS |
| SystemUpdatesBlockedByHTTP | Indicates that OS updates have been blocked via HTTP. | iOS |
| SystemUpdatesBlockedByFilesystem | Indicates that OS updates have been blocked via the filesystem. | iOS |
| ProcessExecOnRDPFile | A PE file was written and executed from an RDP session. | Windows |
| SafetyNetVerifyAppsStatus | An event that contains information about the status of SafetyNet Verify Apps (Google Play Protect) o... | Android |
| MemoryProtectionUpdated | Triggers if a new executable memory region is mapped which is writable or mapped from a file. | Linux, Falcon Container |
| NamespaceChanged |  | Linux, Falcon Container |
| ProcessSessionCreated |  | Linux, Falcon Container |
| FileSetMode | Indicates the file permissions have been modified via chmod/fchmod/fchmodat. | Linux, Falcon Container |
| BMLFeatureData |  | Windows, macOS, Linux, Falcon Container |
| HostTimeModified |  | Linux, Falcon Container |
| KernelServiceStarted | Indicated that a kernel service was started locally or remotely. | Windows |
| RootkitDetectionResponse |  | Windows |
| MbrOverwriteRawDetectInfo |  | Windows |
| RegCredAccessDetectInfo |  | Windows |
| SourceCodeFileWritten |  | Windows, macOS |
| ArchiveFileContent |  | Windows, macOS |
| UnixFileWritten | Fields: Android | Android |
| ScheduledTaskTamperingRegistryOperation |  | Windows |
| ScriptFileWrittenInfo |  | Windows |
| SmtpEmailMessage |  | Windows |
| SessionPatternTelemetry |  | Linux, macOS |
| PacketFilterAttached |  | Linux, Windows, Linux |
| FileStatFsInfo |  | Linux |
| UnixName |  | Linux |
| Pop3Command |  | Windows, Linux |
| ThreadPreviousModeMismatch |  | Windows |
| SigningIdentity |  | iOS |
| ProcessTokenPrivilegesEdited |  | Windows |
| SensorTampering | Thrown when a tampering event occurs on the sensor. | Linux, Android |
| MobileOsForensicsReport |  | iOS, Android |
| IntrusivePackageDiscovered | Fields: Android | Android |
| IntrusiveProcessDiscovered |  | iOS |
| MotwWritten |  | Windows |
| SignInfoWithContext | Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains... | Windows, macOS |
| SuspiciousCredentialModuleLoad | An indicator event fired when suspicious credential module activity is detected, which means the pro... | Windows |
| SignInfoWithCertAndContext | Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains... | macOS, Windows |
| InjectedThreadFromUnsignedModule | This event contains information about a thread that was injected into a process from an unsigned mod... | Windows |
| SuspiciousRawDiskReadFromUnsignedModule | This event contains information about an unsigned module reading a target file using raw disk access... | Windows |
| FileIntegrityMonitorRuleMatched | An event that contains data about a change to a directory, file, or registry key. Used with the File... | macOS, Windows, Linux |
| MacroContentInfo | Description: Provides information about a macro extracted when an Office file is written or opened | Windows |
| SensorSettingsUpdate |  | Windows, macOS |
| IdpConnectionsOverloadNotification | IDP Traffic Inspection detected more than 15,000 concurrent connections in active enforcement mode. | Windows |
| ProcessTreeCompositionPatternTelemetry |  | Windows |
| K8SAdmissionReviewResult | Fields: Kubernetes | Kubernetes |
| K8SAdmissionReviewResultPrime | Fields: Public Cloud | Public Cloud |
| RemoteCommandResponse |  | Linux, Windows, macOS |
| ProcessRollup2Stats | Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only... | Linux, Falcon Container, macOS |
| SuspiciousLackOfProcessRollupEvents | This event is emitted if we don't see any ProcessRollup2 events for a long time. | Windows |
| AgentConnect | This event is generated when the sensor successfully connects to the cloud. | Windows Legacy, Windows, Linux, Falcon Container, Kubernetes, macOS, Android, iOS, Windows Legacy, Vmcluster, iOS, Linux, Falcon Container, Android, Kubernetes, macOS, Windows |
| IsoExtensionFileWritten |  | Windows |
| ImgExtensionFileWritten |  | Windows |
| DcBluetoothDeviceConnectedDetails |  | Windows, macOS |
| FirmwareImageAnalyzed | Indicates that analysis of a firmware image was completed. | Windows, macOS |
| DirectoryTraversalOverSMB | This event indicates Directory traversal over an SMB session detected. | Windows |
| CrashNotification | The sensor sends this to the cloud when the Diagnostics Actor notices that the machine has booted wi... | macOS, Windows |
| OciContainerComplianceInfo |  | Linux, Falcon Container |
| IdpDcPerfReport | This event reports Domain Controller performance counter. | Windows |
| FileRenameInfo | This event is generated when a file is renamed. Only sent as part of a detection. | Linux, Falcon Container, macOS, Windows |
| SensorSelfDiagnosticTelemetry |  | Windows, Linux, macOS |
| SpotlightEntityBatch | Single Event consisting of a list of Spotlight Entity State data packaged for optimal size and part ... | Linux, Windows, macOS |
| CustomIOADomainNameDetectionInfoEvent | An event triggered by a Domain Name custom IOA rule. | Windows, macOS, Linux |
| CustomIOAFileWrittenDetectionInfoEvent | An event triggered by a File Creation custom IOA rule. | Windows, macOS, Linux |
| CustomIOABasicProcessDetectionInfoEvent | An event triggered by a Process Creation custom IOA rule. | Windows, Linux, Falcon Container, macOS |
| CustomIOANetworkConnectionDetectionInfoEvent | An event triggered by a Network Connection custom IOA rule. | Windows, macOS, Linux |
| RegistryOperationBlocked | An event that indicates that a registry operation has been blocked using a callback filter. | Windows |
| RegistryOperationDetectInfo | An event that describes a registry operation blocked using a callback filter. | Windows |
| MacroDetectInfo | Event description: Provides more context around the macro content that was detected. | Windows |
| UmppcDetectInfo | An event that describes a UMPPC-based detection. | Windows |
| SnapshotVolumeMounted | Information about a snapshot volume that was just mounted. | Windows |
| ImpersonationTokenInfo | ImpersonationTokenInfo represents a security context for a general impersonation activity. Each Impe... | Windows |
| UserIdentity | The UserIdentity event is generated when a user logs in to a host. It conveys important security-rel... | macOS, Windows, Forensics, Linux |
| DriverLoad | An event to notify of a driver load that will be used for detection. Fields: Forensics | Forensics, Windows |
| UserAccountDeleted | User account deleted. This event is generated when a user account is deleted. The data will indicate... | Forensics, Windows, Linux |
| ProcessTrace |  | Linux, Falcon Container |
| InstanceMetadata | Metadata information about the instance on which the sensor is running. | macOS, Kubernetes, Windows, Linux, Falcon Container |
| FileAccessOperationOverSMB | File access operations over a SMB user session. | Windows |
| K8SSnapshot | Fields: Kubernetes | Kubernetes |
| K8SWatchStarted | Fields: Kubernetes | Kubernetes |
| K8SResource | Fields: Kubernetes | Kubernetes |
| K8SWatchStopped | Fields: Kubernetes | Kubernetes |
| IdpEntityRiskScoreChange | Fields: Public Cloud | Public Cloud |
| HostedServiceStarted | This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is star... | Windows |
| NetShareAdd | This event is generated when a network share is added or modified on a host. | Windows |
| UserAccountCreated | This event is generated when a new user account is created. The data will indicate the initial proce... | Windows, Linux |
| ServiceStarted | This event is generated when a standalone service is started by the service control manager (SCM). S... | Windows |
| ScheduledTaskDeleted | This event is sent when Falcon has detected that a scheduled task has been removed from the machine.... | Windows |
| FirewallSetRule | A firewall rule has been created or modified, such as a rule allowing inbound RDP connections. The d... | Windows |
| FirewallDeleteRule | A firewall rule has been deleted, such as removing a rule preventing inbound RDP connections. The da... | Windows |
| FirewallChangeOption | A firewall configuration option has been changed, such as enabling or disabling the firewall. The da... | Windows |
| UserAccountAddedToGroup | This event is generated when an existing user account is added to an existing group. The data will i... | Windows, Linux |
| BITSJobCreated | The event is generated when a Background Intelligent Transfer Service (BITS) download is created and... | Windows |
| EventLogCleared | This event is generated when a Windows event log is cleared. | Windows |
| ScheduledTaskRegistered | This event is sent when Falcon detects that a scheduled task has been added to the machine, either l... | Windows |
| NetShareDelete | This event is generated when a network share is removed from a host. | Windows |
| NetShareSecurityModify | This event is generated when the security descriptor of a network share is changed. | Windows |
| VolumeSnapshotCreated | A volume snapshot has been created. | Windows |
| VolumeSnapshotDeleted | A volume snapshot has been deleted. | Windows |
| VolumeSnapshotOperationBlocked | Event describing a snapshot volume block operation. IFN and CL are based upon the RpcProcessId, in V... | Windows, Windows |
| MemoryScanErrorEvent |  | Windows |
| ServiceStopped | This event is emitted when a standalone service is stopped by the service control manager (SCM). Unf... | Windows |
| SuspiciousPeFileWritten | A suspicious PE image file was written to disk. | Windows |
| PodInfo | Metadata associated with a Kubernetes pod. | Linux, Falcon Container |
| DmpFileWritten | Emitted when a process is done writing a dump file. PidFromCommandLine will be enhanced in some case... | Windows, macOS, Linux |
| SevenZipFileWritten | This event is generated when a 7ZIP file type (.7zip) is written to disk. | Windows, macOS, Linux |
| PdfFileWritten | This event is generated when a PDF file type (.pdf) is written to disk. | Windows, macOS, Linux |
| OleFileWritten | This event is generated when a file a Microsoft Office (Pre-Office 2007) file type is written to dis... | Windows, macOS, Linux |
| RarFileWritten | Emitted when a process is done writing a RAR file. | Windows, macOS, Linux |
| OoxmlFileWritten | This event is generated when a Microsoft Office (Post-Office 2007) file type is written to disk. | Windows, macOS, Linux |
| ZipFileWritten | This event is generated when a ZIP file type (.zip) is written to disk. | Windows, macOS, Linux |
| RtfFileWritten | Emitted when a process is done writing an RTF file. | Windows, macOS, Linux |
| PeFileWritten | This event is generated when a Windows Portable Executable file type is written to disk. The differe... | macOS, Linux, Windows |
| XarFileWritten | Emitted when a process is done writing a Xar file. macOS installer files are of this type. | Windows, macOS, Linux |
| BZip2FileWritten | Emitted when a process is done writing a BZip2 file. | Windows, macOS, Linux |
| MachOFileWritten | Emitted when a process is done writing a MachO file. | Windows, macOS, Linux, Windows, macOS, Linux |
| IdwFileWritten | Emitted when a process is done writing an IDW file. | Windows |
| DwgFileWritten | An event that is emitted when a process is done writing to a DWG file. | Windows |
| ELFFileWritten | Emitted when a file has been written that contains a real ELF image header. | Windows, macOS, Android, Linux |
| GzipFileWritten | Emitted when a file has been written that contains a real Gzip image header. | Windows, macOS, Linux |
| JavaClassFileWritten | Emitted when a process is done writing a Java Class file. | Windows, macOS, Linux |
| CabFileWritten | Emitted when a process is done writing a Microsoft Cabinet (CAB) file. | macOS, Windows, Linux |
| ArcFileWritten | Emitted when a process is done writing a ARC file. | Windows, macOS, Linux |
| TiffFileWritten |  | Windows, macOS, Linux |
| ArjFileWritten | Emitted when a process is done writing a ARJ file. | macOS, Windows, Linux |
| VmdkFileWritten |  | Windows, macOS, Linux |
| JpegFileWritten | Emitted when a process is done writing a Jpeg image file. | Windows, macOS, Linux |
| BmpFileWritten | Emitted when a process is done writing a BMP image file. | Windows, macOS, Linux |
| GifFileWritten | Emitted when a process is done writing a GIF image file. | macOS, Windows, Linux |
| PngFileWritten |  | macOS, Windows, Linux |
| MSXlsxFileWritten |  | Windows, macOS, Linux |
| MSPptxFileWritten |  | Windows, macOS, Linux |
| VdiFileWritten |  | Windows, macOS, Linux |
| MSDocxFileWritten |  | Windows, macOS, Linux |
| MSVsdxFileWritten |  | macOS, Windows, Linux |
| DxfFileWritten |  | Windows, Windows |
| RpmFileWritten |  | Windows, macOS, Linux |
| DebFileWritten |  | Windows, macOS, Linux |
| BlfFileWritten | Emitted when a process is done writing an BLF file. | macOS, Windows, Linux |
| MsiFileWritten |  | Windows, macOS, Linux |
| LnkFileWritten |  | Windows, macOS, Linux |
| DmgFileWritten |  | Windows, macOS, Linux |
| EmailFileWritten |  | Windows, macOS, Linux |
| EmailArchiveFileWritten |  | macOS |
| EseFileWritten |  | macOS, Windows, Linux |
| RegistryHiveFileWritten |  | Windows |
| ADExplorerFileWritten |  | Windows |
| WebScriptFileWritten |  | Windows, macOS, Linux |
| CrxFileWritten |  | Windows, macOS, Linux |
| PythonFileWritten |  | Windows |
| HttpRequestDetect | An event that indicates a detection on an HTTP(S) request. | Windows |
| HttpRequest |  | Linux, macOS |
| DcBluetoothDeviceProperties | This event contains properties for a connected Bluetooth device. | macOS, Windows |
| IdpCloudHealthStatus |  | Windows |
| DiskCapacity | An event that contains information about disks, the quantity of disks, and the storage capability of... | Windows, Linux |
| MemoryMapped | Triggers when an executable memory region is mapped. | Linux, Falcon Container |
| TlsClientHello |  | Windows, Linux, macOS |
| SmtpAttachment |  | Linux |
| SmtpCommand |  | Linux |
| FtpCommand |  | Linux |
| NetworkLinkConfigGetLink |  | Linux |
| NetworkLinkConfigGetAddress |  | Linux |
| RansomwareFileAccessPattern | Helper event for ransomware file access patterns. | Windows |
| AsepFileChangeScanInfo | Rollup indicating an ASEP file has been created or modified but there was no template detection on t... | macOS, macOS |
| BPFCommandIssued | Emitted when a process executes bpf syscall. | Linux, Falcon Container |
| FileSystemOperationBlocked | An event that indicates that a file system operation has been blocked. | macOS, Windows |
| SecureTrafficDecrypted | An event that contains certificate info for the compromised network connection. Fields: Android, iOS | Android, iOS |
| FileSystemOperationDetectInfo | Informational event for a file system operation detection. | Windows |
| ModuleBlockedEventWithPatternId | This event adds a potential reason for blocking (as a PatternId) to module blocking information. | macOS, Linux, Falcon Container, Windows |
| ModuleBlockedEvent | This event is sent to inform cloud about the fact that given module (identified by hash) was blocked... | macOS, Windows, Linux, Falcon Container |
| ChannelVersionRequired | This event informs the cloud information about the state of a channel on the sensor. The cloud will ... | Windows, macOS, Linux, Falcon Container, Android, Kubernetes, Vmcluster, iOS |
| LfoUploadDataUnneeded | Emitted when the sensor initiates a file upload, but the cloud has determined the file is not needed... | Windows, macOS, Linux, Android, Kubernetes, Vmcluster |
| LfoUploadDataComplete | Emitted when the LFOUploadActor has successfully uploaded a file to the cloud. | Windows, macOS, Linux, Android, Kubernetes, Vmcluster |
| LfoUploadDataFailed | Emitted when the sensor has detected error(s) and has decided not to stop uploading a file to the cl... | Windows, macOS, Linux, Android, Kubernetes, Vmcluster |
| ProvisioningChannelVersionRequired | This event informs the cloud about the state of a channel on the sensor during provisioning. It is o... | Linux, Falcon Container, macOS, Windows, iOS, Android |
| LfoUploadStart | Emitted when the sensor initiates a file upload. | Windows, macOS, Linux, Android, Kubernetes, Vmcluster |
| NetworkListenIP4 | This event is generated when an application establishes a socket in listening mode This event is gen... | Windows, macOS, Android, Linux, Falcon Container, Forensics, ChromeOS |
| NetworkConnectIP6 | This event is created whenever an application using a connection-oriented protocol attempts a remote... | Windows, macOS, Android, iOS, Forensics, ChromeOS, Linux, Falcon Container |
| NetworkReceiveAcceptIP4 | This event is generated when an application using a connection-oriented protocol attempts to accept ... | Windows, macOS, Android, Linux, Falcon Container, Forensics |
| NetworkReceiveAcceptIP6 | This event is created whenever an application using a connection-oriented protocol attempts to accep... | Windows, macOS, Android, Linux, Falcon Container, Forensics |
| NetworkCloseIP4 | An event that is generated by an application using a connection-oriented or connectionless protocol ... | Windows, Android, Forensics, macOS, Linux, Falcon Container |
| NetworkConnectIP4 | This event is generated when an application attempts a remote connection. | Windows, macOS, Android, iOS, Linux, Falcon Container, Forensics, ChromeOS |
| NetworkListenIP6 | This event is created whenever an application using a connection-oriented protocol establishes a soc... | Windows, macOS, Android, Linux, Falcon Container, Forensics, ChromeOS |
| FirewallSetRuleIP6 | An event that indicates an IPv6 firewall rule has been created. The field 'IsUnique' will be TRUE if... | macOS |
| FirewallDeleteRuleIP4 | An event that notifies that an Ipv4 firewall rule has been deleted. The field 'IsUnique' will be TRU... | macOS |
| FirewallDeleteRuleIP6 | An event that notifies that an Ipv6 firewall rule has been deleted. The field 'IsUnique' will be TRU... | macOS |
| FirewallSetRuleIP4 | An event that indicates an IPv4 firewall rule has been created. The field 'IsUnique' will be TRUE if... | macOS |
| NetworkCloseIP6 | An event that is generated by an application using a connection-oriented or connectionless protocol ... | Linux, Falcon Container, Windows, Forensics, macOS, Android |
| NetworkConnectIP4Blocked | This event is created whenever a NetworkConnectIP4 event is blocked. This event is created whenever ... | Windows, Android, macOS, iOS |
| NetworkConnectIP6Blocked | This event is created whenever a NetworkConnectIP6 event is blocked. This event is created whenever ... | Android, Windows, macOS, iOS |
| NetworkConnectIP4DetectInfo | This event is sent whenever a connection to malicious IP4 address is detected. Fields: Android | Android, iOS |
| NetworkConnectIP6DetectInfo | This event is sent whenever a connection to malicious IP6 address is detected. Fields: Android | Android, iOS |
| RemediationActionKillIP4Connection | Sensor attempted to kill a connection to a malicious IPv4 address. No further data will be sent or r... | Android, iOS |
| RemediationActionKillIP6Connection | Sensor attempted to kill a connection to a malicious IPv6 address. No further data will be sent or r... | Android, iOS |
| CreateSocket | This event is created whenever a process creates a socket. | Linux, Falcon Container, Forensics |
| NetworkOutboundPortScanDetectInfo |  | Windows |
| RawBindIP6 | IPv6 network binding event. Terminating socket is in raw mode. An event that is created when an appl... | Forensics, Linux, Falcon Container, Android, macOS, Windows |
| RawBindIP4 | IPv4 network binding event. Terminating socket is in raw mode. An event that is created when an appl... | Forensics, Android, Windows, macOS, Linux, Falcon Container |
| NewScriptWritten | Emitted when a process is done writing a script file, as determined by #! at the start of the file. ... | Linux, macOS, Windows |
| PatternHandlingError | This event is emitted when an error occurs in processing a behavior. | Windows, macOS, Linux, Falcon Container |
| ProcessPatternTelemetry |  | Windows, macOS, Linux |
| ActiveDirectoryIncomingPsExecExecution2 | Indicates remote code execution on a domain controller using PsExec. This event is generated based o... | Windows |
| IdpPolicyAlertRuleMatch | Fields: Public Cloud | Public Cloud |
| BrowserInjectedThread | Indicates a browser process injected a thread into some other process. | Windows |
| KernelCallbackTableUpdate | An event that indicates that the ProcessEnvironmentBlock KernelCallbackTable field has been changed ... | Windows, Windows |
| FileDetectInfo |  | Linux, macOS, Windows |
| IdpPolicyFederatedAccessRuleMatch | Fields: Public Cloud | Public Cloud |
| BootLoopProtectionTelemetry |  | Windows |
| LightningUnresponsiveStatus |  | Windows, macOS |
| AndroidEnterpriseInfo | This event contains metadata related to the state of the device as reported by the Android Managemen... | Android |
| InjectedThread | This event is generated when one process injects an execution thread into another process. While oft... | Windows |
| JavaInjectedThread | This event is generated when Java injects a thread into another process. | Windows |
| DocumentProgramInjectedThread | Indicates a document program process injected a thread into some other process. | Windows |
| ActiveDirectoryAuthenticationFailure | Indicates that the Domain Controller handled one or more failed authentications by an account on an ... | Windows |
| ActiveDirectoryInteractiveDomainLogon | Indicates an interactive logon to an Active Directry domain handled by a Domain Controller. The inte... | Windows |
| SetWindowsHook | An event that is sent from the sensor when a user mode program attempts to set a windows hook. | Windows |
| ScriptControlDetectInfo | This event is sent when Falcon has detected malicious script content being executed on the host. Thi... | macOS, Linux, Windows |
| ActiveDirectoryAuthentication | Indicates that the Domain Controller handled one or more successful authentications by an account on... | Windows |
| ActiveDirectoryServiceAccessRequestFailure | Indicates that the Domain Controller handled one or more failed service requests from an account on ... | Windows |
| CloudAssociateTreeIdWithRoot | This event is generated when there is a detection in the CrowdStrike cloud. This event has a data fi... | Windows, Linux, Falcon Container, macOS, ChromeOS |
| K8SProductConfig | Fields: Kubernetes | Kubernetes |
| IdpTelemetryData |  | Windows |
| IdpPacketDiversionLdapsConnectionsOverloadNotification |  | Windows |
| DataProtectionArchiveAssessed | Describes an archive processed by Data Protection assessment. Top level event fields are properties ... | Windows, macOS |
| FileTimestampsModified | An event that is emitted when a change occurs to the timestamps of a file. | Windows, Linux, Falcon Container |
| VMClusterInfo | Event sent periodically to let the cloud know that the sensor is running with the following VM clust... | Vmcluster |
| VmcSensorStatus | This event is sent to provide VMC sensor operational status. Fields: Vmcluster | Vmcluster |
| VmcVmAsset | This event is sent to provide VMware vCenter VM information. Fields: Vmcluster | Vmcluster, Windows |
| InboundHttpParsingStatus |  | Windows, macOS, Linux |
| InstalledBrowserExtension | An event that contains information about installed browser extensions, including updates and removal... | Windows, macOS |
| BrowserExtensionStatus |  | macOS, Windows, macOS, Linux, Falcon Container, Windows Legacy |
| AssociateIndicator | This event is generated when the sensor generates an indicator. An indicator is like a detection eve... | Windows, Linux, Falcon Container, macOS |
| FirewallRuleIP6Matched | An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations ... | Windows, macOS, Linux |
| FirewallRuleIP4Matched | An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations ... | Windows, macOS, Linux |
| NamedMutantHandleClosedTelemetry | An event that indicates that a process closed a handle to a known bad named mutex. | Windows, Windows |
| ProcessControl |  | Linux, Falcon Container |
| ClassifiedModuleLoad | The ClassifiedModuleLoad event provides information about a module which has been loaded into a proc... | Windows |
| ProcessExecOnPackedExecutable | An event that contains telemetry data emitted on execution of a PE file which is known to be packed.... | Windows |
| IdpCloudHealthConfigurationsGetResponse |  | Windows |
| ModuleDetectInfo | This event identifies a scenario that would be a blocking prevention if more rigorous settings were ... | macOS, Linux, Falcon Container, Windows |
| AppSideLoaded | An event that contains the package name and installer info of the app that has been installed outsid... | Android |
| MobileAppIdentifiers | An event that describes details about a mobile application package. Fields: Android | Android |
| RegValueQueryDetectInfo |  | Windows |
| WmiQueryDetectInfo |  | Windows |
| DriverLoadedV2DetectInfo |  | Windows, Windows |
| DotnetModuleLoadDetectInfo |  | Windows |
| PtTelemetry |  | Windows |
| ModuleLoadV3DetectInfo | Additional information for detections from the Module Load V3 template. | Windows |
| IdpDcTiConfiguration |  | Windows |
| SmbServerShareOpenedEtw | An event that indicates a remote machine opening a local share. This event is supported on all Windo... | Windows |
| IdpWatchdogRemediationActionTaken |  | Windows |
| IdpWatchdogRemediationActionTakenForMemory |  | Windows |
| DBusMessage | An event that generates telemetry that provides visibility into D-Bus messages flowing over local Un... | Linux |
| FirewallRuleIP4 | Fields: Forensics | Forensics |
| InboundHttpHeader |  | Linux, macOS, Windows |
| InternetExposureData |  | macOS, Linux, Windows |
| SyntheticSystemdServiceCreated |  | Linux |
| SystemdTimerDeleted |  | Linux |
| RouteIP6 | IPv6 Route entry. Fields: Forensics | Forensics |
| DnsServer | DNS server IP addresses. Fields: Forensics | Forensics |
| BrowserProxyInfo | Browser proxy information. Fields: Forensics | Forensics |
| SpotlightSearchEntry | Per-user spotlight search information. Fields: Forensics | Forensics |
| RegSystemConfigKeyUpdate |  | Windows |
| SudoCommandAttempt |  | macOS |
| NamedPipeDetectInfo | Named pipe detect telemetry event | Windows |
| NetworkEndPointDataUsage | This event has total counts of sent/received octets/packets to/from the network-attached end point d... | Forensics |
| UsbDeviceInfo | Information on each USB device attachment. Fields: Forensics | Forensics |
| UserAccountRemovedFromGroup |  | Linux, Windows |
| SensorEnteredSafemode |  | macOS, Linux, Falcon Container, Windows |
| PtyDetached |  | Linux |
| SystemdServiceCreated |  | Linux |
| IdpCloudHealthCheck |  | Windows |
| SmbServerLocalNamedPipeOpenedEtw |  | Windows |
| OpenDirectoryAttributeSet |  | macOS |
| OpenDirectoryAttributeRemove |  | macOS |
| RegGenericKeyUpdate |  | Windows |
| TerminalSavedStateInfo | MacOS terminal saved state information. Fields: Forensics | Forensics |
| OpenDirectoryAttributeAdd |  | macOS |
| OpenDirectoryGroupSet |  | macOS |
| ActiveDirectoryAuditGpoModified |  | Windows |
| FirewallRuleIP6 | Fields: Forensics | Forensics |
| KernelParameter | Fields: Forensics | Forensics |
| UserGroupCreated |  | Linux |
| SystemdServiceDeleted |  | Linux |
| ScheduledTaskInfo | Scheduled windows tasks. Fields: Forensics | Forensics |
| ProcessDataUsage | Measurements and statistics of data traffic sent and received to/from the target process. Fields: Fo... | Forensics |
| WSLVMStopping | The Linux Virtual Machine Root Namespace is stopping. | Windows |
| SyntheticSystemdTimerCreated |  | Linux, Windows |
| NetShareInfo | Shared resource information. Fields: Forensics | Forensics |
| OsUpdateTimestamp | Operating system update timestamp. Fields: Forensics | Forensics |
| NetworkDnsSuffix | A network suffix name in the configured DNS suffix list. Fields: Forensics | Forensics |
| NetworkHostsFileEntry | A host name entry in the network hosts file. Fields: Forensics | Forensics |
| ActiveDirectoryAuditPasswordModificationAttempt |  | Windows |
| ProcessSignal |  | Linux |
| ProcessInjection | An event that indicates that a remote process wrote and executed code. | Windows |
| SpotlightEntitySystemState | Spotlight Entity heart-beat event to notify cloud of current state with last synced batch and Channe... | Windows, macOS, Linux |
| ConfigurationProfileModified |  | macOS |
| OpenDirectoryDeleteUser |  | macOS |
| LogonBehaviorCompositionDetectInfo |  | Windows |
| OpenDirectoryGroupAdd |  | macOS |
| DnsCache | An entry observed within the system's DNS Cache. Fields: Forensics | Forensics |
| WindowsTimelineEntryTimestamp | Fields: Forensics | Forensics |
| BrowserAccountInfo | Browser user account information. Fields: Forensics | Forensics |
| BrowserHistoryClearInfo | Browser history clearing event information. Fields: Forensics | Forensics |
| ForensicsCollectorOffline | Final event of a Forensics collection. Fields: Forensics | Forensics |
| ForensicsCollectorOnline | Marks the beginning of a Forensics collection. Fields: Forensics | Forensics |
| WmiQuery | Windows Management Instrumentation (WMI) query status. Fields: Forensics | Forensics |
| FilesStatisticInfo | Files statistic information. Fields: Forensics | Forensics |
| BrowserCookieInfo | Browser tracking cookie information. Fields: Forensics | Forensics |
| WSLDistributionUnregistered | A user unregisters a Linux distribution. | Windows |
| SystemdTimerCreated |  | Linux |
| WSLDistributionStopping | The Linux distribution is stopping. | Windows |
| DriverLoadBlocked | Event which indicates we successfully blocked a driver from loading. | Windows |
| SigningPublicKey |  | iOS, Android |
| FsVolumeReadInfo |  | Windows |
| IdpWatchdogRemediationActionRequest |  | Windows |
| ActiveDirectoryAuditGroupModified |  | Windows |
| ActiveDirectoryIncomingDceRpcRequest | Indicates that the Domain Controller must handle one or more incoming DCE/RPC requests from an accou... | Windows |
| DcRemovableStorageDeviceConnected |  | Windows, macOS |
| DcRemovableStorageDeviceDisconnected |  | Windows, macOS |
| ScriptControlDotNetMetadata | Contains the last 56kb of ScriptContent from a .NET AMSI scan. | Windows |
| GroupAccount | Describes an observed group account. Fields: Forensics | Forensics |
| PrefetchFile | Prefetch or Layout file records 8 most recent execution times of a Windows application. Fields: Fore... | Forensics |
| BrowserHistoryVisit | Browser history hit information. Fields: Forensics | Forensics |
| EventTapInfo | Describes a macOS Event Tap. Event Taps allow for capturing of keyboard and mouse HID events. Fields... | Forensics |
| LoginItemAdded |  | macOS |
| IdpPolicyCloudAccessRuleMatch | Fields: Public Cloud | Public Cloud |
| SuspiciousUserRemoteAPCAttempt | An event that indicates that a remote APC (Asynchronous Procedure Call) that is classified as potent... | Windows |
| SuperfetchAppInfo | Application entry from Windows Superfetch AgForegroundAppHistory.db. Fields: Forensics | Forensics |
| ForensicsCollectorLog | A log entry emitted by the Falcon Forensics Collector process. Fields: Forensics | Forensics |
| RuntimeEnvironmentVariable | Environment Variable provided to a process; In the context of falcon forensics, this is an environme... | Forensics |
| MftBootSector | Windows Master File Table (MFT) Boot sector. Fields: Forensics | Forensics |
| UserAssistAppLaunchInfo | Application launched via user-assisted GUI menu. Fields: Forensics | Forensics |
| IdpWatchdogRemediationActionTakenForCpu |  | Windows |
| GetAsyncKeyStateEtwBatch | An event that indicates that an application called the GetAsyncKeyState API multiple times. | Windows |
| NamedPipe | Named pipe information. Fields: Forensics | Forensics |
| ProcessHandleTableEntry | An entry in a process handle table referencing a kernel object. Fields: Forensics | Forensics |
| DataEgress | Description of a data egress observed on the sensor. | Windows, macOS |
| WSLDistributionStarted | The Linux distribution starts. | Windows |
| FileSignatureStatistics | On-demand scan for files with name extensions and header magic values. Fields: Forensics | Forensics |
| WSLDistributionRegistered | A user registers a Linux distribution but hasn’t started it yet. | Windows |
| SuperfetchAppSchedule | Application running schedule/period recently updated from Windows Superfetch AgGlobalHistory.db. Fie... | Forensics |
| WSLVMStarted | The Linux Virtual Machine Root Namespace starts. | Windows |
| LocalGroupIdentity | Group identity information includes user group name, GID, and names, UIDs and sid of user members. F... | Forensics |
| BrowserExtensionInfo | Browser extension/addon information. Fields: Forensics | Forensics |
| DcBluetoothAuthorizationStatus |  | macOS |
| UserGroupDeleted |  | Linux |
| GcpAsset | An event that contains GCP (Google Cloud Platform) Organization Metadata. Fields: Public Cloud | Public Cloud |
| GcpComputeFirewall | An event that contains GCP (Google Cloud Platform) Compute Image configuration details. Fields: Publ... | Public Cloud |
| AzureVirtualMachineState | An event that contains the machine state for any Azure virtual machine. Fields: Public Cloud | Public Cloud, Public Cloud |
| GcpComputeNetworkPeering | An event that contains GCP (Google Cloud Platform) Compute Network Peering configuration details. Fi... | Public Cloud |
| GcpComputeInstance | An event that contains GCP (Google Cloud Platform) Compute Instance configuration information. Field... | Public Cloud |
| GcpComputeNetwork | An event that contains GCP (Google Cloud Platform) Compute Network configuration information. Fields... | Public Cloud |
| GcpComputeDisk | An event that contains GCP (Google Cloud Platform) Compute Disk Configuration details. Fields: Publi... | Public Cloud |
| GcpComputeSubnetwork | An event that contains GCP (Google Cloud Platform) Compute Subnetwork configuration details. Fields:... | Public Cloud |
| AzureIpConfiguration | An event that contains a list of Azure IP configurations and attributes of the Azure IP configuratio... | Public Cloud |
| AzureVirtualNetwork | An event that contains a list of the Azure virtual networks and the Azure virtual network attributes... | Public Cloud |
| GcpIamServiceAccount | An event that contains GCP (Google Cloud Platform) IAM Service Account configuration details. Fields... | Public Cloud |
| AzureSubscription | An event that contains a list of Azure subscriptions. Fields: Public Cloud | Public Cloud |
| AzureNetworkInterface | An event that contains a list of Azure network interfaces and the Azure network interface attributes... | Public Cloud |
| GcpComputeImage | An event that contains GCP (Google Cloud Platform) Compute Image configuration details. Fields: Publ... | Public Cloud |
| AzureResourceGroup | An event that contains a list of Azure Resource Groups. Fields: Public Cloud | Public Cloud |
| AzureDisk | An event that contains a list of Azure disks and their attributes. Fields: Public Cloud | Public Cloud |
| AzureVirtualMachine | An event that contains a list of Azure virtual machines and the Azure virtual machine attributes. Fi... | Public Cloud |
| AzureSubnet | An event that contains Azure sub-networks in the virtual network. Fields: Public Cloud | Public Cloud |
| AzurePublicIpAddress | An event that contains Azure public IP addresses. Fields: Public Cloud | Public Cloud |
| AzureNetworkSecurityGroup | An event that contains information about an Azure Network Security Group. Fields: Public Cloud | Public Cloud |
| AzureVirtualNetworkPeering | An event that contains a list of the Azure virtual networks and the Azure virtual network attributes... | Public Cloud |
| AzurePrivateEndpoint | An event that connects Azure Network interface to other services with private links. Fields: Public ... | Public Cloud |
| EksNodeGroup | Snapshot of an AWS EKS node group. Fields: Public Cloud | Public Cloud |
| EksCluster | Snapshot of an AWS EKS cluster. Fields: Public Cloud | Public Cloud |
| K8SDeployment | Snapshot of a deployment object in Kubernetes. Fields: Public Cloud | Public Cloud |
| K8SReplicaSet | Snapshot of a Replica Set object in Kubernetes. Fields: Public Cloud | Public Cloud |
| K8SDaemonSet | Snapshot of a Daemon Set object in Kubernetes. Fields: Public Cloud | Public Cloud |
| EksFargateProfile | Snapshot of an AWS EKS Fargate profile. Fields: Public Cloud | Public Cloud |
| IdpWatchdogConfigurationsGetResponse |  | Windows |
| FileContentsChanged |  | Linux |
| SruApplicationTimelineProvider | System Resource Utilization Monitor: application resource usage timeline. Fields: Forensics | Forensics |
| ShellBagFileTimeStampMetadata | One event is emitted per timestamp from a ShellBag registry entry. Fields: Forensics | Forensics |
| SyscacheEntry | An entry in windows syscache hive. Fields: Forensics | Forensics |
| BITSJobMetadata | Background Intelligent Transfer Service (BITS) job metadata: times, proxy. Fields: Forensics | Forensics |
| RegCrowdstrikeValueUpdate |  | Windows |
| BrowserDownloadStarted | Browser downloaded file information signifying download start time. Fields: Forensics | Forensics |
| BrowserDownloadEnded | Browser downloaded file information signifying download end time. Fields: Forensics | Forensics |
| OdsScanComplete | On-demand scan for files with name extensions and header magic values. Fields: Forensics | Forensics |
| AutoRunProcessInfo | Describes a process that is automatically executed. Fields: Forensics | Forensics |
| PeSectionInfo | Windows Portable Executable (PE) section information. Fields: Forensics | Forensics |
| ShellBagInfo | Windows ShellBag MRU registry entry. Fields: Forensics | Forensics |
| PeHeaderOptionalInfo | Portable Executable optional header information from a Windows executable. Fields: Forensics | Forensics |
| RemoteThreadCreate |  | macOS |
| ActiveDirectoryAuditGroupMemberModified |  | Windows |
| RouteIP4 | IPv4 Route entry. Fields: Forensics | Forensics |
| PeFileWrittenDetectInfo |  | Windows |
| MachOHeaderParsed | A MachO file was read into memory from disk and its header was parsed. | macOS |
| MemoryLocked |  | Linux |
| VulnerableDriverDetectInfo |  | Windows |
| DeliverRulesEngineResultsToCloud |  | Windows, Linux, macOS |
| AtJobInfo | Windows At jobs in use. Fields: Forensics | Forensics |
| HttpResponse |  | Linux, macOS |
| PcaAppLaunchEntry | An application launch entry in windows Program Compatibility Assistant (PCA) file PcaAppLaunchDic.tx... | Forensics |
| SyntheticPR2Stats |  | macOS |
| PcaGeneralDbEntry | An application launch entry in windows Program Compatibility Assistant (PCA) database PcaGeneralDb[0... | Forensics |
| SyntheticVirtualMemoryArea |  | Linux |
| VirtualMemoryArea |  | Linux |
| FileOfInterestBasicInfo |  | macOS, Windows, Linux |
| FalconProcessHandleOpDetectInfo |  | Windows |
| ScriptFileContentsDetectInfo |  | Windows |
| DnsRequest | When a process on a host generates a DNS query, the sensor waits for the response, to generate a Dns... | Windows, Linux, Android, macOS, iOS |
| ArchiveMemberInfo | Archive member file information. Fields: Forensics | Forensics |
| FileSystemContainmentStatus |  | Windows |
| SystemExtension | Describes a macOS system extension identified by the collector. Fields: Forensics | Forensics |
| SharedObjectLoaded |  | Linux, Linux, Falcon Container, Windows, macOS |
| SignInfo | Sent by FalconForensicsCollector containing information about the signing-state of an image. | macOS, Windows, Forensics |
| MalPaths | Malicious DLL or executable image name conflicts found in different or unexpected folders. Fields: F... | Forensics |
| AppleScriptFileWritten |  | Windows, macOS, Linux |
| LzfseFileWritten |  | macOS, Windows, Linux |
| FileTimestampMetadata | FileTime event is emitted per timestamp for a given file. This helps analysts build a timeline of fi... | Forensics |
| BITSJobFileInfo | Background Intelligent Transfer Service (BITS) job file information. Fields: Forensics | Forensics |
| LinkFileInfo | Link file information. Fields: Forensics | Forensics |
| LogEntry | A log entry observed on an endpoint. Fields: Forensics | Forensics |
| FileEntry | Some portion of a text file, either a single line or matched regular expression. Fields: Forensics | Forensics |
| PtyAttached |  | Linux |
| PeHeaderInfo | Portable Executable header information from a Windows executable. Fields: Forensics | Forensics |
| EntropyScan | File contents entropy, useful for identifying potentially malicious files. Fields: Forensics | Forensics |
| LSQuarantineEvent | Fields: Forensics | Forensics |
| PemFileWritten |  | Linux, Windows, macOS |
| RecentExecutionTimestamp | Recent execution timestamp from a Forensics artifact. Fields: Forensics | Forensics |
| ArchiveInfo | Archive file information. Fields: Forensics | Forensics, Forensics |
| FileWrittenWithEntropyHigh |  | Windows, Linux |
| MftRecord | Windows Master File Table (MFT) record. Fields: Forensics | Forensics |
| XzFileWritten |  | Windows, macOS, Linux |
| SyntheticSharedObjectLoaded |  | Linux |
| AmcacheEntry | Metadata related to PE execution and program installation on Windows 7 and Server 2008 R2 and above.... | Forensics |
| MemoryAdvise |  | Linux |
| WebShellDetected | To identify webshell script files in a target folder, the content of each text file is matched again... | Forensics |
| UserEatAccessMonitoring |  | Windows |
| ClassifiedProcessStart |  | Windows |
| PromiscuousBindIP4 | This is a reified NetworkBindIP4 indicating a socket is in promiscuous mode. | Windows, Windows, Linux, macOS |
| DcUsbDevicePolicyViolation | An event that indicates a USB device that matched a rule in a policy but was not blocked due to the ... | macOS, Windows, Linux |
| DcBluetoothDeviceBlocked |  | macOS |
| DcBluetoothDevicePolicyViolation |  | macOS |
| SruApplicationResourceUsage | System Resource Utilization Monitor: application resource usage per user. Fields: Forensics | Forensics |
| NtfsLinkCreatedDetectInfo |  | Windows |
| IPCDetectInfo |  | Windows |
| MacKnowledgeActivityStart | An entry from a knowledgeC database indicating the start of some user activity on a MacOs system. Fi... | Forensics |
| MemoryProtectionChanged |  | Linux |
| ScheduledTaskTemplateDetectInfo |  | Windows |
| DcRemovableStorageDeviceBlocked |  | Windows, macOS |
| DcRemovableStorageDevicePolicyViolation |  | Windows, macOS |
| ResourceLimit |  | Linux |
| RegFeatureUsageInfo | Fields: Forensics | Forensics |
| HttpRequestV2Detect |  | Windows, Windows |
| HostedServiceStatusInfo | Status information includes loaded DLL for a hosted service. Fields: Forensics | Forensics |
| RegCrowdstrikeKeyUpdate |  | Windows |
| K8SInitContainerStatus | Snapshot of an Initialization(Init) Container belonging to a Pod Fields: Public Cloud | Public Cloud |
| AzureNatFirewallRule | An event that contains Azure firewall rules for LAN. Fields: Public Cloud | Public Cloud |
| ActiveDirectoryIncomingLdapSearchRequest | Indicates that the Domain Controller must handle one or more LDAP search requests from an account on... | Windows |
| AksCluster | Snapshot of an Azure AKS cluster. Fields: Public Cloud | Public Cloud |
| AksAgentPool | Snapshot of an Azure AKS Agent Pool. Fields: Public Cloud | Public Cloud |
| K8SPod | Snapshot of a Pod object in Kubernetes. Fields: Public Cloud | Public Cloud |
| K8SService | Snapshot of a Service object in Kubernetes. Fields: Public Cloud | Public Cloud |
| K8SNode | Snapshot of a Node object in Kubernetes. Fields: Public Cloud | Public Cloud |
| K8SRunningContainer | Snapshot of a running Container belonging to a Pod. Fields: Public Cloud | Public Cloud |
| AzureFirewall | An event that contains information about Azure cloud-based network security service. Fields: Public ... | Public Cloud |
| AzureFirewallRuleCollection | An event that contains Azure firewall rule collections for application, NAT (network address transla... | Public Cloud |
| AzureNetworkSecurityGroupRule | An event that contains Azure security rules in the specified network security group. Fields: Public ... | Public Cloud |
| K8SEphemeralContainer | Snapshot of an ephemeral Container belonging to a Pod. Fields: Public Cloud | Public Cloud |
| K8SRunningContainerStatus | Snapshot of status for a running Container inside a Pod. Fields: Public Cloud | Public Cloud |
| AksVMSS | Snapshot of an Azure Virtual Machine Scale Sets. Fields: Public Cloud | Public Cloud |
| K8SInitContainer | Snapshot of status for an Initialization(Init) Container inside a Pod. Fields: Public Cloud | Public Cloud |
| AzureApplicationFirewallRule | An event that contains firewall rules for https traffic or Azure SQL traffic. Fields: Public Cloud | Public Cloud |
| BamRegAppRunTime | Recent program execution timeline from Background Activity Moderator (BAM) system service registry. ... | Forensics |
| ScriptControlDetectInvalidInfo |  | Linux, Falcon Container |
| UserAccount | Describes an observed user account. Fields: Forensics | Forensics |
| JumpListInfo | Fields: Forensics | Forensics |
| RegShimCache | Shim cache registry entry. Fields: Forensics | Forensics |
| ActiveDirectoryAuditUserModified |  | Windows |
| KernelExtension | Describes a macOS kernel extension identified by the collector. Fields: Forensics | Forensics |
| AzureNetworkFirewallRule | An event that contains Azure network filtering rules. Fields: Public Cloud | Public Cloud |
| ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate |  | Windows |
| ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate |  | Windows |
| ConfigStateUpdate | Sent periodically and when dynamic config is updated. Analysts can find out which config was active ... | Windows, macOS, Linux, Falcon Container, iOS, Android, Kubernetes, Windows Legacy, Vmcluster |
| LFODownloadConfirmation | Thrown when the agent receives an LFODownload event. | Windows, macOS, Linux, Falcon Container, Android, iOS, Kubernetes, Vmcluster |
| ASLRBypassAttempt | Emitted when a process that applied ForceASLR to a module detects an invalid execution attempt. This... | Windows |
| HeapSprayAttempt | Emitted when a process that had HeapSpray protections applied detects an invalid execution attempt. | Windows |
| SEHOverWriteAttempt | An event that is emitted when a UserException event has failed a SEH (Structured Exception Handler) ... | Windows |
| SsoUserLogon | Indicates an initial, successful sign-in to an SSO facilitator, which could be either an IDaaS direc... | Public Cloud |
| SsoUserLogonFailure | Indicates an initial, failed sign-in to an SSO facilitator, which could be either an IDaaS directory... | Public Cloud |
| SsoApplicationAccess | Indicates successful access to an application through an SSO facilitator, which could be either an I... | Public Cloud |
| AdditionalHostInfo | Serves as an addition to kernel-driven HostInfo event. Provides host-specific machine information fr... | Windows, macOS |
| AndroidModuleStateUpdate | Status information of modules for the Android sensor. AndroidModuleId lists available modules. Field... | Android |
| SsoApplicationAccessFailure | Indicates failed access to an application through an SSO facilitator, which could be either an IDaaS... | Public Cloud |
| UserAccessLogEntry | Per-user access log information for the year for a service role and IP address pair on Windows serve... | Forensics |
| FileSignatureMismatch | On-demand scan for files with name extensions and header magic values. Fields: Forensics | Forensics |
| RemoteProcessMemoryWrite |  | Linux |
| FileHashesEvent | Fields: Forensics | Forensics |
| WindowsTimelineEntry | Fields: Forensics | Forensics |
| OpenDirectoryGroupRemove |  | macOS |
| RegGenericInfo | Registry entry generic information. Fields: Forensics | Forensics |
| MacKnowledgeActivityEnd | An entry from a knowledgeC database indicating the end of some user activity on a MacOs system. Fiel... | Forensics, Windows |
| MacMRU | A digital forensics record derived from Apple SharedFileList (.sfl/.sfl2) files. This event helps id... | Forensics |
| WlanInterfaceInfo | Fields: Forensics | Forensics |
| ShimDbTag | A tag entry in the Shim database. Fields: Forensics | Forensics, Forensics |
| SruNetworkConnectivityUsage | System Resource Utilization Monitor: connection time per local network interface, application and us... | Forensics |
| FileExtendedAttrOperation |  | macOS |
| USNRecord | Fields: Forensics | Forensics |
| PeCodePageInfo | A code page that is used to decode code point values within a windows Portable Executable resource. ... | Forensics |
| RemoteProcessMemoryRead |  | Linux |
| XProtectAction |  | macOS |
| AspmCollectionStatusUpdate |  | Linux, Windows |
| ProcessOpenedFileDescriptor | Fields: Forensics | Forensics |
| EddScanStart | Sent by sensor to indicate the start of a new EDD scan run. Note: This event is currently not suppor... | macOS, Windows |
| CreateThreadNoStartImage | This event is used to indicate the target start address of a CreateThread attempt is not within the ... | Windows |
| CreateThreadReflectiveDll | This event is used to indicate the presence of a reflectively loaded dll in the callstack for a Crea... | Windows |
| UmppcEntryAnomaly |  | Windows |
| ScriptControlBlocked | This event is sent when Falcon Host has blocked malicious script content from being executed on the ... | Windows |
| ProcessHandleOpDetectInfo | An event that describes the operation on a Process handle that triggered a detection. | Windows |
| ReflectiveDllOpenProcess | A userspace thread attempted to open a process which appeared to originate from a reflectively loade... | Windows |
| ScriptControlScanTelemetry |  | Windows |
| IdpPolicyAccessRuleMatch |  | Windows |
| CreateThreadKernelNoStartImage | Emitted when a new system thread is created outside of a loaded driver. | Windows |
| IdpWatchdogReEnabled |  | Windows |
| SensorSelfDiagnosticAlert |  | Linux, macOS, Windows |
| ExtendedExploitMitigationViolatedDetectInfo |  | Windows |
| ProcessState | Running process observed at collection time. Fields: Forensics | Forensics |
| FfcBytePatternScanResult | Describes a scanning result performed by the Falcon Forensics Collector. Fields: Forensics | Forensics |
| CSAResultsGenericDetectInfo |  | Windows |
| DataProtectionBrowserConnect |  | Windows, macOS |
| ProcessSubstituteUser |  | macOS |
| DcUsbDeviceConnected | An event that describes a connected USB device to which Device Control is attached. It is sent each ... | Linux, Windows, macOS |
| GcpComputeNetworkInterface | An event that contains GCP (Google Cloud Platform) Compute Network Interface configuration informati... | Public Cloud |
| SuspectCreateThreadStack | This event is used to indicate that suspicious data has been discovered in the context of a CreateTh... | Windows |
| ErrorEvent | Event indicating a sensor error. | Linux, Falcon Container, Windows, macOS, Vmcluster, Kubernetes |
| ResourceUtilization | An event that contains CPU and RAM utilization data for a system. The event is sent when the sensor ... | Linux, Falcon Container, macOS, Kubernetes, Windows |
| RecentlyModifiedFileExecutedInContainer |  | Linux, Falcon Container |
| DetectionExcluded | This event indicates that a detection has been excluded, either by customer exclusions or by CrowdSt... | Android, iOS, macOS, Linux, Falcon Container, Windows |
| ZstdFileWritten |  | Linux, macOS, Windows |
| LhaFileWritten |  | Windows |
| BcmFileWritten |  | Windows |
| FreeArcFileWritten |  | Windows |
| Base64PeFileWritten |  | Windows |
| LRZipFileWritten |  | Linux, macOS, Windows |
| BlakHoleFileWritten |  | Windows |
| ZpaqFileWritten |  | Windows |
| BrotliFileWritten |  | Windows |
| PeaFileWritten |  | Windows |
| Yz1FileWritten |  | Windows |
| NetworkSummary |  | Windows |
| LZipFileWritten |  | macOS, Linux, Windows |
| ProcessEnvironmentEmpty |  | Linux |
| NetworkStatisticsIP6 | Fields: Forensics | Forensics, macOS |
| LzmaFileWritten |  | Windows, macOS, Linux |
| SyntheticProcessTrace |  | Linux |
| ShellCommandLineInfo |  | Linux |
| NetworkStatisticsUDP6 | Fields: Forensics | Forensics |
| LZOFileWritten |  | Linux, Windows, macOS |
| NetworkStatisticsTCP4 | Fields: Forensics | Forensics |
| NetworkStatisticsUDP4 | Fields: Forensics | Forensics |
| NetworkStatisticsIP4 | Fields: Forensics | Forensics |
| PromiscuousBindIP6 |  | Windows |
| LZ4FileWritten |  | macOS, Windows, Linux |
| MpThreatWMI | Fields: Forensics | Forensics |
| NetworkStatisticsTCP6 | Fields: Forensics | Forensics |
| NetworkIcmpDataIP4 |  | Linux |
| SensorMetadataUpdate |  | Linux |
| UserExceptionDEP | This event is emitted when a userspace process is detected as having has a DEP or NX-related excepti... | Windows |
| MpThreatAction | Report when a particular threat action type has occurred. Fields: Forensics | Forensics |
| ClassifiedSensitiveFileAccess |  | Windows |
| PhpEvalString |  | Linux |
| PhpExecuteScript |  | Linux |
| PhpBase64Decode |  | Linux |
| FileDescriptorMonitor | Fields: Forensics | Forensics |
| WSLMetadata |  | Linux |
| BITSJobInfo | Background Intelligent Transfer Service (BITS) job information. Fields: Forensics | Forensics |
| MpThreat | Microsoft protection threat. Fields: Forensics | Forensics |
| MpThreatDetection | Microsoft protection threat detection. Fields: Forensics | Forensics |
| NetworkIcmpDataIP6 |  | Linux |
| MpThreatDetectionWMI | Fields: Forensics | Forensics |
| DataProtectionPACDiagnostic |  | Windows |
| InstallServiceDownloadComplete | An install service download has completed. | Windows |
| QuarantineActionResult | This event reports the result of a file quarantine triggered by Falcon Prevent. | Windows, macOS, Linux, Kubernetes, Vmcluster |
| UpdateManifestDownloadComplete | An update manifest download has completed. | Windows |
| NetworkUncontainmentCompleted | This event is sent by the sensor after processing a NetworkUncontainmentRequest event from the cloud... | Windows, macOS, Linux, Android, iOS |
| QuarantinedFile | This event is generated when a file is quarantined by Falcon Prevent. | Windows, macOS, Linux, Kubernetes, Vmcluster |
| InstallBundleDownloadComplete | An install bundle download has completed. | Windows |
| NetworkContainmentCompleted | This event is sent by the sensor after processing a NetworkContainmentRequest event from the cloud. ... | Windows, Linux, macOS, iOS, Android |
| SAMHashDumpFromUnsignedModule | This event contains information about an unsigned module that accessed protected SAM account registr... | Windows |
| QuarantinedFileState | This event reports the state of a file quarantined by Falcon Prevent. | Windows, macOS, Linux, Kubernetes, Vmcluster |
| OsfmDownloadComplete | Sent by LFODownloadActor when new OSFM data is downloaded. | Windows |
| InstalledUpdates | An event that describes the updates installed on the system. The Status field will indicate if some ... | Windows |
| UserFontLoad | An event that is sent when a user mode program attempts to add a font. | Windows |
| NullPageUnmapAttempt | An event that indicates that an attempt was made to unmap the NULL page. | Windows |
| UmppaErrorEvent |  | Windows |
| NullPageProtectionModificationAttempt | An event that indicates that an attempt was made to modify the protection of the NULL page. | Windows |
| RansomwareOpenFile | A reified LocalFsPostCreate event so the cloud can route these events for ransomware support. | Windows |
| RegNtPostOpenKeyEx | Registry post open key operation event. | Windows |
| FsPostCreate | This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing... | Windows |
| ManifestDownloadComplete | Sent by LFODownloadActor when a new configuration manifest has been downloaded. | Windows, macOS, Linux, Falcon Container, Kubernetes, Vmcluster |
| ConfigDownloadComplete | Sent by LFODownloadActor when a new binary configuration has been downloaded as part of a configurat... | Windows, macOS, Linux, Falcon Container, Kubernetes, Vmcluster |
| FsPostOpen | This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing... | Windows |
| ModuleDownloadComplete | Sent by LFODownloadActor when a new module has been downloaded as part of a configuration update. | Windows, macOS, Linux |
| ECBDownloadComplete | Sent by LFODownloadActor when a new ECB module has been downloaded as part of a configuration update... | Windows, macOS, Linux, Windows |
| RegKeySecurityDecreasedFromUnsignedModule | This event contains information about a protected registry security object whose security was decrea... | Windows |
| ChannelDataDownloadComplete | Sent by LFODownloadActor when a new channel data file has been downloaded. | Windows, Android, Linux, Falcon Container, macOS, Kubernetes, iOS, Vmcluster |
| FsPostOpenSnapshotFile | Information about a file opened on a snapshot volume. | Windows |
| PrivilegedProcessHandle | Indicates a process has opened a handle to a privileged process with special access rights. | Windows |
| FsPostOpenUpImpersonating | A reified FsPostOpen event that occurred in the context of a thread up-impersonating another user, a... | Windows |
| RegNtPostOpenKeyExUpImpersonating | A reified RegNtPostOpenKeyEx event that occurred in the context of a thread up-impersonating another... | Windows |
| PrivilegedProcessHandleFromUnsignedModule | This event contains information about a privileged process handle created from an unsigned module. | Windows, Windows |
| ConfigurationLoaded | Thrown when a new configuration has been successfully loaded but before any Event Sources are starte... | Android, iOS |
| OciImageInfo | An event that contains information about this image used in a container. | Linux, Falcon Container |
| CsUmProcessCrashSummaryEvent | A event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field. | Windows |
| FirewallRuleApplicationFailed | An event that indicates that the application of a firewall rule has failed. An event that indicates ... | Windows, macOS, Linux |
| FalconServiceStatus | A message from CsFalconService regarding the service and its servlets' lifecycle events. | Windows, Windows |
| RemediationActionServiceRemoval | Notification of a service persistence removal remediation action attempted by the sensor. | Windows |
| CidMigrationError |  | Windows, Linux, macOS |
| CidMigrationManifestDownloadComplete |  | Windows, macOS, Linux |
| AmsBytePatternScanTelemetry |  | Windows |
| AmsBytePatternScanResult |  | Windows |
| RecoveryActionDeleteFilesComplete |  | Windows, Linux, Falcon Container, Kubernetes, macOS |
| RecoveryActionRegistryDeleteValueKeyComplete |  | Windows |
| RecoveryActionRegistryDeleteKeyComplete |  | Windows |
| RecoveryActionRegistryDeleteKeyReply |  | Windows |
| RecoveryActionRegistryCreateKeyComplete |  | Windows |
| RecoveryActionManipulateModuleTableComplete |  | Linux, Falcon Container, macOS, Windows |
| RecoveryActionKillProcessesComplete |  | Linux, Falcon Container, Kubernetes, Windows, macOS |
| RecoveryActionKillProcessesReply | Fields: Kubernetes, Windows, macOS, Linux, Falcon Container | Kubernetes, Windows, macOS, Linux, Falcon Container |
| PackageManagerDownloadComplete | Fields: Vmcluster, macOS, Linux, Falcon Container, Windows, Kubernetes | Vmcluster, macOS, Linux, Falcon Container, Windows, Kubernetes |
| OciContainerPlumbingSummary |  | Linux |
| EddScanStatus | Sent by sensor periodically to report the status of an on-going scan. Note: This event is currently ... | macOS, Windows |
| LFODownloadComplete |  | macOS, Kubernetes, Vmcluster, Android, iOS, Windows, Linux, Falcon Container |
| IdpCloudHealthConfigurationsSetResponse |  | Windows |
| IdpWatchdogConfigurationsSetResponse |  | Windows |
| RemediationMonitorKillProcess | Notification of a kill process remediation action that would have been attempted by the sensor but w... | Linux, macOS, Windows |
| RemediationActionQuarantineMacroFile |  | Windows |
| KernelCallbackTablePatch | An event that indicates that the KernelCallbackTable has been altered at the specified index. If pre... | Windows |
| EarlyExploitPivotDetect | Telemetry event indicating execution pivoting in an unusual way. Could be indicative of malicious co... | Windows |
| SuspiciousUserFontLoad | Sent when a UserFontLoad event has been blocked by the sensor. | Windows |
| CommsLogReset | Sent by Communications indicating that the CommsLog was flushed due to invalid data | macOS |
| RecoveryActionRegistrySetValueKeyReply |  | Windows |
| RecoveryActionSetRuntimeSystemTagsComplete |  | Windows, macOS, Linux, Falcon Container |
| RecoveryActionSetSystemTagsComplete | Fields: Kubernetes, Windows, macOS, Linux, Falcon Container | Kubernetes, Windows, macOS, Linux, Falcon Container |
| RecoveryActionGetSystemTagsComplete | Fields: Kubernetes, macOS, Linux, Falcon Container, Windows | Kubernetes, macOS, Linux, Falcon Container, Windows |
| OpenDirectoryPasswordModification |  | macOS |
| RecoveryActionDeleteFilesReply | Fields: Kubernetes, Windows, macOS, Linux, Falcon Container | Kubernetes, Windows, macOS, Linux, Falcon Container |
| RecoveryActionGetModuleTableRecordComplete |  | macOS, Windows, Linux, Falcon Container |
| OciContainerInfo | An event that contains information about this container on creation of the container. | Linux, Falcon Container |
| HttpVisibilityStatus | An event that indicates that the status of the HTTP Visibility event source has been updated. | Windows |
| SSHClientAuthenticated |  | Linux |
| RecoveryActionGetRuntimeSystemTagsComplete |  | Windows, macOS, Linux, Falcon Container, Windows |
| DriverPreventFailed | Event which indicates we failed (or timed out) attempting to block a driver load. | Windows |
| RemediationActionKillProcess | Notification of a kill process remediation action attempted by the sensor. | Windows, Linux, macOS, Windows Legacy |
| RemediationActionQuarantineFile | Notification of a quarantine file remediation action attempted by the sensor. | Windows |
| RemediationMonitorQuarantineFile | Notification of a quarantine file remediation action that would have been attempted by the sensor bu... | Windows |
| CreateProcessArgs | Full command line argument corresponding to a process creation. | macOS |
| CloudScanControl | A event to that notifies downstream services of completed tasks. Fields: Public Cloud | Public Cloud, Windows |
| RemediationActionRegistryRemoval | Notification of a registry persistence removal remediation action attempted by the sensor. | Windows |
| BlockThreadFailed | A block thread request failed. | Windows |
| KillProcessError | If KillProcessActor fails to kill a process due to process being marked as system critical or for an... | Linux, Falcon Container, macOS, Windows |
| MacFsEventRecord | Mac fsevents record, forensically interesting filesystem logging/information. Fields: Forensics | Forensics |
| ExcelDocumentOpened |  | Windows |
| QuarantineXattribute | Fields: Forensics | Forensics |
| AppProtocolDetected |  | macOS |
| RemediationActionQuarantineOfficeMacroFile |  | Windows, Windows |
| OpenDirectoryCreateUser |  | macOS |
| ZerologonExploitAttempt |  | Windows |
| PeLanguageId | A language on which a windows Portable Executable resource depends. Fields: Forensics | Forensics |
| MsiTransactionExecuted |  | Windows |
| RecoveryActionRegistryDeleteValueKeyReply |  | Windows |
| RecoveryActionRegistrySetValueKeyComplete |  | Windows |
| EtwComponentResponse | Event sent in when EtwComponent has initialized. AttemptNumber is no longer used. | Windows |
| SuspendProcessError | This event is emitted if KillProcessActor fails to suspend a process. | Linux, Falcon Container, Windows, macOS |
| RemediationActionScheduledTaskRemoval | Notification of a scheduled task persistence removal remediation action attempted by the sensor. | Windows |
| RecoveryActionRegistryCreateKeyReply |  | Windows, Android, iOS |


## Detailed Event Information

### AcUninstallConfirmation

**Description:** This event is generated when a Falcon sensor is uninstalled from a host. Important: The Falcon sensor stores events locally in a cache, which enables you to maintain data integrity even if connection to the cloud is interrupted. The cache holds a maximum of 20,000 events and sends them after a host re-establishes a connection with the cloud. However, if you reboot, the cache is lost. This means that if you uninstall a sensor off network and reboot, the cache storing those events is lost, including any AcUninstallConfirmation events.

**Platforms:** Windows, macOS, Linux

---

### AcUnloadConfirmation

**Description:** The cloud will respond with this event as acknowledgement that a sensor was uninstalled.

**Platforms:** Windows, macOS, Linux

---

### HostInfo

**Description:** This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This event provides information about the host running the sensor. When searching for information about a specific host, you should use the much faster aid_master search capability instead of searching for HostInfo events This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This event provides information about the host running the sensor. When searching for information about a specific host, you should use the much faster aid_master search capability instead of searching for HostInfo events

**Platforms:** Windows, macOS, iOS, Windows Legacy

---

### HookedDriverObject

**Description:** This event describes the presence of a hooked pointer in a DRIVER_OBJECT structure.

**Platforms:** Windows

---

### WfpFilterTamperingFilterDeleted

**Description:** This event is created whenever WFP indicates to our callout driver that a filter that references one of our callout functions has been deleted from the Base Filtering Engine.

**Platforms:** Windows

---

### WfpFilterTamperingFilterAdded

**Description:** This event is created whenever WFP indicates to our callout driver that a new filter that references one of our callout functions has been added to the Base Filtering Engine.

**Platforms:** Windows

---

### DeliverLocalFXToCloud

**Description:** DeliverLocalFXToCloud conveys feature extraction (FX) data to the cloud from the sensor. `DeliverLocalFXToCloud` conveys feature extraction (FX) data to the cloud from the sensor.

**Platforms:** Windows, macOS, Linux

---

### UserLogoff

**Description:** This event is generated when a user logs off from a host.

**Platforms:** Windows, macOS, Linux, ChromeOS

---

### NeighborListIP4

**Description:** This event shows the IPv4 network addresses and MAC addresses of other devices on the host's network, gathered using ARP on the host. The first time a device sends this event to the CrowdStrike Cloud, its entire ARP table is sent. For later events, only the changes to the ARP table are sent. This event returns data as a MAC address, an IPv4 address, and a delimiter character (0 or 1). Each item is separated by a pipe character (|). If the delimiter character is a 0, the preceding MAC and IP addresses belong to a device. If the delimiter character is 1, the preceding IP and MAC addresses belong to the host's gateway.

**Platforms:** Windows, macOS, Linux, Falcon Container, Forensics

---

### NeighborListIP6

**Description:** This event shows the MAC addresses and IPv6 network addresses of other devices on the host's network, gathered using ARP on the host. The first time a device sends this event to the CrowdStrike Cloud, its entire ARP table is sent. For later events, only the changes to the ARP table are sent. This event returns data as a MAC address, an IPv6 address, and a delimiter character (0 or 1). Each item is separated by a pipe character (|). If the delimiter character is a 0, the preceding MAC and IP addresses belong to a device. If the delimiter character is 1, the preceding IP and MAC addresses belong to the host's gateway.

**Platforms:** Windows, macOS, Linux, Falcon Container, Forensics

---

### LocalIpAddressRemovedIP4

**Description:** This event is generated when a host loses its IPv4 network address.

**Platforms:** Windows, macOS, Linux, Falcon Container, iOS, Android

---

### LocalIpAddressRemovedIP6

**Description:** This event is generated when a host loses its IPv6 network address.

**Platforms:** Windows, macOS, Linux, Falcon Container, iOS, Android

---

### DcUsbEndpointDescriptor

**Description:** An event that describes an endpoint descriptor extracted from the firmware of a USB device. An interface descriptor typically defines 2 or more endpoints that are used for data transfer. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** Windows, macOS, Linux

---

### DcUsbHIDDescriptor

**Description:** This event describes a HID (Human Interface Device) descriptor extracted from the firmware of a USB device. A HID descriptor is a container for a complex set of sub-descriptors that identify the capabilities of a HID device. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** Windows, macOS, Linux

---

### DcStatus

**Description:** An event that contains the status information for the Device Control plug-and-play driver. It is sent once per day after it has successfully connected to the Device Control interface.

**Platforms:** Windows, macOS, Linux

---

### DcUsbConfigurationDescriptor

**Description:** An event that describes a configuration descriptor extracted from the firmware of a USB device. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** Windows, macOS, Linux

---

### DcUsbInterfaceDescriptor

**Description:** An event that describes an interface descriptor extracted from the firmware of a USB device. There are typically multiple interface descriptors for a given configuration descriptor, with each interface exposing a device capability. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** Windows, macOS, Linux

---

### DcUsbDeviceDisconnected

**Description:** An event that describes a disconnected USB device to which Device Control has previously attached. It is sent each time the system powers off, the associated hub/port is power cycled, or the device is physically removed from the system.

**Platforms:** Windows, macOS, Linux

---

### DcOnline

**Description:** An event that indicates the Device Control plug-and-play driver interface has come online. It is sent each time the sensor connects to the Device Control interface.

**Platforms:** Windows, macOS, Linux

---

### DcOffline

**Description:** An event that indicates the Device Control plug-and-play driver interface has gone offline. It is sent each time the sensor disconnects from the Device Control interface.

**Platforms:** Windows, macOS, Linux

---

### DcUsbDeviceWhitelisted

**Description:** An event that indicates a USB device was added to an allowlist by a Device Control policy. The Device Control plug-and-play driver did not attach to the device as a result of an allowlist policy rule.

**Platforms:** Windows, macOS, Linux

---

### AwsIamAccountAlias

**Description:** Information from AWS API call ListAccountAliases.

**Platforms:** Windows, Public Cloud

---

### FirmwareAnalysisStatus

**Description:** This event contains status of the FPnP filter driver.

**Platforms:** Windows, macOS

---

### FirmwareRegionMeasured

**Description:** Indicates that a certain region of a firmware image was measured.

**Platforms:** Windows, macOS

---

### FirmwareAnalysisErrorEvent

**Description:** Indicates an occurrence of error associated with the Firmware Analysis feature.

**Platforms:** Windows, macOS

---

### FirmwareAnalysisHardwareData

**Description:** This event contains hardware data collected by Firmware Analysis.

**Platforms:** Windows, macOS

---

### AwsEc2NetworkInterface

**Description:** This event provides key metadata regarding network interfaces in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeNetworkInterfaces API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html] on your behalf. Network interfaces can either be in detached or attached state. When attached, they have an associated EC2 instance ID which can be used to correlate between the two events. Note that multiple network interface objects can also be associated to a single EC2 instance. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkInterfacePrivateIP

**Description:** This event provides key metadata regarding private IP addresses in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeNetworkInterfaces API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeNetworkInterfaces.html] on your behalf. Multiple private IPs can be assigned to a single network interface. The AwsNetworkInterfaceId field can be used to correlate these private IPs to the associated AwsEc2NetworkInterface event. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Volume

**Description:** This event provides key metadata regarding EBS volumes configured in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeVolumes API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVolumes.html] on your behalf. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Instance

**Description:** This event provides key metadata regarding EC2 instances in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeInstances API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html] on your behalf. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2SecurityGroup

**Description:** This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSecurityGroups API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html] on your behalf. Security groups control the level of network based access to resources within a VPC and can typically associated to network interfaces and their attached EC2 instances. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud, Windows, Public Cloud

---

### AwsEc2Subnet

**Description:** This event provides key metadata regarding subnets configured in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSubnets API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSubnets.html] on your behalf. Subnets represent a level of network segmentation and are created within a VPC to control and manage routing configurations. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Image

**Description:** This event provides key metadata regarding images (AMIs, AKIs, and ARIs) available in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeImages API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeImages.html] on your behalf. This event is only generated for Discover for AWS [/support/documentation/10/falcon-discover-feature-guide] customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2SecurityGroupRule

**Description:** This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSecurityGroups API [https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeSecurityGroups.html] on your behalf. Each event represents a specific rule/ACL defined within a security group and are associated based on the AwsGroupId field. Rules represent the actual logic or ACL applied to the group. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkAcl

**Description:** 

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkAclEntry

**Description:** Information from AWS API call DescribeNetworkAcls.

**Platforms:** Windows, Public Cloud

---

### GroupIdentity

**Description:** Provides the sensor boot unique mapping between GID, AuthenticationId, UserPrincipal, and UserSid.

**Platforms:** macOS, Forensics

---

### IOServiceRegister

**Description:** This event describes an IOService being registered with a notification handler.

**Platforms:** macOS

---

### LocalIpAddressIP4

**Description:** This event is generated when a host uses a new IPv4 network address.

**Platforms:** Linux, Falcon Container, iOS, Android, macOS, Windows, Forensics

---

### LocalIpAddressIP6

**Description:** This event is generated when a host uses a new IPv6 network address.

**Platforms:** Linux, Falcon Container, iOS, Android, macOS, Windows, Forensics

---

### HostnameChanged

**Description:** Sent by the hostname awareness actor to communicate change in hostname.

**Platforms:** Linux, Falcon Container, macOS

---

### OsVersionInfo

**Description:** This event is generated during any one of the following scenarios: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This provides details about the operating system on which the sensor is running. Servers do not get rebooted often. Hence, you might not see some servers in this sample query. Fields: Android

**Platforms:** Android, iOS, Windows, macOS, Linux, Falcon Container, Forensics, Windows Legacy, Vmcluster, Kubernetes

---

### APKMetadata

**Description:** Sent from mobile sensor in PlayStore mode when a new APK file is present on the device, as a result of an installation or an update Fields: Android

**Platforms:** Android

---

### MobileAppsManifest

**Description:** Delivers information about apps. Fields: Android

**Platforms:** Android

---

### UncontainerizeAppResponse

**Description:** Sent in response to UncontainerizeApp, containing response information for the operation. Fields: Android

**Platforms:** Android

---

### WiFiConnect

**Description:** Sent when a device connects to a WiFi network. This event is only sent if the Connected Wi-Fi networks setting is enabled in Mobile Policies. Fields: Android, iOS

**Platforms:** Android, iOS

---

### WiFiDisconnect

**Description:** Sent when a device disconnects from a WiFi network. This event is only sent if the Connected Wi-Fi networks setting is enabled in Mobile Policies. Fields: Android, iOS

**Platforms:** Android, iOS

---

### MobilePowerStats

**Description:** Sent when power level in a mobile device changes, also contains duration when the sensor is in foreground/background during IntervalStartTime to IntervalEndTime. Fields: Android

**Platforms:** Android, iOS

---

### ContainerizationUpdate

**Description:** Sent following an LFODownload of a new APK to be installed or updated in the container, containing response information for the operation. Fields: Android

**Platforms:** Android

---

### FileInfo

**Description:** Error event for FileInfo response. FileInfo response with information about a file. Fields: Forensics

**Platforms:** Forensics, macOS

---

### ClipboardCopy

**Description:** Sent when content is copied to the clipboard.

**Platforms:** iOS, Android

---

### InstalledApplication

**Description:** An event that describes a single application. E.g. representing a newly installed application, one just removed, or one discovered during enumeration. An event that describes a single application. E.g. representing a newly installed application, one just removed, or one discovered during enumeration. This event contains all the information for a single app.

**Platforms:** Windows, macOS, Linux, Forensics

---

### SmbClientShareOpenedEtw

**Description:** An event that indicates when a machine connects to a remote share. This event is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmbClientShareClosedEtw

**Description:** An event that indicates when a machine disconnects from a remote share. This event is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmbServerV1AuditEtw

**Description:** An event that indicates that a client attempted to connect to this machine using the Server Message Block protocol, SMBv1. Captured using the ETW consumer.

**Platforms:** Windows

---

### DeactivateMobileSensorResponse

**Description:** Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. On Android, container apps and data have been wiped from the device. Complete deactivation of the sensor, including all current and future cloud connections, will follow shortly after. Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. Fields: Android, iOS

**Platforms:** Android, iOS

---

### AccessoryConnected

**Description:** Sent when the device connects to an external accessory. This event will only be sent if the Connected Bluetooth devices setting is enabled in Mobile Policies. Fields: Android

**Platforms:** Android, iOS

---

### AccessoryDisconnected

**Description:** Sent when a device disconnects from an external accessory. This event will only be sent if the Connected Bluetooth devices setting is enabled in Mobile Policies. Fields: Android

**Platforms:** Android, iOS

---

### BillingInfo

**Description:** Sensor sends this event to inform the cloud about the sensor billing type.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### EtwErrorEvent

**Description:** An event that indicates that an error occurred which associated is with the ETW consumer.

**Platforms:** Windows

---

### OciContainerTelemetry

**Description:** An event that contains telemetry information on a container.

**Platforms:** Linux, Falcon Container

---

### OciContainerStarted

**Description:** An event that is sent by the sensor to indicate a container has started when the container is created.

**Platforms:** Linux, Falcon Container

---

### OciImageHeartbeat

**Description:** An event that is sent by the sensor to indicate this image is still being used.

**Platforms:** Linux, Falcon Container

---

### OciContainerHeartbeat

**Description:** An event that is sent by the sensor to indicate this container engine is still being used. This event is sent every 24 hours.

**Platforms:** Linux, Falcon Container

---

### OciContainerStopped

**Description:** An event sent to indicate a container has stopped when the container is deleted.

**Platforms:** Linux, Falcon Container

---

### AuditCveKmEtw

**Description:** An event that indicates that a driver or the kernel reported a known CVE (Common Vulnerabilities and Exposures id). Captured using the ETW consumer.

**Platforms:** Windows

---

### CsUmProcessCrashAuxiliaryEvent

**Description:** An event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field, one per thread.

**Platforms:** Windows

---

### FsVolumeMounted

**Description:** Provides information about a mounted volume. Fields: Forensics

**Platforms:** Forensics, iOS, Windows, Linux, Falcon Container, macOS

---

### OciContainerEngineInfo

**Description:** An event that contains information about this container engine.

**Platforms:** Linux, Falcon Container

---

### AuditCveUmEtw

**Description:** An event that indicates that an application reported a known CVE (Common Vulnerabilities and Exposures id). Captured using the ETW consumer.

**Platforms:** Windows

---

### SystemCapacity

**Description:** An event that describes the CPU and RAM capacity of the system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in capacity is detected. An event that describes the CPU and RAM capacity data for a system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in capacity is detected.

**Platforms:** Windows, macOS, Linux

---

### AndroidManifestXmlUploaded

**Description:** An event that indicates the LFO upload of the AndroidManifest of an android application package was successful and maps the package name to the upload ID. Fields: Android

**Platforms:** Android

---

### AndroidManifestFragmentData

**Description:** An event that's sent by the sensor along with AndroidManifestXmlUploaded that contains a logical portion of AndroidManifest encoded as JSON after a process is installed or after it is opened. Fields: Android

**Platforms:** Android, Windows

---

### FileVaultStatus

**Description:** Contains information regarding the system FileVault (encrypted) state.

**Platforms:** macOS

---

### AmsiRegistrationStatus

**Description:** Event to record status in AMSI module.

**Platforms:** Windows

---

### PtActivationStatus

**Description:** Reports host's compatibility with the Processor Trace feature.

**Platforms:** Windows

---

### ProvisioningStarted

**Description:** Sent when sensor begins provisioning.

**Platforms:** Windows

---

### ProvisioningStatusUpdate

**Description:** Sent every 2 minutes during provisioning.

**Platforms:** Windows

---

### ProvisioningEnded

**Description:** Sent when provisioning is completed.

**Platforms:** Windows

---

### K8SCluster

**Description:** Snapshot of Kubernetes cluster for mapping Kubernetes cluster id and name. Fields: Public Cloud

**Platforms:** Public Cloud

---

### SpotlightEntityBatchHeader

**Description:** Spotlight Batch header to indicate all required metadata of incoming batch along with information to deal with possibilities of dropped subsequent events.

**Platforms:** Windows, macOS, Linux

---

### RemovableMediaVolumeMounted

**Description:** This event provides information about a removable media volume that was just mounted. Fields: Android

**Platforms:** Android, Windows

---

### FsVolumeUnmounted

**Description:** Provides information about an unmounted volume.

**Platforms:** iOS, Windows, macOS, Linux, Falcon Container

---

### RemovableMediaVolumeUnmounted

**Description:** An event that contains information about a removable media volume that was just unmounted. Fields: Android

**Platforms:** Android

---

### RemovableMediaFileWritten

**Description:** An event that is emitted for files written to removable media on Android devices. Fields: Android

**Platforms:** Android

---

### ActiveDirectoryAccountNameUpdate

**Description:** Indicates a change to the subject account's SAM account name.

**Platforms:** Windows

---

### ActiveDirectoryAccountOuUpdate

**Description:** Indicates a change to the subject account's organizational unit.

**Platforms:** Windows

---

### ActiveDirectoryAccountDisabled

**Description:** Indicates the subject account has been disabled.

**Platforms:** Windows

---

### ActiveDirectoryAccountLocked

**Description:** Indicates the subject account has been locked.

**Platforms:** Windows

---

### ActiveDirectoryAccountUnlocked

**Description:** Indicates the subject account has been unlocked.

**Platforms:** Windows, Windows

---

### ActiveDirectoryAccountCreated

**Description:** Indicates the creation of the subject account.

**Platforms:** Windows

---

### ActiveDirectoryAccountPasswordUpdate

**Description:** Indicates a change to the subject account's password.

**Platforms:** Windows

---

### ActiveDirectoryAccountEnabled

**Description:** Indicates the subject account has been enabled.

**Platforms:** Windows

---

### StaticAnalysisContainerTelemetry

**Description:** Cloudable event in response to a telemetry query for the static analysis containers.

**Platforms:** Windows

---

### UserInformationEtw

**Description:** An event that indicates the password of a user was changed or set and other user information taken from UserLogonEtw.

**Platforms:** Windows

---

### TcgPcrInfo

**Description:** An event that contains the Platform Configuration Register (PCR) values.

**Platforms:** Windows

---

### DcBluetoothDeviceDisconnected

**Description:** This event represents a disconnected Bluetooth device.

**Platforms:** Windows, macOS

---

### DiskUtilization

**Description:** An event that contains the used and available storage space for each mounted logical drive or volume that has an underlying physical disk locally attached to the system. The event is sent when the sensor connects and every 12 hours thereafter.

**Platforms:** Linux, Forensics

---

### DcBluetoothDeviceConnected

**Description:** This event represents a connected Bluetooth device.

**Platforms:** Windows, macOS

---

### CidMigrationConfirmation

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### CidMigrationComplete

**Description:** 

**Platforms:** macOS, Windows, Linux, Android

---

### DriverPreventionStatus

**Description:** 

**Platforms:** Windows

---

### SensorGroupingTagsUpdate

**Description:** 

**Platforms:** Windows

---

### SysConfigInfo

**Description:** 

**Platforms:** Linux, Falcon Container

---

### IdpPolicyAccountEventRuleMatch

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### UserLogon

**Description:** This event is generated when a user logs on to a host.

**Platforms:** Linux, Windows, macOS, ChromeOS

---

### SensorAntiTamperState

**Description:** 

**Platforms:** Windows

---

### UserLogonFailed2

**Description:** An event that indicates that a local user attempted to logon, but failed due to bad password. LogonTime is the last successful logon time. The remote information will be present only if the logon originated over the network. RawProcessId will attribute a pid if relevant.

**Platforms:** Linux, ChromeOS, macOS, Windows, Windows

---

### ServicesStatusInfo

**Description:** Detailed information and status of a windows service.

**Platforms:** Windows, Forensics

---

### OdsCancelRequestReceived

**Description:** 

**Platforms:** Windows, macOS

---

### OdsScheduleCancelRequestReceived

**Description:** 

**Platforms:** Windows, macOS

---

### OdsScheduleRequestReceived

**Description:** 

**Platforms:** Windows, macOS

---

### OdsStarted

**Description:** 

**Platforms:** Windows, macOS

---

### OdsProfileReceived

**Description:** 

**Platforms:** Windows, macOS

---

### OdsStartRequestReceived

**Description:** 

**Platforms:** Windows, macOS

---

### OdsMaliciousFileFound

**Description:** 

**Platforms:** Windows, macOS

---

### OdsActionStatus

**Description:** 

**Platforms:** Windows, macOS

---

### ChannelActive

**Description:** 

**Platforms:** Windows

---

### OdsScheduleCanceled

**Description:** 

**Platforms:** Windows, macOS

---

### OdsStatus

**Description:** 

**Platforms:** Windows, macOS

---

### DcIdentification

**Description:** This event enables monitoring of domain controllers (DCs) and the passing of identifying information to the CrowdStrike Cloud.

**Platforms:** Windows

---

### K8SClusterInfo

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### AgentOnline

**Description:** This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor is installed on a host 3. An existing sensor is updated This event can help to determine when a host was last rebooted. However, it's not intended for gathering report data, such as uptime of long-running servers or counting all active hosts. For reports, use Falcon Investigate's Sensor Report [/investigate/events/en-US/app/eam2/sensor_app] . This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor is installed on a host 3. An existing sensor is updated 4. The managed configuration changes This event can help to determine when a host was last rebooted. However, it's not intended for gathering report data, such as uptime of long-running servers or counting all active hosts. Fields: ChromeOS

**Platforms:** ChromeOS, macOS, Windows, Linux, Falcon Container, Android, Kubernetes, iOS, Windows Legacy, Vmcluster

---

### SensorHeartbeat

**Description:** Sent periodically to inform the cloud that the sensor is active. Sent periodically to inform the cloud that the sensor is active. Fields: ChromeOS

**Platforms:** ChromeOS, Windows Legacy, Vmcluster, Android, iOS, macOS, Windows, Linux, Falcon Container, Kubernetes

---

### LocalWindowsUserUpdate

**Description:** 

**Platforms:** Windows

---

### SmbClientShareLogonBruteForceSuspected

**Description:** 

**Platforms:** Windows, Windows

---

### CsKmCrashSummaryEvent

**Description:** 

**Platforms:** Windows

---

### LockdownModeStatus

**Description:** 

**Platforms:** iOS

---

### IdpContainerRestarted

**Description:** 

**Platforms:** Windows

---

### AsepValueUpdate

**Description:** This event is generated when a Microsoft Auto Start Execution Point registry key has been updated.

**Platforms:** Windows, Windows, macOS, Linux, Falcon Container

---

### RansomwareRenameFile

**Description:** A reified LocalFsPostRename event so the cloud can route these events for ransomware support.

**Platforms:** Windows

---

### AsepKeyUpdate

**Description:** Generated when an Auto Start Execution Point registry key is updated.

**Platforms:** Windows

---

### ProcessRollup

**Description:** An event that contains information from several sources and combines it into one event. The event describes a process which is running or has previously run on the host. The functionality of this event has been replaced by ProcessRollup2.

**Platforms:** Windows

---

### PeVersionInfo

**Description:** An event that describes file version information from a Portable Executable file resource location, as seen in the file properties dialog on Windows. The data is in the form of a binary blob that requires further parsing.

**Platforms:** Windows

---

### KernelModeLoadImage

**Description:** Indicates a kernel-mode module has been loaded into memory.

**Platforms:** Windows, macOS, Linux, Falcon Container, Forensics

---

### IoSessionConnected

**Description:** An event that is emitted when an IO session has been connected.

**Platforms:** Windows

---

### IoSessionLoggedOn

**Description:** An event that is emitted when an IO session has been logged off.

**Platforms:** Windows

---

### CreateService

**Description:** Generated when a Windows service is created.

**Platforms:** Windows

---

### ModifyServiceBinary

**Description:** Indicates a Windows service's binary was changed.

**Platforms:** Windows

---

### UACCredentialCaptureElevation

**Description:** This UAC event indicates the UAC consent.exe application was used by Windows to refresh the smart card credentials after a configurable timeout has expired.

**Platforms:** Windows

---

### UACCOMElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target COM object.

**Platforms:** Windows

---

### UACMSIElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target MSI.

**Platforms:** Windows

---

### WroteExeAndGeneratedServiceEvent

**Description:** Indicates a process both wrote an executable and generated a service event.

**Platforms:** Windows, Windows

---

### UACAxisElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target ActiveX Installation Service (AXIS).

**Platforms:** Windows

---

### DllInjection

**Description:** This event indicates that DLL injection occurred in the target process.

**Platforms:** Windows

---

### UnsignedModuleLoad

**Description:** This event contains information about an unsigned module that was loaded into a target process. It combines relevant information from the ImageHash and SignInfoWithCertAndContext events for the unsigned module.

**Platforms:** Windows

---

### SuspiciousRawDiskRead

**Description:** This event indicates a process successfully read a target file using raw disk access.

**Platforms:** Windows

---

### HostedServiceStopped

**Description:** This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is stopped by the service control manager (SCM). Unfortunately, the sensor is not currently capable of identifying who requested this operation. However, it can be used to confirm that this is a service stopping vs. a service crashing or being terminated. Also, starting and stopping hosted services multiple times during boot might not always show up in this event due to caching done by the SCM.

**Platforms:** Windows

---

### WmiCreateProcess

**Description:** Windows Management Instrumentation (WMI) is a default service installed on machines with Windows XP and newer. WMI is the infrastructure for management data and operations which allows a user to remotely manage machines and automate administrative tasks. WMI also supports scripting languages such as PowerShell and VBScript. Adversaries have utilized the WMI service to install implants, tools and perform credential theft via scripting in an effort to maneuver throughout customer environments. The Enhanced Attacker Execution Profiling (EAEP) event “WmiCreateProcess” will be useful in tracking the adversary’s lateral activity and/or origin of an attack during an intrusion. The Enhanced Attacker Execution Profiling (EAEP) event category focuses on gathering additional endpoint data on things like service creation, scheduled tasks, firewall rule modification, etc. This event is emitted when it is determined WMI was used to start a new process. ProcessRollup2 may also be updated to include RPC client information if available. There may be some known inconsistencies with attribution of the real RPC client data here, due to worker thread indirection that occurs within the WMI service process. If so, a later update will resolve those inconsistencies.

**Platforms:** Windows

---

### ExecutableDeleted

**Description:** This event indicates that an executable was deleted from the host.

**Platforms:** Windows, macOS, Linux

---

### NewExecutableRenamed

**Description:** This event is generated when an executable is renamed.

**Platforms:** Windows, macOS

---

### SuspiciousDnsRequest

**Description:** This event is generated when the sensor detects a suspicious DNS request. A request is suspicious if it is attempting to send a request to a domain found on the sensor’s list of suspicious domains.

**Platforms:** Windows, Linux, macOS

---

### ProcessSelfDeleted

**Description:** This event indicates when a process self-delete situation is detected. It will be thrown when a process deletes a file that was previously loaded as the primary module in an ancestor process. If the self-delete was accomplished via injecting into an already running process, ContextProcessId will be the injector as well.

**Platforms:** Windows, macOS, Linux

---

### FlashThreadCreateProcess

**Description:** Thread associated with Flash activity created a process.

**Platforms:** Windows, macOS

---

### EndOfProcess

**Description:** When a process that’s running on a host finishes, the sensor will count all of the events that were generated by that process, bundle the information in an EndOfProcess event, and send it to the cloud. This allows you to determine, for example, how many DNS requests a process made, how many directory creation events occurred, or how many network connections a process made.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### CommandHistory

**Description:** This event includes the full command history associated with one of the consoles in a process that has recently terminated (identified by the TargetProcessId). Note that a given UPID may be associated with multiple consoles (identified by ApplicationName).

**Platforms:** Windows

---

### BehaviorWhitelisted

**Description:** Indicates that a behavior has been whitelisted.

**Platforms:** Windows, macOS, Linux

---

### UserLogonFailed

**Description:** This event is generated when a user logon fails.

**Platforms:** Windows

---

### FalconHostRegTamperingInfo

**Description:** An event that describes the registry event that triggered a Falcon sensor tampering indicator.

**Platforms:** Windows

---

### FalconHostFileTamperingInfo

**Description:** An event that describes the file event that triggered a Falcon sensor tampering indicator.

**Platforms:** Windows

---

### ScriptControlErrorEvent

**Description:** An event that contains telemetry data containing up to 56 KB ScriptContent field data from AMSI (AntiMalware Scan Interface) that has been deobfuscated.

**Platforms:** Windows

---

### SuspiciousRegAsepUpdate

**Description:** An event that describes the registry activity that triggered a suspicious registry ASEP (Autostart Extension Point) detect.

**Platforms:** Windows

---

### NetworkModuleLoadAttempt

**Description:** An event that indicates that a process whose primary image was not on a network attempted to load a module from that network.

**Platforms:** Windows

---

### RemovableDiskModuleLoadAttempt

**Description:** An event that indicates that a process with a primary image that is not on a removable disk attempted to load a module from a removable disk.

**Platforms:** Windows

---

### SuspiciousEseFileWritten

**Description:** This event indicates that a possible domain credential file (NTDS.dit) was copied from a volume snapshot.

**Platforms:** Windows

---

### FileDeleteInfo

**Description:** This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event.

**Platforms:** Windows, macOS, Linux

---

### SystemTokenStolen

**Description:** An event that indicates that system token stealing was detected.

**Platforms:** Windows

---

### LowILModuleLoadAttempt

**Description:** An event that indicates that a non-LowIL process attempted to load an untrusted LowIL module.

**Platforms:** Windows

---

### ImageHash

**Description:** This event is generated for each DLL or executable loaded into a process’ memory.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### TerminateProcess

**Description:** This event is thrown when a process exits normally or is forcibly terminated.

**Platforms:** macOS, Linux, Falcon Container, Windows, ChromeOS

---

### ProcessActivitySummary

**Description:** A rollup event created when a process terminates. Includes statistical information about what a process did during its lifetime.

**Platforms:** macOS, Windows

---

### KextLoad

**Description:** Signals a Kernel Extension (KEXT) Load, triggered via a MAC hook.

**Platforms:** macOS

---

### KextUnload

**Description:** Signals a Kernel Extension (KEXT) Unload, triggered via a MAC hook.

**Platforms:** macOS

---

### DirectoryCreate

**Description:** This event is generated when a process creates a new folder.

**Platforms:** macOS, Windows, Linux

---

### SyntheticProcessRollup2

**Description:** This event provides data similar to what is available in a ProcessRollup2. SyntheticProcessRollup2 events are generated for processes that started before the sensor does, such as during installation.

**Platforms:** macOS, Windows, Linux, Falcon Container, ChromeOS

---

### CriticalFileAccessed

**Description:** A critical file was accessed.

**Platforms:** macOS, Linux, Falcon Container, ChromeOS

---

### CriticalFileModified

**Description:** A critical file was modified.

**Platforms:** macOS, Linux, Falcon Container, ChromeOS

---

### PtyCreated

**Description:** An event that notifies that a pty has been created.

**Platforms:** macOS

---

### FileOpenInfo

**Description:** This event is generated when a file is opened by a process.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### FirewallDisabled

**Description:** An event that is sent from the sensor when packet filter is disabled.

**Platforms:** macOS

---

### FirewallEnabled

**Description:** An event that is sent from the sensor when packet filter is enabled.

**Platforms:** macOS

---

### FileCreateInfo

**Description:** This event is generated when a file is created by a process.

**Platforms:** macOS, Linux, Falcon Container, Windows, Linux, Falcon Container, Windows, macOS, Windows Legacy

---

### CriticalEnvironmentVariableChanged

**Description:** A process set a critical environment variable.

**Platforms:** Linux, Falcon Container

---

### FileDeleted

**Description:** This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event. This event has been deprecated as of Falcon Sensor for Windows 4.16.7903, and Falcon Sensor for Mac 4.16.7801. Older sensors and existing data for these events will still appear, but new sensors utilize the FileOpenInfo event. This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event. File entry from a file observed in the recycle bin. Fields: Android

**Platforms:** Android, Windows, Forensics

---

### ProcessRollup2

**Description:** This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats. This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats. Understanding TargetProcessId Every ProcessRollup2 event contains a field called TargetProcessId. This ID is generated internally by the sensor, and will be unique for every instance of a process. For example, if you run cmd.exe twice, you will see two different ProcessRollup2 events with two unique values for TargetProcessId. This ID should not be confused with the host operating system PID for the process, which will be a different value. Processes often generate multiple, if not dozens of related events. For example, opening a browser or running an executable can generate network connectivity events, temporary file write events, DNS request events, etc. We therefore need a way to understand the parent-child relationship between processes and the events they generate. Understanding ContextProcessId Every event that is generated by a ProcessRollup2 contains a data field called ContextProcessId. The ContextProcessId will match the TargetProcessId of its parent ProcessRollup2 event. In the example below, the ContextProcessId values indicate that each of the events are children of the parent ProcessRollup2events. By searching for events that have matching values for ContextProcessId and TargetProcessId, you can see a list of all events that were generated as a result of a ProcessRollup2 event. Understanding ParentProcessId As previously mentioned, every process that executes on a host has a corresponding ProcessRollup2 event. This means that when a process spawns another process, a brand new ProcessRollup2 event will be generated for that new ProcessRollup2event. This new event will contain a field called ParentProcessId. The ParentProcessId of the child PR2 will match the TargetProcessId of the parent PR2, as shown below : By searching for events that have matching values for ParentProcessId and TargetProcessId, you can determine the parent-child relationship of multiple ProcessRollup2 events. This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats. Understanding TargetProcessId Every ProcessRollup2 event contains a field called TargetProcessId. This ID is generated internally by the sensor, and will be unique for every instance of a process. For example, if you run cmd.exe twice, you will see two different ProcessRollup2 events with two unique values for TargetProcessId. This ID should not be confused with the host operating system PID for the process, which will be a different value. Processes often generate multiple, if not dozens of related events. For example, opening a browser or running an executable can generate network connectivity events, temporary file write events, DNS request events. We therefore need a way to understand the parent-child relationship between processes and the events they generate. Understanding ContextProcessId Every event that is generated by a ProcessRollup2 contains a data field called ContextProcessId. The ContextProcessId will match the TargetProcessId of its parent ProcessRollup2 event. In the example below, the ContextProcessId values indicate that each of the events are children of the parent ProcessRollup2events. By searching for events that have matching values for ContextProcessId and TargetProcessId, you can see a list of all events that were generated as a result of a ProcessRollup2 event. Understanding ParentProcessId As previously mentioned, every process that executes on a host has a corresponding ProcessRollup2 event. This means that when a process spawns another process, a brand new ProcessRollup2 event will be generated for that new ProcessRollup2event. This new event will contain a field called ParentProcessId. The ParentProcessId of the child PR2 will match the TargetProcessId of the parent PR2, as shown below : By searching for events that have matching values for ParentProcessId and TargetProcessId, you can determine the parent-child relationship of multiple ProcessRollup2 events. Fields: Android

**Platforms:** Android, Linux, Falcon Container, ChromeOS, Forensics, Windows Legacy, macOS, Windows

---

### ReflectiveDllLoaded

**Description:** An event that indicates that a user space thread reflectively loaded DLL.

**Platforms:** Windows, Windows

---

### ProtectVmEtw

**Description:** A virtual memory protect event generated from ETW data.

**Platforms:** Windows

---

### ProcessWitness

**Description:** Emitted when the sensor witnesses a process is running. This event is not an indication that a process just started, only that the process was first seen running when the event was sent. It is used for iOS where there is no way to be notified of processes start or running, or to query about running processes, and the sensor only knows a process exists when it makes a network connection. This event is therefore different from PR2s or SynPR2s.

**Platforms:** iOS

---

### ClipboardPaste

**Description:** Sent when content is pasted from the clipboard. Fields: Android

**Platforms:** Android

---

### AndroidIntentSentIPC

**Description:** This event is sent when an Android Intent is fired from the container Fields: Android

**Platforms:** Android

---

### MobileOsIntegrityStatus

**Description:** Describes the integrity of the mobile OS (eg. jailbroken/rooted)

**Platforms:** iOS, Android

---

### JarFileWritten

**Description:** This event is generated when a Java executable archive (.jar) file type is written to disk. Fields: Android

**Platforms:** Android, Windows, macOS, Linux

---

### RegGenericValueUpdate

**Description:** An event that indicates that a registry value has been updated.

**Platforms:** Windows

---

### ScreenshotTakenEtw

**Description:** An event that indicates that partial or full screenshot has been taken. Captured using the ETW consumer.

**Platforms:** Windows

---

### SetWinEventHookEtw

**Description:** An event that indicates that an application called the SetWinEventHook API. Captured using the ETW consumer.

**Platforms:** Windows

---

### RegSystemConfigValueUpdate

**Description:** An event that indicates that a registry value related to system configuration or security has been updated.

**Platforms:** Windows

---

### SetThreadCtxEtw

**Description:** 

**Platforms:** Windows

---

### RegisterRawInputDevicesEtw

**Description:** An event that indicates that an application called the RegisterRawInputDevices API. Captured using the ETW consumer.

**Platforms:** Windows

---

### QueueApcEtw

**Description:** 

**Platforms:** Windows

---

### SmbClientNamedPipeConnectEtw

**Description:** An event that indicates when a machine connects to a remote SMB (Server Message Block) named pipe. The event contains the pattern id of the associated indicator and is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows, Windows

---

### ProcessExecOnSMBFile

**Description:** An event that contains telemetry data emitted on execution of a PE file which was written by SMB.

**Platforms:** Windows

---

### TokenImpersonated

**Description:** An event that contains detailed before and after impersonation information for detection telemetry.

**Platforms:** Windows

---

### SetWindowsHookExEtw

**Description:** An event that indicates that an application called SetWinEventHookEx API. Captured using the ETW consumer.

**Platforms:** Windows

---

### WmiProviderRegistrationEtw

**Description:** An event that is emitted when a WMI (Windows Management Instrumentation) provider gets registered. Captured using the ETW consumer.

**Platforms:** Windows

---

### MobileDetection

**Description:** An event that's sent by the sensor when a sensor-level detection occurs. Fields: Android, iOS

**Platforms:** Android, iOS

---

### DexFileWritten

**Description:** Emitted when a file has been written that contains a real Dex image header. Fields: Android

**Platforms:** Android

---

### DeveloperOptionsStatus

**Description:** An event that contains info about developer-related settings on the device. Fields: Android, iOS

**Platforms:** Android, iOS

---

### SELinuxStatus

**Description:** An event that contains info about the SELinus status. Fields: Android

**Platforms:** Android

---

### StorageEncryptionStatus

**Description:** An event that contains information about the Device Storage encryption. Fields: Android

**Platforms:** Android

---

### LockScreenStatus

**Description:** An event that contains info about the device lock screen mechanism. Fields: Android, iOS

**Platforms:** Android, iOS

---

### SystemPartitionStatus

**Description:** An event that contains information about the device system partition. This event is deprecated as of Android sensor version 2021.09.3060002. Fields: Android

**Platforms:** Android

---

### SafetyNetCompatibilityStatus

**Description:** An event that contains the SafetyNet compatibility status obtained via the Google SafetyNet API. Fields: Android

**Platforms:** Android

---

### DnsRequestResult

**Description:** An event that contains DNS request results after a DNS request. Fields: Android, iOS

**Platforms:** Android, iOS

---

### FileSystemAttributesStatus

**Description:** An event that contains info about the Filesystem attributes of the device.

**Platforms:** iOS

---

### DebuggableFlagTurnedOn

**Description:** An event that indicates a debuggable flag has been turned on for a non-dev build of an app. Fields: Android

**Platforms:** Android

---

### BootLoaderStatus

**Description:** An event that contains info about the device's bootloader. Fields: Android

**Platforms:** Android

---

### HarmfulAppData

**Description:** An event that contains the name, hash, and category of the harmful app. Fields: Android

**Platforms:** Android

---

### DuplicateInstallFromPlayStore

**Description:** An event that indicates a containerized app is also installed outside the container. Fields: Android

**Platforms:** Android, Windows

---

### ScriptControlScanInfo

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### ObjCRuntimeAltered

**Description:** An event that indicates an Obj-C method has been tampered with. MethodSignature indicates which Obj-C method has been tampered with. ImageFileName contains the path to the image containing the new, swizzled, implementation of the method. ExpectedImageFileName contains the path where it was expected. SuspectAddress contains the load address of ImageFileName. ExpectedAddress contains the load address of ExpectedImageFileName.

**Platforms:** iOS

---

### UnexpectedDynamicLibraryLoaded

**Description:** An event that indicates that an unexpected dynamic library was loaded at runtime.

**Platforms:** iOS

---

### UnexpectedFileFound

**Description:** An event that indicates a file that should not exist on the device has been found. An event that indicates a file that should not exist on the device has been found.

**Platforms:** iOS, Android

---

### TrampolineDetected

**Description:** An event that indicates a C function has been tampered with. In iOS jailbreak, functions are modified by adding an unconditional trampoline in the first 4 words. FunctionName contains the function that has been determined to have been tampered with, ImageFileName contains the path to the image where the trampoline jumps to, and ExecutableBytes contains the first 4 words of the tampered-with function where the trampoline was detected.

**Platforms:** iOS

---

### CertificatePinningCompromised

**Description:** An event that indicates that the certificate pinning methods/functions on the device have been tampered with and cannot be trusted. For further details, see the following associated events: ObjCRuntimeAltered or TrampolineDetected.

**Platforms:** iOS

---

### ProcessTokenStolen

**Description:** An event that describes a process token stealing detection. ContextProcessId has been detected stealing the token of TargetProcessId.

**Platforms:** Windows

---

### DebuggedState

**Description:** An event that indicates a process is in the state of being debugged (i.e., has a debugger attached to it.)

**Platforms:** iOS

---

### PathUnexpectedlyReadable

**Description:** An event that indicates a system file or directory can be opened for reading. On a non-jailbroken system, this should not be possible.

**Platforms:** iOS

---

### UnexpectedEnvironmentVariable

**Description:** An event that indicates some dangerous environment variables have made it to the app at runtime.

**Platforms:** iOS

---

### CodeSigningAltered

**Description:** An event that indicates the code signing flags of the current application have unexpected flags or are missing expected ones.

**Platforms:** iOS

---

### SafetyNetCheckFailed

**Description:** An event that indicates the SafetyNet check could not be completed. Fields: Android

**Platforms:** Android

---

### SystemPartitionAltered

**Description:** An event that indicates a system partition has been altered and is in an unexpected state.

**Platforms:** iOS

---

### InstallFromUnknownSourcesStatus

**Description:** An event that contains info about third-party app installers on Android. Fields: Android

**Platforms:** Android

---

### RemoteBruteForceDetectInfo

**Description:** An event that describes a remote brute force detection.

**Platforms:** Windows

---

### SensitiveWmiQuery

**Description:** An event that indicates that a client process executed a sensitive WMI query.

**Platforms:** Windows

---

### DCSyncAttempted

**Description:** Directory Services changes were replicated. If the source host is not a Domain Controller, this could represent malicious activity.

**Platforms:** Windows

---

### RemediationMonitorRegistryRemoval

**Description:** Notification of a registry persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### ThreadBlocked

**Description:** Reports the status of a block thread attempt.

**Platforms:** Windows

---

### VerifyAppsDisabled

**Description:** This event has been deprecated. Fields: Android

**Platforms:** Android

---

### DNSRequestDetectInfo

**Description:** This event is sent whenever a malicious DnsRequest is detected. Fields: Android, iOS

**Platforms:** Android, iOS, Linux

---

### DnsRequestBlocked

**Description:** This event is sent whenever a DnsRequest is blocked. Connection to either the IP or the domain in this request has been blocked. Fields: Android, iOS

**Platforms:** Android, iOS

---

### UserSetProcessBreakOnTermination

**Description:** 

**Platforms:** Windows

---

### SuspiciousPrivilegedProcessHandle

**Description:** Indicates a process has opened a handle to a privileged process with special access rights.

**Platforms:** Windows

---

### FileWrittenAndExecutedInContainer

**Description:** A file was written and later executed in a container.

**Platforms:** Linux, Falcon Container

---

### DwmCompositionResourceExploitAttempt

**Description:** 

**Platforms:** Windows

---

### GenericFileWritten

**Description:** An event that is emitted when a process is done writing to a file that doesn't match a more specific *FileWritten event. These events are currently generated for removable disks only. An event that is emitted when a process is done writing to a file that doesn't match a more specific *FileWritten event. These events are currently generated for removable disks only.

**Platforms:** macOS, Windows

---

### RemediationMonitorScheduledTaskRemoval

**Description:** Notification of a scheduled task persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### ReflectiveDotnetModuleLoad

**Description:** Event generated when .NET module is reflectively (e.g. from a byte array) loaded in a process.

**Platforms:** Windows

---

### HookedAndroidMethodFound

**Description:** An event that indicates that a hooking framework such as Xposed has been found to have been loaded by the FalconMobile application. The FalconMobile application might have been compromised and the device might have been rooted. Fields: Android

**Platforms:** Android

---

### SuspiciousAndroidStackTraceElementFound

**Description:** An event that indicates that a hooking framework has been found via stacktrace analysis and that the FalconMobile application might have been compromised. Fields: Android

**Platforms:** Android

---

### SuspiciousAndroidActivityFound

**Description:** An event that indicates that a currently installed application on the device has been found providing a suspicious Android Activity. Fields: Android

**Platforms:** Android

---

### SuspiciousAndroidSystemPropertyFound

**Description:** An event that indicates that a suspicious system property has been found. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted. Fields: Android

**Platforms:** Android

---

### SuspiciousAppFound

**Description:** An event that indicates that a suspicious application has been found to be installed on the device. Fields: Android

**Platforms:** Android

---

### SuspiciousAndroidLogcatMessageFound

**Description:** An event that indicates that an application log message originating from a suspicious source has been found indicating the FalconMobile application might have been compromised and the device might have been rooted. Fields: Android

**Platforms:** Android

---

### NtfsQueryEaExploitAttempt

**Description:** 

**Platforms:** Windows

---

### NewExecutableWritten

**Description:** This event is generated when an executable file extension is written, whether or not it is truly an executable file type. Any file that ends with a known executable file extension (e.g. .exe, .bat, .scr) will generate this event. The difference between a NewExecutableWritten event and PeFileWritten is that NewExecutableWritten looks for the extension of a file written, while PEFileWritten looks for the PE header in a file that was written.

**Platforms:** Linux, macOS, Windows

---

### RemediationMonitorServiceRemoval

**Description:** Notification of a service persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### AndroidInitServiceRemoved

**Description:** An event that indicates that an init (boot) service has been removed from the system configuration. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted. Fields: Android

**Platforms:** Android

---

### AndroidInitServiceAdded

**Description:** An event that indicates that a new init (boot) service has been added to the system configuration. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted. Fields: Android

**Platforms:** Android

---

### SystemUpdatesBlockedByDNS

**Description:** Indicates that OS updates have been blocked via DNS.

**Platforms:** iOS

---

### SystemUpdatesBlockedByHTTP

**Description:** Indicates that OS updates have been blocked via HTTP.

**Platforms:** iOS

---

### SystemUpdatesBlockedByFilesystem

**Description:** Indicates that OS updates have been blocked via the filesystem.

**Platforms:** iOS

---

### ProcessExecOnRDPFile

**Description:** A PE file was written and executed from an RDP session.

**Platforms:** Windows

---

### SafetyNetVerifyAppsStatus

**Description:** An event that contains information about the status of SafetyNet Verify Apps (Google Play Protect) on the device. Fields: Android

**Platforms:** Android

---

### MemoryProtectionUpdated

**Description:** Triggers if a new executable memory region is mapped which is writable or mapped from a file.

**Platforms:** Linux, Falcon Container

---

### NamespaceChanged

**Description:** 

**Platforms:** Linux, Falcon Container

---

### ProcessSessionCreated

**Description:** 

**Platforms:** Linux, Falcon Container

---

### FileSetMode

**Description:** Indicates the file permissions have been modified via chmod/fchmod/fchmodat.

**Platforms:** Linux, Falcon Container

---

### BMLFeatureData

**Description:** 

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### HostTimeModified

**Description:** 

**Platforms:** Linux, Falcon Container

---

### KernelServiceStarted

**Description:** Indicated that a kernel service was started locally or remotely.

**Platforms:** Windows

---

### RootkitDetectionResponse

**Description:** 

**Platforms:** Windows

---

### MbrOverwriteRawDetectInfo

**Description:** 

**Platforms:** Windows

---

### RegCredAccessDetectInfo

**Description:** 

**Platforms:** Windows

---

### SourceCodeFileWritten

**Description:** 

**Platforms:** Windows, macOS

---

### ArchiveFileContent

**Description:** 

**Platforms:** Windows, macOS

---

### UnixFileWritten

**Description:** Fields: Android

**Platforms:** Android

---

### ScheduledTaskTamperingRegistryOperation

**Description:** 

**Platforms:** Windows

---

### ScriptFileWrittenInfo

**Description:** 

**Platforms:** Windows

---

### SmtpEmailMessage

**Description:** 

**Platforms:** Windows

---

### SessionPatternTelemetry

**Description:** 

**Platforms:** Linux, macOS

---

### PacketFilterAttached

**Description:** 

**Platforms:** Linux, Windows, Linux

---

### FileStatFsInfo

**Description:** 

**Platforms:** Linux

---

### UnixName

**Description:** 

**Platforms:** Linux

---

### Pop3Command

**Description:** 

**Platforms:** Windows, Linux

---

### ThreadPreviousModeMismatch

**Description:** 

**Platforms:** Windows

---

### SigningIdentity

**Description:** 

**Platforms:** iOS

---

### ProcessTokenPrivilegesEdited

**Description:** 

**Platforms:** Windows

---

### SensorTampering

**Description:** Thrown when a tampering event occurs on the sensor.

**Platforms:** Linux, Android

---

### MobileOsForensicsReport

**Description:** 

**Platforms:** iOS, Android

---

### IntrusivePackageDiscovered

**Description:** Fields: Android

**Platforms:** Android

---

### IntrusiveProcessDiscovered

**Description:** 

**Platforms:** iOS

---

### MotwWritten

**Description:** 

**Platforms:** Windows

---

### SignInfoWithContext

**Description:** Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains information about the signing-state of an image.

**Platforms:** Windows, macOS

---

### SuspiciousCredentialModuleLoad

**Description:** An indicator event fired when suspicious credential module activity is detected, which means the process opened a handle to the LSASS process and loaded one of its DLLs for symbolic resolution of protected LSASS resources. The name of the DLL that was loaded is in the ImageFileName field This event also contains data from the offending application, whose name is stored in TargetFileName

**Platforms:** Windows

---

### SignInfoWithCertAndContext

**Description:** Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains information about the signing-state of an image.

**Platforms:** macOS, Windows

---

### InjectedThreadFromUnsignedModule

**Description:** This event contains information about a thread that was injected into a process from an unsigned module. It combines relevant information from the InjectedThread and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### SuspiciousRawDiskReadFromUnsignedModule

**Description:** This event contains information about an unsigned module reading a target file using raw disk access. It combines relevant information from the SuspiciousRawDiskRead and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### FileIntegrityMonitorRuleMatched

**Description:** An event that contains data about a change to a directory, file, or registry key. Used with the FileVantage service.

**Platforms:** macOS, Windows, Linux

---

### MacroContentInfo

**Description:** Description: Provides information about a macro extracted when an Office file is written or opened

**Platforms:** Windows

---

### SensorSettingsUpdate

**Description:** 

**Platforms:** Windows, macOS

---

### IdpConnectionsOverloadNotification

**Description:** IDP Traffic Inspection detected more than 15,000 concurrent connections in active enforcement mode.

**Platforms:** Windows

---

### ProcessTreeCompositionPatternTelemetry

**Description:** 

**Platforms:** Windows

---

### K8SAdmissionReviewResult

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### K8SAdmissionReviewResultPrime

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### RemoteCommandResponse

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### ProcessRollup2Stats

**Description:** Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only generates ProcessRollup2 events. When a process finishes running, the sensor generates and sends a ProcessRollup2 event. Linux sensors send far more ProcessRollup2 events than Windows (roughly 20x as many), so rather than send events for every process on those hosts, the sensor sends an initial ProcessRollup2 event, followed 60 minutes later by a ProcessRollup2Stats event with a SHA256 hash and the count of how many times the hash executed in the last 60 minutes. Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only generates ProcessRollup2 events. When a process finishes running, the sensor generates and sends a ProcessRollup2 event. Mac sensors send far more ProcessRollup2 events than Windows (roughly 20x as many), so rather than send events for every process on those hosts, the sensor sends an initial ProcessRollup2 event, followed 10 minutes later by a ProcessRollup2Stats event with a SHA256 hash and the count of how many times the hash executed in the last 10 minutes.

**Platforms:** Linux, Falcon Container, macOS

---

### SuspiciousLackOfProcessRollupEvents

**Description:** This event is emitted if we don't see any ProcessRollup2 events for a long time.

**Platforms:** Windows

---

### AgentConnect

**Description:** This event is generated when the sensor successfully connects to the cloud.

**Platforms:** Windows Legacy, Windows, Linux, Falcon Container, Kubernetes, macOS, Android, iOS, Windows Legacy, Vmcluster, iOS, Linux, Falcon Container, Android, Kubernetes, macOS, Windows

---

### IsoExtensionFileWritten

**Description:** 

**Platforms:** Windows

---

### ImgExtensionFileWritten

**Description:** 

**Platforms:** Windows

---

### DcBluetoothDeviceConnectedDetails

**Description:** 

**Platforms:** Windows, macOS

---

### FirmwareImageAnalyzed

**Description:** Indicates that analysis of a firmware image was completed.

**Platforms:** Windows, macOS

---

### DirectoryTraversalOverSMB

**Description:** This event indicates Directory traversal over an SMB session detected.

**Platforms:** Windows

---

### CrashNotification

**Description:** The sensor sends this to the cloud when the Diagnostics Actor notices that the machine has booted with indication of previous session ending in a crash.

**Platforms:** macOS, Windows

---

### OciContainerComplianceInfo

**Description:** 

**Platforms:** Linux, Falcon Container

---

### IdpDcPerfReport

**Description:** This event reports Domain Controller performance counter.

**Platforms:** Windows

---

### FileRenameInfo

**Description:** This event is generated when a file is renamed. Only sent as part of a detection.

**Platforms:** Linux, Falcon Container, macOS, Windows

---

### SensorSelfDiagnosticTelemetry

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### SpotlightEntityBatch

**Description:** Single Event consisting of a list of Spotlight Entity State data packaged for optimal size and part of a larger set of batch events that will be processed in Cloud.

**Platforms:** Linux, Windows, macOS

---

### CustomIOADomainNameDetectionInfoEvent

**Description:** An event triggered by a Domain Name custom IOA rule.

**Platforms:** Windows, macOS, Linux

---

### CustomIOAFileWrittenDetectionInfoEvent

**Description:** An event triggered by a File Creation custom IOA rule.

**Platforms:** Windows, macOS, Linux

---

### CustomIOABasicProcessDetectionInfoEvent

**Description:** An event triggered by a Process Creation custom IOA rule.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### CustomIOANetworkConnectionDetectionInfoEvent

**Description:** An event triggered by a Network Connection custom IOA rule.

**Platforms:** Windows, macOS, Linux

---

### RegistryOperationBlocked

**Description:** An event that indicates that a registry operation has been blocked using a callback filter.

**Platforms:** Windows

---

### RegistryOperationDetectInfo

**Description:** An event that describes a registry operation blocked using a callback filter.

**Platforms:** Windows

---

### MacroDetectInfo

**Description:** Event description: Provides more context around the macro content that was detected.

**Platforms:** Windows

---

### UmppcDetectInfo

**Description:** An event that describes a UMPPC-based detection.

**Platforms:** Windows

---

### SnapshotVolumeMounted

**Description:** Information about a snapshot volume that was just mounted.

**Platforms:** Windows

---

### ImpersonationTokenInfo

**Description:** ImpersonationTokenInfo represents a security context for a general impersonation activity. Each ImpersonationTokenInfo can be linked to a corresponding UserIdentity by using the (UserSid, AuthenticationId) tuple.

**Platforms:** Windows

---

### UserIdentity

**Description:** The UserIdentity event is generated when a user logs in to a host. It conveys important security-related characteristics associated with a user to the CrowdStrike cloud, such as the user name. It’s normally generated once per security principal, and is thus not on its own a sign of a suspicious activity.

**Platforms:** macOS, Windows, Forensics, Linux

---

### DriverLoad

**Description:** An event to notify of a driver load that will be used for detection. Fields: Forensics

**Platforms:** Forensics, Windows

---

### UserAccountDeleted

**Description:** User account deleted. This event is generated when a user account is deleted. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Fields: Forensics

**Platforms:** Forensics, Windows, Linux

---

### ProcessTrace

**Description:** 

**Platforms:** Linux, Falcon Container

---

### InstanceMetadata

**Description:** Metadata information about the instance on which the sensor is running.

**Platforms:** macOS, Kubernetes, Windows, Linux, Falcon Container

---

### FileAccessOperationOverSMB

**Description:** File access operations over a SMB user session.

**Platforms:** Windows

---

### K8SSnapshot

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### K8SWatchStarted

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### K8SResource

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### K8SWatchStopped

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### IdpEntityRiskScoreChange

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### HostedServiceStarted

**Description:** This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is started by the service control manager (SCM). ServiceDisplayName, TargetProcessId, ImageFileName and TargetThreadId are all for the new service. TargetThreadId is the primary thread of the new hosted service. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Also, starting and stopping hosted services multiple times during boot might not always show up in this event due to caching done by the SCM.

**Platforms:** Windows

---

### NetShareAdd

**Description:** This event is generated when a network share is added or modified on a host.

**Platforms:** Windows

---

### UserAccountCreated

**Description:** This event is generated when a new user account is created. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows, Linux

---

### ServiceStarted

**Description:** This event is generated when a standalone service is started by the service control manager (SCM). ServiceDisplayName, TargetProcessId, ImageFileName and CommandLine are all for the new service. The data will indicate the initial process (command- line tool, custom utility, or GUI application) or remote address/host name that resulted in this action.

**Platforms:** Windows

---

### ScheduledTaskDeleted

**Description:** This event is sent when Falcon has detected that a scheduled task has been removed from the machine. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Note that the context here is not sufficient to determine full details on the task being removed (that is captured in ScheduledTaskRegistered), but does show the task name and originator info.

**Platforms:** Windows

---

### FirewallSetRule

**Description:** A firewall rule has been created or modified, such as a rule allowing inbound RDP connections. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### FirewallDeleteRule

**Description:** A firewall rule has been deleted, such as removing a rule preventing inbound RDP connections. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### FirewallChangeOption

**Description:** A firewall configuration option has been changed, such as enabling or disabling the firewall. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### UserAccountAddedToGroup

**Description:** This event is generated when an existing user account is added to an existing group. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. The group RID will indicate which group this user was added to. Of interest, for example, is a user being added to the “Administrators” group.

**Platforms:** Windows, Linux

---

### BITSJobCreated

**Description:** The event is generated when a Background Intelligent Transfer Service (BITS) download is created and a new file is dropped on the system.

**Platforms:** Windows

---

### EventLogCleared

**Description:** This event is generated when a Windows event log is cleared.

**Platforms:** Windows

---

### ScheduledTaskRegistered

**Description:** This event is sent when Falcon detects that a scheduled task has been added to the machine, either locally or remotely. This includes things added via the at command (at.exe) or scheduled tasks (schtasks.exe). The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. This service has multiple versions over time from Windows 7 to Windows 10, so some fields may not be available in all versions. The raw TaskXml will always be available, which should be a superset of the other ‘Task’ fields.

**Platforms:** Windows

---

### NetShareDelete

**Description:** This event is generated when a network share is removed from a host.

**Platforms:** Windows

---

### NetShareSecurityModify

**Description:** This event is generated when the security descriptor of a network share is changed.

**Platforms:** Windows

---

### VolumeSnapshotCreated

**Description:** A volume snapshot has been created.

**Platforms:** Windows

---

### VolumeSnapshotDeleted

**Description:** A volume snapshot has been deleted.

**Platforms:** Windows

---

### VolumeSnapshotOperationBlocked

**Description:** Event describing a snapshot volume block operation. IFN and CL are based upon the RpcProcessId, in VSS operations only RPC tree is relevant.

**Platforms:** Windows, Windows

---

### MemoryScanErrorEvent

**Description:** 

**Platforms:** Windows

---

### ServiceStopped

**Description:** This event is emitted when a standalone service is stopped by the service control manager (SCM). Unfortunately, the sensor is not currently capable of identifying who requested this operation. However, it can be used to confirm that this is a service stopping vs. a service crashing or being terminated.

**Platforms:** Windows

---

### SuspiciousPeFileWritten

**Description:** A suspicious PE image file was written to disk.

**Platforms:** Windows

---

### PodInfo

**Description:** Metadata associated with a Kubernetes pod.

**Platforms:** Linux, Falcon Container

---

### DmpFileWritten

**Description:** Emitted when a process is done writing a dump file. PidFromCommandLine will be enhanced in some cases to extract out the pid from the commandline of the writing process if possible.

**Platforms:** Windows, macOS, Linux

---

### SevenZipFileWritten

**Description:** This event is generated when a 7ZIP file type (.7zip) is written to disk.

**Platforms:** Windows, macOS, Linux

---

### PdfFileWritten

**Description:** This event is generated when a PDF file type (.pdf) is written to disk.

**Platforms:** Windows, macOS, Linux

---

### OleFileWritten

**Description:** This event is generated when a file a Microsoft Office (Pre-Office 2007) file type is written to disk.

**Platforms:** Windows, macOS, Linux

---

### RarFileWritten

**Description:** Emitted when a process is done writing a RAR file.

**Platforms:** Windows, macOS, Linux

---

### OoxmlFileWritten

**Description:** This event is generated when a Microsoft Office (Post-Office 2007) file type is written to disk.

**Platforms:** Windows, macOS, Linux

---

### ZipFileWritten

**Description:** This event is generated when a ZIP file type (.zip) is written to disk.

**Platforms:** Windows, macOS, Linux

---

### RtfFileWritten

**Description:** Emitted when a process is done writing an RTF file.

**Platforms:** Windows, macOS, Linux

---

### PeFileWritten

**Description:** This event is generated when a Windows Portable Executable file type is written to disk. The difference between a NewExecutableWritten event and PeFileWritten is that NewExecutableWritten looks for the extension of a file written, while PEFileWritten looks for the PE header in a file that was written.

**Platforms:** macOS, Linux, Windows

---

### XarFileWritten

**Description:** Emitted when a process is done writing a Xar file. macOS installer files are of this type.

**Platforms:** Windows, macOS, Linux

---

### BZip2FileWritten

**Description:** Emitted when a process is done writing a BZip2 file.

**Platforms:** Windows, macOS, Linux

---

### MachOFileWritten

**Description:** Emitted when a process is done writing a MachO file.

**Platforms:** Windows, macOS, Linux, Windows, macOS, Linux

---

### IdwFileWritten

**Description:** Emitted when a process is done writing an IDW file.

**Platforms:** Windows

---

### DwgFileWritten

**Description:** An event that is emitted when a process is done writing to a DWG file.

**Platforms:** Windows

---

### ELFFileWritten

**Description:** Emitted when a file has been written that contains a real ELF image header.

**Platforms:** Windows, macOS, Android, Linux

---

### GzipFileWritten

**Description:** Emitted when a file has been written that contains a real Gzip image header.

**Platforms:** Windows, macOS, Linux

---

### JavaClassFileWritten

**Description:** Emitted when a process is done writing a Java Class file.

**Platforms:** Windows, macOS, Linux

---

### CabFileWritten

**Description:** Emitted when a process is done writing a Microsoft Cabinet (CAB) file.

**Platforms:** macOS, Windows, Linux

---

### ArcFileWritten

**Description:** Emitted when a process is done writing a ARC file.

**Platforms:** Windows, macOS, Linux

---

### TiffFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### ArjFileWritten

**Description:** Emitted when a process is done writing a ARJ file.

**Platforms:** macOS, Windows, Linux

---

### VmdkFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### JpegFileWritten

**Description:** Emitted when a process is done writing a Jpeg image file.

**Platforms:** Windows, macOS, Linux

---

### BmpFileWritten

**Description:** Emitted when a process is done writing a BMP image file.

**Platforms:** Windows, macOS, Linux

---

### GifFileWritten

**Description:** Emitted when a process is done writing a GIF image file.

**Platforms:** macOS, Windows, Linux

---

### PngFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### MSXlsxFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### MSPptxFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### VdiFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### MSDocxFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### MSVsdxFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### DxfFileWritten

**Description:** 

**Platforms:** Windows, Windows

---

### RpmFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### DebFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### BlfFileWritten

**Description:** Emitted when a process is done writing an BLF file.

**Platforms:** macOS, Windows, Linux

---

### MsiFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### LnkFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### DmgFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### EmailFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### EmailArchiveFileWritten

**Description:** 

**Platforms:** macOS

---

### EseFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### RegistryHiveFileWritten

**Description:** 

**Platforms:** Windows

---

### ADExplorerFileWritten

**Description:** 

**Platforms:** Windows

---

### WebScriptFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### CrxFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### PythonFileWritten

**Description:** 

**Platforms:** Windows

---

### HttpRequestDetect

**Description:** An event that indicates a detection on an HTTP(S) request.

**Platforms:** Windows

---

### HttpRequest

**Description:** 

**Platforms:** Linux, macOS

---

### DcBluetoothDeviceProperties

**Description:** This event contains properties for a connected Bluetooth device.

**Platforms:** macOS, Windows

---

### IdpCloudHealthStatus

**Description:** 

**Platforms:** Windows

---

### DiskCapacity

**Description:** An event that contains information about disks, the quantity of disks, and the storage capability of disks. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in disk parameters is detected. An event that contains information about disks, the quantity of disks, and the storage capability of disks that are locally attached to a system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in disk parameters is detected.

**Platforms:** Windows, Linux

---

### MemoryMapped

**Description:** Triggers when an executable memory region is mapped.

**Platforms:** Linux, Falcon Container

---

### TlsClientHello

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### SmtpAttachment

**Description:** 

**Platforms:** Linux

---

### SmtpCommand

**Description:** 

**Platforms:** Linux

---

### FtpCommand

**Description:** 

**Platforms:** Linux

---

### NetworkLinkConfigGetLink

**Description:** 

**Platforms:** Linux

---

### NetworkLinkConfigGetAddress

**Description:** 

**Platforms:** Linux

---

### RansomwareFileAccessPattern

**Description:** Helper event for ransomware file access patterns.

**Platforms:** Windows

---

### AsepFileChangeScanInfo

**Description:** Rollup indicating an ASEP file has been created or modified but there was no template detection on the contents.

**Platforms:** macOS, macOS

---

### BPFCommandIssued

**Description:** Emitted when a process executes bpf syscall.

**Platforms:** Linux, Falcon Container

---

### FileSystemOperationBlocked

**Description:** An event that indicates that a file system operation has been blocked.

**Platforms:** macOS, Windows

---

### SecureTrafficDecrypted

**Description:** An event that contains certificate info for the compromised network connection. Fields: Android, iOS

**Platforms:** Android, iOS

---

### FileSystemOperationDetectInfo

**Description:** Informational event for a file system operation detection.

**Platforms:** Windows

---

### ModuleBlockedEventWithPatternId

**Description:** This event adds a potential reason for blocking (as a PatternId) to module blocking information.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### ModuleBlockedEvent

**Description:** This event is sent to inform cloud about the fact that given module (identified by hash) was blocked.

**Platforms:** macOS, Windows, Linux, Falcon Container

---

### ChannelVersionRequired

**Description:** This event informs the cloud information about the state of a channel on the sensor. The cloud will use this event to decide whether to send the sensor updated channel data.

**Platforms:** Windows, macOS, Linux, Falcon Container, Android, Kubernetes, Vmcluster, iOS

---

### LfoUploadDataUnneeded

**Description:** Emitted when the sensor initiates a file upload, but the cloud has determined the file is not needed. A specific cloud reason will be provided in LfoUploadCloudStatus.

**Platforms:** Windows, macOS, Linux, Android, Kubernetes, Vmcluster

---

### LfoUploadDataComplete

**Description:** Emitted when the LFOUploadActor has successfully uploaded a file to the cloud.

**Platforms:** Windows, macOS, Linux, Android, Kubernetes, Vmcluster

---

### LfoUploadDataFailed

**Description:** Emitted when the sensor has detected error(s) and has decided not to stop uploading a file to the cloud. LfoUploadExtendedStatus will indicate the detailed failure reason.

**Platforms:** Windows, macOS, Linux, Android, Kubernetes, Vmcluster

---

### ProvisioningChannelVersionRequired

**Description:** This event informs the cloud about the state of a channel on the sensor during provisioning. It is only sent when the sensor is in an unprovisioned state.

**Platforms:** Linux, Falcon Container, macOS, Windows, iOS, Android

---

### LfoUploadStart

**Description:** Emitted when the sensor initiates a file upload.

**Platforms:** Windows, macOS, Linux, Android, Kubernetes, Vmcluster

---

### NetworkListenIP4

**Description:** This event is generated when an application establishes a socket in listening mode This event is generated when an application establishes a socket in listening mode.

**Platforms:** Windows, macOS, Android, Linux, Falcon Container, Forensics, ChromeOS

---

### NetworkConnectIP6

**Description:** This event is created whenever an application using a connection-oriented protocol attempts a remote connection (e.g., via a call to the connect() function) or a connectionless protocol first attempts to transmit a message (e.g., via a call to the sendto() function). This event is generated when an application attempts a remote connection.

**Platforms:** Windows, macOS, Android, iOS, Forensics, ChromeOS, Linux, Falcon Container

---

### NetworkReceiveAcceptIP4

**Description:** This event is generated when an application using a connection-oriented protocol attempts to accept a remote connection request (e.g., via a call to the accept() function) or a connectionless protocol attempts to process the first datagram received.

**Platforms:** Windows, macOS, Android, Linux, Falcon Container, Forensics

---

### NetworkReceiveAcceptIP6

**Description:** This event is created whenever an application using a connection-oriented protocol attempts to accept a remote connection request (e.g., via a call to the accept() function) or a connectionless protocol attempts to process the first datagram received.

**Platforms:** Windows, macOS, Android, Linux, Falcon Container, Forensics

---

### NetworkCloseIP4

**Description:** An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 5 minutes using UDP. IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 2 minutes using UDP.IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state.

**Platforms:** Windows, Android, Forensics, macOS, Linux, Falcon Container

---

### NetworkConnectIP4

**Description:** This event is generated when an application attempts a remote connection.

**Platforms:** Windows, macOS, Android, iOS, Linux, Falcon Container, Forensics, ChromeOS

---

### NetworkListenIP6

**Description:** This event is created whenever an application using a connection-oriented protocol establishes a socket in listening mode (e.g., via a call to the listen() function).

**Platforms:** Windows, macOS, Android, Linux, Falcon Container, Forensics, ChromeOS

---

### FirewallSetRuleIP6

**Description:** An event that indicates an IPv6 firewall rule has been created. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallDeleteRuleIP4

**Description:** An event that notifies that an Ipv4 firewall rule has been deleted. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallDeleteRuleIP6

**Description:** An event that notifies that an Ipv6 firewall rule has been deleted. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallSetRuleIP4

**Description:** An event that indicates an IPv4 firewall rule has been created. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### NetworkCloseIP6

**Description:** An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 2 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 5 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 10 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state.

**Platforms:** Linux, Falcon Container, Windows, Forensics, macOS, Android

---

### NetworkConnectIP4Blocked

**Description:** This event is created whenever a NetworkConnectIP4 event is blocked. This event is created whenever a NetworkConnectIP4 event is blocked because of the IP or the domain/URL being accessed.

**Platforms:** Windows, Android, macOS, iOS

---

### NetworkConnectIP6Blocked

**Description:** This event is created whenever a NetworkConnectIP6 event is blocked. This event is created whenever a NetworkConnectIP6 event is blocked because of the IP or the domain/URL being accessed. Fields: Android

**Platforms:** Android, Windows, macOS, iOS

---

### NetworkConnectIP4DetectInfo

**Description:** This event is sent whenever a connection to malicious IP4 address is detected. Fields: Android

**Platforms:** Android, iOS

---

### NetworkConnectIP6DetectInfo

**Description:** This event is sent whenever a connection to malicious IP6 address is detected. Fields: Android

**Platforms:** Android, iOS

---

### RemediationActionKillIP4Connection

**Description:** Sensor attempted to kill a connection to a malicious IPv4 address. No further data will be sent or received on the connection. Fields: Android

**Platforms:** Android, iOS

---

### RemediationActionKillIP6Connection

**Description:** Sensor attempted to kill a connection to a malicious IPv6 address. No further data will be sent or received on the connection. Fields: Android

**Platforms:** Android, iOS

---

### CreateSocket

**Description:** This event is created whenever a process creates a socket.

**Platforms:** Linux, Falcon Container, Forensics

---

### NetworkOutboundPortScanDetectInfo

**Description:** 

**Platforms:** Windows

---

### RawBindIP6

**Description:** IPv6 network binding event. Terminating socket is in raw mode. An event that is created when an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). It is a more specific version of the event NetworkBindIP6 indicating a socket is in raw mode. IPv6 is the source of the connection/connectionless protocol in this event. A NetworkBindIP6 event is created whenever an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). The event's ConnectionFlags field describes the parameters of that bind operation. A socket that is bound has not performed any network activity per se. Only a subsequent call to listen() or connect() generates network activity through the bound socket. The attributes of the bind, such as promiscuous mode or raw socket, are available in the ConnectionFlags field. Fields: Forensics

**Platforms:** Forensics, Linux, Falcon Container, Android, macOS, Windows

---

### RawBindIP4

**Description:** IPv4 network binding event. Terminating socket is in raw mode. An event that is created when an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). It is a more specific version of the event NetworkBindIP4 indicating a socket is in raw mode. IPv4 is the source of the connection/connectionless protocol in this event. A NetworkBindIP4 event is created whenever an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). The event's ConnectionFlags field describes the parameters of that bind operation. A socket that is bound has not performed any network activity per se. Only a subsequent call to listen() or connect() generates network activity through the bound socket. The attributes of the bind, such as promiscuous mode or raw socket, are available in the ConnectionFlags field. Fields: Forensics

**Platforms:** Forensics, Android, Windows, macOS, Linux, Falcon Container

---

### NewScriptWritten

**Description:** Emitted when a process is done writing a script file, as determined by #! at the start of the file. This event is generated when a new script is written (e.g. .js, .aspx, .bat, .ps1, .vbs, .lua).

**Platforms:** Linux, macOS, Windows

---

### PatternHandlingError

**Description:** This event is emitted when an error occurs in processing a behavior.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### ProcessPatternTelemetry

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### ActiveDirectoryIncomingPsExecExecution2

**Description:** Indicates remote code execution on a domain controller using PsExec. This event is generated based on a REMOTE_INTERACTIVE type ActiveDirectoryIncomingDceRpcEpmRequest event that correlates with an ActiveDirectoryServiceAccessRequest event to the Common Internet File System (CIFS) or a host Service Principal Name (SPN). This event replaces the ActiveDirectoryIncomingPsExecExecution event, which is now obsolete.

**Platforms:** Windows

---

### IdpPolicyAlertRuleMatch

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### BrowserInjectedThread

**Description:** Indicates a browser process injected a thread into some other process.

**Platforms:** Windows

---

### KernelCallbackTableUpdate

**Description:** An event that indicates that the ProcessEnvironmentBlock KernelCallbackTable field has been changed from its prior value. This might indicate an attempt to alter one of the callback routines.

**Platforms:** Windows, Windows

---

### FileDetectInfo

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### IdpPolicyFederatedAccessRuleMatch

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### BootLoopProtectionTelemetry

**Description:** 

**Platforms:** Windows

---

### LightningUnresponsiveStatus

**Description:** 

**Platforms:** Windows, macOS

---

### AndroidEnterpriseInfo

**Description:** This event contains metadata related to the state of the device as reported by the Android Management API (AMAPI). Fields: Android

**Platforms:** Android

---

### InjectedThread

**Description:** This event is generated when one process injects an execution thread into another process. While often associated with malicious activity, this is also common behavior for certain core operating system processes.

**Platforms:** Windows

---

### JavaInjectedThread

**Description:** This event is generated when Java injects a thread into another process.

**Platforms:** Windows

---

### DocumentProgramInjectedThread

**Description:** Indicates a document program process injected a thread into some other process.

**Platforms:** Windows

---

### ActiveDirectoryAuthenticationFailure

**Description:** Indicates that the Domain Controller handled one or more failed authentications by an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryInteractiveDomainLogon

**Description:** Indicates an interactive logon to an Active Directry domain handled by a Domain Controller. The interactive logon is combined of initial authentication following by some service access events.

**Platforms:** Windows

---

### SetWindowsHook

**Description:** An event that is sent from the sensor when a user mode program attempts to set a windows hook.

**Platforms:** Windows

---

### ScriptControlDetectInfo

**Description:** This event is sent when Falcon has detected malicious script content being executed on the host. This event provides the details of exactly what content was detected.

**Platforms:** macOS, Linux, Windows

---

### ActiveDirectoryAuthentication

**Description:** Indicates that the Domain Controller handled one or more successful authentications by an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryServiceAccessRequestFailure

**Description:** Indicates that the Domain Controller handled one or more failed service requests from an account on an endpoint. The requests were to a service identified by an Active Directory account.

**Platforms:** Windows

---

### CloudAssociateTreeIdWithRoot

**Description:** This event is generated when there is a detection in the CrowdStrike cloud. This event has a data field called PatternId which contains a pattern ID. Pattern IDs are associated with a detection.

**Platforms:** Windows, Linux, Falcon Container, macOS, ChromeOS

---

### K8SProductConfig

**Description:** Fields: Kubernetes

**Platforms:** Kubernetes

---

### IdpTelemetryData

**Description:** 

**Platforms:** Windows

---

### IdpPacketDiversionLdapsConnectionsOverloadNotification

**Description:** 

**Platforms:** Windows

---

### DataProtectionArchiveAssessed

**Description:** Describes an archive processed by Data Protection assessment. Top level event fields are properties of enclosing archive file (e.g. Size)

**Platforms:** Windows, macOS

---

### FileTimestampsModified

**Description:** An event that is emitted when a change occurs to the timestamps of a file.

**Platforms:** Windows, Linux, Falcon Container

---

### VMClusterInfo

**Description:** Event sent periodically to let the cloud know that the sensor is running with the following VM cluster data. Fields: Vmcluster

**Platforms:** Vmcluster

---

### VmcSensorStatus

**Description:** This event is sent to provide VMC sensor operational status. Fields: Vmcluster

**Platforms:** Vmcluster

---

### VmcVmAsset

**Description:** This event is sent to provide VMware vCenter VM information. Fields: Vmcluster

**Platforms:** Vmcluster, Windows

---

### InboundHttpParsingStatus

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### InstalledBrowserExtension

**Description:** An event that contains information about installed browser extensions, including updates and removals. The event is sent when the sensor connects and every 48 hours thereafter. If no browser extensions are identified, a default event indicating no-extension-available is sent to the CrowdStrike cloud.

**Platforms:** Windows, macOS

---

### BrowserExtensionStatus

**Description:** 

**Platforms:** macOS, Windows, macOS, Linux, Falcon Container, Windows Legacy

---

### AssociateIndicator

**Description:** This event is generated when the sensor generates an indicator. An indicator is like a detection event (AssociateTreeIdWithRoot) except that it is not necessarily malicious, either because it is just an indicator (e.g. when a process opens the Recycle Bin) or because CrowdStrike is not yet confident enough in the indicator to trigger it as a detection. Note that a detection, unlike an indicator, establishes a detection tree (AssociateTreeIdWithRoot) which causes the sensor to send additional information for that process tree for analysis/hunting purposes. An indicator is just a single event that has no other sensor impact.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### FirewallRuleIP6Matched

**Description:** An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match. An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match.

**Platforms:** Windows, macOS, Linux

---

### FirewallRuleIP4Matched

**Description:** An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match. An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match.

**Platforms:** Windows, macOS, Linux

---

### NamedMutantHandleClosedTelemetry

**Description:** An event that indicates that a process closed a handle to a known bad named mutex.

**Platforms:** Windows, Windows

---

### ProcessControl

**Description:** 

**Platforms:** Linux, Falcon Container

---

### ClassifiedModuleLoad

**Description:** The ClassifiedModuleLoad event provides information about a module which has been loaded into a process's memory space. It is only generated for 'classified' module loads, that is module loads that are interesting enough for us to cloud.

**Platforms:** Windows

---

### ProcessExecOnPackedExecutable

**Description:** An event that contains telemetry data emitted on execution of a PE file which is known to be packed. The packer type is indicated by the FileSubType field.

**Platforms:** Windows

---

### IdpCloudHealthConfigurationsGetResponse

**Description:** 

**Platforms:** Windows

---

### ModuleDetectInfo

**Description:** This event identifies a scenario that would be a blocking prevention if more rigorous settings were active.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### AppSideLoaded

**Description:** An event that contains the package name and installer info of the app that has been installed outside of the Google PlayStore. Fields: Android

**Platforms:** Android

---

### MobileAppIdentifiers

**Description:** An event that describes details about a mobile application package. Fields: Android

**Platforms:** Android

---

### RegValueQueryDetectInfo

**Description:** 

**Platforms:** Windows

---

### WmiQueryDetectInfo

**Description:** 

**Platforms:** Windows

---

### DriverLoadedV2DetectInfo

**Description:** 

**Platforms:** Windows, Windows

---

### DotnetModuleLoadDetectInfo

**Description:** 

**Platforms:** Windows

---

### PtTelemetry

**Description:** 

**Platforms:** Windows

---

### ModuleLoadV3DetectInfo

**Description:** Additional information for detections from the Module Load V3 template.

**Platforms:** Windows

---

### IdpDcTiConfiguration

**Description:** 

**Platforms:** Windows

---

### SmbServerShareOpenedEtw

**Description:** An event that indicates a remote machine opening a local share. This event is supported on all Windows platform except 8.1 and Server 2012 R2.

**Platforms:** Windows

---

### IdpWatchdogRemediationActionTaken

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionTakenForMemory

**Description:** 

**Platforms:** Windows

---

### DBusMessage

**Description:** An event that generates telemetry that provides visibility into D-Bus messages flowing over local Unix sockets between processes. The sensor will produce events for each message and apply any relevant detections.

**Platforms:** Linux

---

### FirewallRuleIP4

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### InboundHttpHeader

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### InternetExposureData

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### SyntheticSystemdServiceCreated

**Description:** 

**Platforms:** Linux

---

### SystemdTimerDeleted

**Description:** 

**Platforms:** Linux

---

### RouteIP6

**Description:** IPv6 Route entry. Fields: Forensics

**Platforms:** Forensics

---

### DnsServer

**Description:** DNS server IP addresses. Fields: Forensics

**Platforms:** Forensics

---

### BrowserProxyInfo

**Description:** Browser proxy information. Fields: Forensics

**Platforms:** Forensics

---

### SpotlightSearchEntry

**Description:** Per-user spotlight search information. Fields: Forensics

**Platforms:** Forensics

---

### RegSystemConfigKeyUpdate

**Description:** 

**Platforms:** Windows

---

### SudoCommandAttempt

**Description:** 

**Platforms:** macOS

---

### NamedPipeDetectInfo

**Description:** Named pipe detect telemetry event

**Platforms:** Windows

---

### NetworkEndPointDataUsage

**Description:** This event has total counts of sent/received octets/packets to/from the network-attached end point during active connection. The counting window is the life of the end point. Fields: Forensics

**Platforms:** Forensics

---

### UsbDeviceInfo

**Description:** Information on each USB device attachment. Fields: Forensics

**Platforms:** Forensics

---

### UserAccountRemovedFromGroup

**Description:** 

**Platforms:** Linux, Windows

---

### SensorEnteredSafemode

**Description:** 

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### PtyDetached

**Description:** 

**Platforms:** Linux

---

### SystemdServiceCreated

**Description:** 

**Platforms:** Linux

---

### IdpCloudHealthCheck

**Description:** 

**Platforms:** Windows

---

### SmbServerLocalNamedPipeOpenedEtw

**Description:** 

**Platforms:** Windows

---

### OpenDirectoryAttributeSet

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryAttributeRemove

**Description:** 

**Platforms:** macOS

---

### RegGenericKeyUpdate

**Description:** 

**Platforms:** Windows

---

### TerminalSavedStateInfo

**Description:** MacOS terminal saved state information. Fields: Forensics

**Platforms:** Forensics

---

### OpenDirectoryAttributeAdd

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryGroupSet

**Description:** 

**Platforms:** macOS

---

### ActiveDirectoryAuditGpoModified

**Description:** 

**Platforms:** Windows

---

### FirewallRuleIP6

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### KernelParameter

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### UserGroupCreated

**Description:** 

**Platforms:** Linux

---

### SystemdServiceDeleted

**Description:** 

**Platforms:** Linux

---

### ScheduledTaskInfo

**Description:** Scheduled windows tasks. Fields: Forensics

**Platforms:** Forensics

---

### ProcessDataUsage

**Description:** Measurements and statistics of data traffic sent and received to/from the target process. Fields: Forensics

**Platforms:** Forensics

---

### WSLVMStopping

**Description:** The Linux Virtual Machine Root Namespace is stopping.

**Platforms:** Windows

---

### SyntheticSystemdTimerCreated

**Description:** 

**Platforms:** Linux, Windows

---

### NetShareInfo

**Description:** Shared resource information. Fields: Forensics

**Platforms:** Forensics

---

### OsUpdateTimestamp

**Description:** Operating system update timestamp. Fields: Forensics

**Platforms:** Forensics

---

### NetworkDnsSuffix

**Description:** A network suffix name in the configured DNS suffix list. Fields: Forensics

**Platforms:** Forensics

---

### NetworkHostsFileEntry

**Description:** A host name entry in the network hosts file. Fields: Forensics

**Platforms:** Forensics

---

### ActiveDirectoryAuditPasswordModificationAttempt

**Description:** 

**Platforms:** Windows

---

### ProcessSignal

**Description:** 

**Platforms:** Linux

---

### ProcessInjection

**Description:** An event that indicates that a remote process wrote and executed code.

**Platforms:** Windows

---

### SpotlightEntitySystemState

**Description:** Spotlight Entity heart-beat event to notify cloud of current state with last synced batch and Channel file version information.

**Platforms:** Windows, macOS, Linux

---

### ConfigurationProfileModified

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryDeleteUser

**Description:** 

**Platforms:** macOS

---

### LogonBehaviorCompositionDetectInfo

**Description:** 

**Platforms:** Windows

---

### OpenDirectoryGroupAdd

**Description:** 

**Platforms:** macOS

---

### DnsCache

**Description:** An entry observed within the system's DNS Cache. Fields: Forensics

**Platforms:** Forensics

---

### WindowsTimelineEntryTimestamp

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### BrowserAccountInfo

**Description:** Browser user account information. Fields: Forensics

**Platforms:** Forensics

---

### BrowserHistoryClearInfo

**Description:** Browser history clearing event information. Fields: Forensics

**Platforms:** Forensics

---

### ForensicsCollectorOffline

**Description:** Final event of a Forensics collection. Fields: Forensics

**Platforms:** Forensics

---

### ForensicsCollectorOnline

**Description:** Marks the beginning of a Forensics collection. Fields: Forensics

**Platforms:** Forensics

---

### WmiQuery

**Description:** Windows Management Instrumentation (WMI) query status. Fields: Forensics

**Platforms:** Forensics

---

### FilesStatisticInfo

**Description:** Files statistic information. Fields: Forensics

**Platforms:** Forensics

---

### BrowserCookieInfo

**Description:** Browser tracking cookie information. Fields: Forensics

**Platforms:** Forensics

---

### WSLDistributionUnregistered

**Description:** A user unregisters a Linux distribution.

**Platforms:** Windows

---

### SystemdTimerCreated

**Description:** 

**Platforms:** Linux

---

### WSLDistributionStopping

**Description:** The Linux distribution is stopping.

**Platforms:** Windows

---

### DriverLoadBlocked

**Description:** Event which indicates we successfully blocked a driver from loading.

**Platforms:** Windows

---

### SigningPublicKey

**Description:** 

**Platforms:** iOS, Android

---

### FsVolumeReadInfo

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionRequest

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuditGroupModified

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryIncomingDceRpcRequest

**Description:** Indicates that the Domain Controller must handle one or more incoming DCE/RPC requests from an account on an endpoint.

**Platforms:** Windows

---

### DcRemovableStorageDeviceConnected

**Description:** 

**Platforms:** Windows, macOS

---

### DcRemovableStorageDeviceDisconnected

**Description:** 

**Platforms:** Windows, macOS

---

### ScriptControlDotNetMetadata

**Description:** Contains the last 56kb of ScriptContent from a .NET AMSI scan.

**Platforms:** Windows

---

### GroupAccount

**Description:** Describes an observed group account. Fields: Forensics

**Platforms:** Forensics

---

### PrefetchFile

**Description:** Prefetch or Layout file records 8 most recent execution times of a Windows application. Fields: Forensics

**Platforms:** Forensics

---

### BrowserHistoryVisit

**Description:** Browser history hit information. Fields: Forensics

**Platforms:** Forensics

---

### EventTapInfo

**Description:** Describes a macOS Event Tap. Event Taps allow for capturing of keyboard and mouse HID events. Fields: Forensics

**Platforms:** Forensics

---

### LoginItemAdded

**Description:** 

**Platforms:** macOS

---

### IdpPolicyCloudAccessRuleMatch

**Description:** Fields: Public Cloud

**Platforms:** Public Cloud

---

### SuspiciousUserRemoteAPCAttempt

**Description:** An event that indicates that a remote APC (Asynchronous Procedure Call) that is classified as potentially suspicious was queued on the target process by the context process.

**Platforms:** Windows

---

### SuperfetchAppInfo

**Description:** Application entry from Windows Superfetch AgForegroundAppHistory.db. Fields: Forensics

**Platforms:** Forensics

---

### ForensicsCollectorLog

**Description:** A log entry emitted by the Falcon Forensics Collector process. Fields: Forensics

**Platforms:** Forensics

---

### RuntimeEnvironmentVariable

**Description:** Environment Variable provided to a process; In the context of falcon forensics, this is an environment variable provided to the collector process itself. Fields: Forensics

**Platforms:** Forensics

---

### MftBootSector

**Description:** Windows Master File Table (MFT) Boot sector. Fields: Forensics

**Platforms:** Forensics

---

### UserAssistAppLaunchInfo

**Description:** Application launched via user-assisted GUI menu. Fields: Forensics

**Platforms:** Forensics

---

### IdpWatchdogRemediationActionTakenForCpu

**Description:** 

**Platforms:** Windows

---

### GetAsyncKeyStateEtwBatch

**Description:** An event that indicates that an application called the GetAsyncKeyState API multiple times.

**Platforms:** Windows

---

### NamedPipe

**Description:** Named pipe information. Fields: Forensics

**Platforms:** Forensics

---

### ProcessHandleTableEntry

**Description:** An entry in a process handle table referencing a kernel object. Fields: Forensics

**Platforms:** Forensics

---

### DataEgress

**Description:** Description of a data egress observed on the sensor.

**Platforms:** Windows, macOS

---

### WSLDistributionStarted

**Description:** The Linux distribution starts.

**Platforms:** Windows

---

### FileSignatureStatistics

**Description:** On-demand scan for files with name extensions and header magic values. Fields: Forensics

**Platforms:** Forensics

---

### WSLDistributionRegistered

**Description:** A user registers a Linux distribution but hasn’t started it yet.

**Platforms:** Windows

---

### SuperfetchAppSchedule

**Description:** Application running schedule/period recently updated from Windows Superfetch AgGlobalHistory.db. Fields: Forensics

**Platforms:** Forensics

---

### WSLVMStarted

**Description:** The Linux Virtual Machine Root Namespace starts.

**Platforms:** Windows

---

### LocalGroupIdentity

**Description:** Group identity information includes user group name, GID, and names, UIDs and sid of user members. Fields: Forensics

**Platforms:** Forensics

---

### BrowserExtensionInfo

**Description:** Browser extension/addon information. Fields: Forensics

**Platforms:** Forensics

---

### DcBluetoothAuthorizationStatus

**Description:** 

**Platforms:** macOS

---

### UserGroupDeleted

**Description:** 

**Platforms:** Linux

---

### GcpAsset

**Description:** An event that contains GCP (Google Cloud Platform) Organization Metadata. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeFirewall

**Description:** An event that contains GCP (Google Cloud Platform) Compute Image configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureVirtualMachineState

**Description:** An event that contains the machine state for any Azure virtual machine. Fields: Public Cloud

**Platforms:** Public Cloud, Public Cloud

---

### GcpComputeNetworkPeering

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network Peering configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeInstance

**Description:** An event that contains GCP (Google Cloud Platform) Compute Instance configuration information. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeNetwork

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network configuration information. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeDisk

**Description:** An event that contains GCP (Google Cloud Platform) Compute Disk Configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeSubnetwork

**Description:** An event that contains GCP (Google Cloud Platform) Compute Subnetwork configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureIpConfiguration

**Description:** An event that contains a list of Azure IP configurations and attributes of the Azure IP configurations. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureVirtualNetwork

**Description:** An event that contains a list of the Azure virtual networks and the Azure virtual network attributes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpIamServiceAccount

**Description:** An event that contains GCP (Google Cloud Platform) IAM Service Account configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureSubscription

**Description:** An event that contains a list of Azure subscriptions. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureNetworkInterface

**Description:** An event that contains a list of Azure network interfaces and the Azure network interface attributes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### GcpComputeImage

**Description:** An event that contains GCP (Google Cloud Platform) Compute Image configuration details. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureResourceGroup

**Description:** An event that contains a list of Azure Resource Groups. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureDisk

**Description:** An event that contains a list of Azure disks and their attributes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureVirtualMachine

**Description:** An event that contains a list of Azure virtual machines and the Azure virtual machine attributes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureSubnet

**Description:** An event that contains Azure sub-networks in the virtual network. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzurePublicIpAddress

**Description:** An event that contains Azure public IP addresses. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureNetworkSecurityGroup

**Description:** An event that contains information about an Azure Network Security Group. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureVirtualNetworkPeering

**Description:** An event that contains a list of the Azure virtual networks and the Azure virtual network attributes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzurePrivateEndpoint

**Description:** An event that connects Azure Network interface to other services with private links. Fields: Public Cloud

**Platforms:** Public Cloud

---

### EksNodeGroup

**Description:** Snapshot of an AWS EKS node group. Fields: Public Cloud

**Platforms:** Public Cloud

---

### EksCluster

**Description:** Snapshot of an AWS EKS cluster. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SDeployment

**Description:** Snapshot of a deployment object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SReplicaSet

**Description:** Snapshot of a Replica Set object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SDaemonSet

**Description:** Snapshot of a Daemon Set object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### EksFargateProfile

**Description:** Snapshot of an AWS EKS Fargate profile. Fields: Public Cloud

**Platforms:** Public Cloud

---

### IdpWatchdogConfigurationsGetResponse

**Description:** 

**Platforms:** Windows

---

### FileContentsChanged

**Description:** 

**Platforms:** Linux

---

### SruApplicationTimelineProvider

**Description:** System Resource Utilization Monitor: application resource usage timeline. Fields: Forensics

**Platforms:** Forensics

---

### ShellBagFileTimeStampMetadata

**Description:** One event is emitted per timestamp from a ShellBag registry entry. Fields: Forensics

**Platforms:** Forensics

---

### SyscacheEntry

**Description:** An entry in windows syscache hive. Fields: Forensics

**Platforms:** Forensics

---

### BITSJobMetadata

**Description:** Background Intelligent Transfer Service (BITS) job metadata: times, proxy. Fields: Forensics

**Platforms:** Forensics

---

### RegCrowdstrikeValueUpdate

**Description:** 

**Platforms:** Windows

---

### BrowserDownloadStarted

**Description:** Browser downloaded file information signifying download start time. Fields: Forensics

**Platforms:** Forensics

---

### BrowserDownloadEnded

**Description:** Browser downloaded file information signifying download end time. Fields: Forensics

**Platforms:** Forensics

---

### OdsScanComplete

**Description:** On-demand scan for files with name extensions and header magic values. Fields: Forensics

**Platforms:** Forensics

---

### AutoRunProcessInfo

**Description:** Describes a process that is automatically executed. Fields: Forensics

**Platforms:** Forensics

---

### PeSectionInfo

**Description:** Windows Portable Executable (PE) section information. Fields: Forensics

**Platforms:** Forensics

---

### ShellBagInfo

**Description:** Windows ShellBag MRU registry entry. Fields: Forensics

**Platforms:** Forensics

---

### PeHeaderOptionalInfo

**Description:** Portable Executable optional header information from a Windows executable. Fields: Forensics

**Platforms:** Forensics

---

### RemoteThreadCreate

**Description:** 

**Platforms:** macOS

---

### ActiveDirectoryAuditGroupMemberModified

**Description:** 

**Platforms:** Windows

---

### RouteIP4

**Description:** IPv4 Route entry. Fields: Forensics

**Platforms:** Forensics

---

### PeFileWrittenDetectInfo

**Description:** 

**Platforms:** Windows

---

### MachOHeaderParsed

**Description:** A MachO file was read into memory from disk and its header was parsed.

**Platforms:** macOS

---

### MemoryLocked

**Description:** 

**Platforms:** Linux

---

### VulnerableDriverDetectInfo

**Description:** 

**Platforms:** Windows

---

### DeliverRulesEngineResultsToCloud

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### AtJobInfo

**Description:** Windows At jobs in use. Fields: Forensics

**Platforms:** Forensics

---

### HttpResponse

**Description:** 

**Platforms:** Linux, macOS

---

### PcaAppLaunchEntry

**Description:** An application launch entry in windows Program Compatibility Assistant (PCA) file PcaAppLaunchDic.txt. Fields: Forensics

**Platforms:** Forensics

---

### SyntheticPR2Stats

**Description:** 

**Platforms:** macOS

---

### PcaGeneralDbEntry

**Description:** An application launch entry in windows Program Compatibility Assistant (PCA) database PcaGeneralDb[0-9]+.txt. Fields: Forensics

**Platforms:** Forensics

---

### SyntheticVirtualMemoryArea

**Description:** 

**Platforms:** Linux

---

### VirtualMemoryArea

**Description:** 

**Platforms:** Linux

---

### FileOfInterestBasicInfo

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### FalconProcessHandleOpDetectInfo

**Description:** 

**Platforms:** Windows

---

### ScriptFileContentsDetectInfo

**Description:** 

**Platforms:** Windows

---

### DnsRequest

**Description:** When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. On Win/Lin sensor the data is deduplicated based on DomainName, IP4, IP6 and CNAME. Meaning if multiple requests are made that have responses containing different IP addresses for a single domain, they will all be visible. The sensor clears deduplication entries every 24 hrs after the first DnsRequest for the specific process is received. When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. On Mac the data is deduplicated just on DomainName. The sensor clears deduplication entries every 24 hrs after the first DnsRequest for the specific process is received. When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses.

**Platforms:** Windows, Linux, Android, macOS, iOS

---

### ArchiveMemberInfo

**Description:** Archive member file information. Fields: Forensics

**Platforms:** Forensics

---

### FileSystemContainmentStatus

**Description:** 

**Platforms:** Windows

---

### SystemExtension

**Description:** Describes a macOS system extension identified by the collector. Fields: Forensics

**Platforms:** Forensics

---

### SharedObjectLoaded

**Description:** 

**Platforms:** Linux, Linux, Falcon Container, Windows, macOS

---

### SignInfo

**Description:** Sent by FalconForensicsCollector containing information about the signing-state of an image.

**Platforms:** macOS, Windows, Forensics

---

### MalPaths

**Description:** Malicious DLL or executable image name conflicts found in different or unexpected folders. Fields: Forensics

**Platforms:** Forensics

---

### AppleScriptFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### LzfseFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### FileTimestampMetadata

**Description:** FileTime event is emitted per timestamp for a given file. This helps analysts build a timeline of file creation, access, and modification. Fields: Forensics

**Platforms:** Forensics

---

### BITSJobFileInfo

**Description:** Background Intelligent Transfer Service (BITS) job file information. Fields: Forensics

**Platforms:** Forensics

---

### LinkFileInfo

**Description:** Link file information. Fields: Forensics

**Platforms:** Forensics

---

### LogEntry

**Description:** A log entry observed on an endpoint. Fields: Forensics

**Platforms:** Forensics

---

### FileEntry

**Description:** Some portion of a text file, either a single line or matched regular expression. Fields: Forensics

**Platforms:** Forensics

---

### PtyAttached

**Description:** 

**Platforms:** Linux

---

### PeHeaderInfo

**Description:** Portable Executable header information from a Windows executable. Fields: Forensics

**Platforms:** Forensics

---

### EntropyScan

**Description:** File contents entropy, useful for identifying potentially malicious files. Fields: Forensics

**Platforms:** Forensics

---

### LSQuarantineEvent

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### PemFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### RecentExecutionTimestamp

**Description:** Recent execution timestamp from a Forensics artifact. Fields: Forensics

**Platforms:** Forensics

---

### ArchiveInfo

**Description:** Archive file information. Fields: Forensics

**Platforms:** Forensics, Forensics

---

### FileWrittenWithEntropyHigh

**Description:** 

**Platforms:** Windows, Linux

---

### MftRecord

**Description:** Windows Master File Table (MFT) record. Fields: Forensics

**Platforms:** Forensics

---

### XzFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### SyntheticSharedObjectLoaded

**Description:** 

**Platforms:** Linux

---

### AmcacheEntry

**Description:** Metadata related to PE execution and program installation on Windows 7 and Server 2008 R2 and above. Fields: Forensics

**Platforms:** Forensics

---

### MemoryAdvise

**Description:** 

**Platforms:** Linux

---

### WebShellDetected

**Description:** To identify webshell script files in a target folder, the content of each text file is matched against a large built-in list of regular expressions. Fields: Forensics

**Platforms:** Forensics

---

### UserEatAccessMonitoring

**Description:** 

**Platforms:** Windows

---

### ClassifiedProcessStart

**Description:** 

**Platforms:** Windows

---

### PromiscuousBindIP4

**Description:** This is a reified NetworkBindIP4 indicating a socket is in promiscuous mode.

**Platforms:** Windows, Windows, Linux, macOS

---

### DcUsbDevicePolicyViolation

**Description:** An event that indicates a USB device that matched a rule in a policy but was not blocked due to the rule being set to reporting mode only.

**Platforms:** macOS, Windows, Linux

---

### DcBluetoothDeviceBlocked

**Description:** 

**Platforms:** macOS

---

### DcBluetoothDevicePolicyViolation

**Description:** 

**Platforms:** macOS

---

### SruApplicationResourceUsage

**Description:** System Resource Utilization Monitor: application resource usage per user. Fields: Forensics

**Platforms:** Forensics

---

### NtfsLinkCreatedDetectInfo

**Description:** 

**Platforms:** Windows

---

### IPCDetectInfo

**Description:** 

**Platforms:** Windows

---

### MacKnowledgeActivityStart

**Description:** An entry from a knowledgeC database indicating the start of some user activity on a MacOs system. Fields: Forensics

**Platforms:** Forensics

---

### MemoryProtectionChanged

**Description:** 

**Platforms:** Linux

---

### ScheduledTaskTemplateDetectInfo

**Description:** 

**Platforms:** Windows

---

### DcRemovableStorageDeviceBlocked

**Description:** 

**Platforms:** Windows, macOS

---

### DcRemovableStorageDevicePolicyViolation

**Description:** 

**Platforms:** Windows, macOS

---

### ResourceLimit

**Description:** 

**Platforms:** Linux

---

### RegFeatureUsageInfo

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### HttpRequestV2Detect

**Description:** 

**Platforms:** Windows, Windows

---

### HostedServiceStatusInfo

**Description:** Status information includes loaded DLL for a hosted service. Fields: Forensics

**Platforms:** Forensics

---

### RegCrowdstrikeKeyUpdate

**Description:** 

**Platforms:** Windows

---

### K8SInitContainerStatus

**Description:** Snapshot of an Initialization(Init) Container belonging to a Pod Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureNatFirewallRule

**Description:** An event that contains Azure firewall rules for LAN. Fields: Public Cloud

**Platforms:** Public Cloud

---

### ActiveDirectoryIncomingLdapSearchRequest

**Description:** Indicates that the Domain Controller must handle one or more LDAP search requests from an account on an endpoint.

**Platforms:** Windows

---

### AksCluster

**Description:** Snapshot of an Azure AKS cluster. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AksAgentPool

**Description:** Snapshot of an Azure AKS Agent Pool. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SPod

**Description:** Snapshot of a Pod object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SService

**Description:** Snapshot of a Service object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SNode

**Description:** Snapshot of a Node object in Kubernetes. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SRunningContainer

**Description:** Snapshot of a running Container belonging to a Pod. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureFirewall

**Description:** An event that contains information about Azure cloud-based network security service. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureFirewallRuleCollection

**Description:** An event that contains Azure firewall rule collections for application, NAT (network address translation) and network firewall rules. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureNetworkSecurityGroupRule

**Description:** An event that contains Azure security rules in the specified network security group. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SEphemeralContainer

**Description:** Snapshot of an ephemeral Container belonging to a Pod. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SRunningContainerStatus

**Description:** Snapshot of status for a running Container inside a Pod. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AksVMSS

**Description:** Snapshot of an Azure Virtual Machine Scale Sets. Fields: Public Cloud

**Platforms:** Public Cloud

---

### K8SInitContainer

**Description:** Snapshot of status for an Initialization(Init) Container inside a Pod. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AzureApplicationFirewallRule

**Description:** An event that contains firewall rules for https traffic or Azure SQL traffic. Fields: Public Cloud

**Platforms:** Public Cloud

---

### BamRegAppRunTime

**Description:** Recent program execution timeline from Background Activity Moderator (BAM) system service registry. BAM key is written on system shutdown. Fields: Forensics

**Platforms:** Forensics

---

### ScriptControlDetectInvalidInfo

**Description:** 

**Platforms:** Linux, Falcon Container

---

### UserAccount

**Description:** Describes an observed user account. Fields: Forensics

**Platforms:** Forensics

---

### JumpListInfo

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### RegShimCache

**Description:** Shim cache registry entry. Fields: Forensics

**Platforms:** Forensics

---

### ActiveDirectoryAuditUserModified

**Description:** 

**Platforms:** Windows

---

### KernelExtension

**Description:** Describes a macOS kernel extension identified by the collector. Fields: Forensics

**Platforms:** Forensics

---

### AzureNetworkFirewallRule

**Description:** An event that contains Azure network filtering rules. Fields: Public Cloud

**Platforms:** Public Cloud

---

### ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate

**Description:** 

**Platforms:** Windows

---

### ConfigStateUpdate

**Description:** Sent periodically and when dynamic config is updated. Analysts can find out which config was active using this event with ConfigStateHash. You may have to reason about what a particular hash really means for a particular event at a given point in time, particularly if the hash has recently changed.

**Platforms:** Windows, macOS, Linux, Falcon Container, iOS, Android, Kubernetes, Windows Legacy, Vmcluster

---

### LFODownloadConfirmation

**Description:** Thrown when the agent receives an LFODownload event.

**Platforms:** Windows, macOS, Linux, Falcon Container, Android, iOS, Kubernetes, Vmcluster

---

### ASLRBypassAttempt

**Description:** Emitted when a process that applied ForceASLR to a module detects an invalid execution attempt. This should only happen during an exploit, when the initial ROP chain is designed to defeat ASLR. In the case of a typical ALSR bypass attempt (trying to utilize code in a rebased image as part of a ROP chain), TargetAddress and ExceptionAddress will likely be identical, as will ImageFileName and SourceFileName.

**Platforms:** Windows

---

### HeapSprayAttempt

**Description:** Emitted when a process that had HeapSpray protections applied detects an invalid execution attempt.

**Platforms:** Windows

---

### SEHOverWriteAttempt

**Description:** An event that is emitted when a UserException event has failed a SEH (Structured Exception Handler) validation. The nature of the failure is described by the bitmask SEHValidationFailureFlags. Depending on the type of failure, ExceptionHandlerAddress field or ExceptionFrameAddress field may not be present.

**Platforms:** Windows

---

### SsoUserLogon

**Description:** Indicates an initial, successful sign-in to an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS. Fields: Public Cloud

**Platforms:** Public Cloud

---

### SsoUserLogonFailure

**Description:** Indicates an initial, failed sign-in to an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS. Fields: Public Cloud

**Platforms:** Public Cloud

---

### SsoApplicationAccess

**Description:** Indicates successful access to an application through an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS. Fields: Public Cloud

**Platforms:** Public Cloud

---

### AdditionalHostInfo

**Description:** Serves as an addition to kernel-driven HostInfo event. Provides host-specific machine information from user mode. ObjectGuid is optional because a given host may not be joined to a domain.

**Platforms:** Windows, macOS

---

### AndroidModuleStateUpdate

**Description:** Status information of modules for the Android sensor. AndroidModuleId lists available modules. Fields: Android

**Platforms:** Android

---

### SsoApplicationAccessFailure

**Description:** Indicates failed access to an application through an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS. Fields: Public Cloud

**Platforms:** Public Cloud

---

### UserAccessLogEntry

**Description:** Per-user access log information for the year for a service role and IP address pair on Windows servers. Fields: Forensics

**Platforms:** Forensics

---

### FileSignatureMismatch

**Description:** On-demand scan for files with name extensions and header magic values. Fields: Forensics

**Platforms:** Forensics

---

### RemoteProcessMemoryWrite

**Description:** 

**Platforms:** Linux

---

### FileHashesEvent

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### WindowsTimelineEntry

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### OpenDirectoryGroupRemove

**Description:** 

**Platforms:** macOS

---

### RegGenericInfo

**Description:** Registry entry generic information. Fields: Forensics

**Platforms:** Forensics

---

### MacKnowledgeActivityEnd

**Description:** An entry from a knowledgeC database indicating the end of some user activity on a MacOs system. Fields: Forensics

**Platforms:** Forensics, Windows

---

### MacMRU

**Description:** A digital forensics record derived from Apple SharedFileList (.sfl/.sfl2) files. This event helps identify most recently used resources (applications, documents, volumes, etc.). Fields: Forensics

**Platforms:** Forensics

---

### WlanInterfaceInfo

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### ShimDbTag

**Description:** A tag entry in the Shim database. Fields: Forensics

**Platforms:** Forensics, Forensics

---

### SruNetworkConnectivityUsage

**Description:** System Resource Utilization Monitor: connection time per local network interface, application and user tuple. Fields: Forensics

**Platforms:** Forensics

---

### FileExtendedAttrOperation

**Description:** 

**Platforms:** macOS

---

### USNRecord

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### PeCodePageInfo

**Description:** A code page that is used to decode code point values within a windows Portable Executable resource. Fields: Forensics

**Platforms:** Forensics

---

### RemoteProcessMemoryRead

**Description:** 

**Platforms:** Linux

---

### XProtectAction

**Description:** 

**Platforms:** macOS

---

### AspmCollectionStatusUpdate

**Description:** 

**Platforms:** Linux, Windows

---

### ProcessOpenedFileDescriptor

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### EddScanStart

**Description:** Sent by sensor to indicate the start of a new EDD scan run. Note: This event is currently not supported in macOS. Sent by sensor to indicate the start of a new EDD scan run.

**Platforms:** macOS, Windows

---

### CreateThreadNoStartImage

**Description:** This event is used to indicate the target start address of a CreateThread attempt is not within the limits of a loaded module. This could indicate the presence of shellcode, or other dynamically allocated code regions.

**Platforms:** Windows

---

### CreateThreadReflectiveDll

**Description:** This event is used to indicate the presence of a reflectively loaded dll in the callstack for a CreateThread attempt.

**Platforms:** Windows

---

### UmppcEntryAnomaly

**Description:** 

**Platforms:** Windows

---

### ScriptControlBlocked

**Description:** This event is sent when Falcon Host has blocked malicious script content from being executed on the machine. This event provides the details of exactly what content was blocked.

**Platforms:** Windows

---

### ProcessHandleOpDetectInfo

**Description:** An event that describes the operation on a Process handle that triggered a detection.

**Platforms:** Windows

---

### ReflectiveDllOpenProcess

**Description:** A userspace thread attempted to open a process which appeared to originate from a reflectively loaded DLL.

**Platforms:** Windows

---

### ScriptControlScanTelemetry

**Description:** 

**Platforms:** Windows

---

### IdpPolicyAccessRuleMatch

**Description:** 

**Platforms:** Windows

---

### CreateThreadKernelNoStartImage

**Description:** Emitted when a new system thread is created outside of a loaded driver.

**Platforms:** Windows

---

### IdpWatchdogReEnabled

**Description:** 

**Platforms:** Windows

---

### SensorSelfDiagnosticAlert

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### ExtendedExploitMitigationViolatedDetectInfo

**Description:** 

**Platforms:** Windows

---

### ProcessState

**Description:** Running process observed at collection time. Fields: Forensics

**Platforms:** Forensics

---

### FfcBytePatternScanResult

**Description:** Describes a scanning result performed by the Falcon Forensics Collector. Fields: Forensics

**Platforms:** Forensics

---

### CSAResultsGenericDetectInfo

**Description:** 

**Platforms:** Windows

---

### DataProtectionBrowserConnect

**Description:** 

**Platforms:** Windows, macOS

---

### ProcessSubstituteUser

**Description:** 

**Platforms:** macOS

---

### DcUsbDeviceConnected

**Description:** An event that describes a connected USB device to which Device Control is attached. It is sent each time the system powers on, the associated hub/port is power cycled, or the device is physically inserted into the system.

**Platforms:** Linux, Windows, macOS

---

### GcpComputeNetworkInterface

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network Interface configuration information. Fields: Public Cloud

**Platforms:** Public Cloud

---

### SuspectCreateThreadStack

**Description:** This event is used to indicate that suspicious data has been discovered in the context of a CreateThread attempt.

**Platforms:** Windows

---

### ErrorEvent

**Description:** Event indicating a sensor error.

**Platforms:** Linux, Falcon Container, Windows, macOS, Vmcluster, Kubernetes

---

### ResourceUtilization

**Description:** An event that contains CPU and RAM utilization data for a system. The event is sent when the sensor connects and every 15 minutes thereafter. An event that contains CPU and RAM utilization data for a system. The event is sent when the sensor connects, every 15 minutes thereafter, and in case any change in capacity is detected.

**Platforms:** Linux, Falcon Container, macOS, Kubernetes, Windows

---

### RecentlyModifiedFileExecutedInContainer

**Description:** 

**Platforms:** Linux, Falcon Container

---

### DetectionExcluded

**Description:** This event indicates that a detection has been excluded, either by customer exclusions or by CrowdStrike. Fields: Android, iOS

**Platforms:** Android, iOS, macOS, Linux, Falcon Container, Windows

---

### ZstdFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### LhaFileWritten

**Description:** 

**Platforms:** Windows

---

### BcmFileWritten

**Description:** 

**Platforms:** Windows

---

### FreeArcFileWritten

**Description:** 

**Platforms:** Windows

---

### Base64PeFileWritten

**Description:** 

**Platforms:** Windows

---

### LRZipFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### BlakHoleFileWritten

**Description:** 

**Platforms:** Windows

---

### ZpaqFileWritten

**Description:** 

**Platforms:** Windows

---

### BrotliFileWritten

**Description:** 

**Platforms:** Windows

---

### PeaFileWritten

**Description:** 

**Platforms:** Windows

---

### Yz1FileWritten

**Description:** 

**Platforms:** Windows

---

### NetworkSummary

**Description:** 

**Platforms:** Windows

---

### LZipFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### ProcessEnvironmentEmpty

**Description:** 

**Platforms:** Linux

---

### NetworkStatisticsIP6

**Description:** Fields: Forensics

**Platforms:** Forensics, macOS

---

### LzmaFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### SyntheticProcessTrace

**Description:** 

**Platforms:** Linux

---

### ShellCommandLineInfo

**Description:** 

**Platforms:** Linux

---

### NetworkStatisticsUDP6

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### LZOFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### NetworkStatisticsTCP4

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### NetworkStatisticsUDP4

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### NetworkStatisticsIP4

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### PromiscuousBindIP6

**Description:** 

**Platforms:** Windows

---

### LZ4FileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### MpThreatWMI

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### NetworkStatisticsTCP6

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### NetworkIcmpDataIP4

**Description:** 

**Platforms:** Linux

---

### SensorMetadataUpdate

**Description:** 

**Platforms:** Linux

---

### UserExceptionDEP

**Description:** This event is emitted when a userspace process is detected as having has a DEP or NX-related exception.

**Platforms:** Windows

---

### MpThreatAction

**Description:** Report when a particular threat action type has occurred. Fields: Forensics

**Platforms:** Forensics

---

### ClassifiedSensitiveFileAccess

**Description:** 

**Platforms:** Windows

---

### PhpEvalString

**Description:** 

**Platforms:** Linux

---

### PhpExecuteScript

**Description:** 

**Platforms:** Linux

---

### PhpBase64Decode

**Description:** 

**Platforms:** Linux

---

### FileDescriptorMonitor

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### WSLMetadata

**Description:** 

**Platforms:** Linux

---

### BITSJobInfo

**Description:** Background Intelligent Transfer Service (BITS) job information. Fields: Forensics

**Platforms:** Forensics

---

### MpThreat

**Description:** Microsoft protection threat. Fields: Forensics

**Platforms:** Forensics

---

### MpThreatDetection

**Description:** Microsoft protection threat detection. Fields: Forensics

**Platforms:** Forensics

---

### NetworkIcmpDataIP6

**Description:** 

**Platforms:** Linux

---

### MpThreatDetectionWMI

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### DataProtectionPACDiagnostic

**Description:** 

**Platforms:** Windows

---

### InstallServiceDownloadComplete

**Description:** An install service download has completed.

**Platforms:** Windows

---

### QuarantineActionResult

**Description:** This event reports the result of a file quarantine triggered by Falcon Prevent.

**Platforms:** Windows, macOS, Linux, Kubernetes, Vmcluster

---

### UpdateManifestDownloadComplete

**Description:** An update manifest download has completed.

**Platforms:** Windows

---

### NetworkUncontainmentCompleted

**Description:** This event is sent by the sensor after processing a NetworkUncontainmentRequest event from the cloud. The Status field indicates the success or failure of the uncontainment operation.

**Platforms:** Windows, macOS, Linux, Android, iOS

---

### QuarantinedFile

**Description:** This event is generated when a file is quarantined by Falcon Prevent.

**Platforms:** Windows, macOS, Linux, Kubernetes, Vmcluster

---

### InstallBundleDownloadComplete

**Description:** An install bundle download has completed.

**Platforms:** Windows

---

### NetworkContainmentCompleted

**Description:** This event is sent by the sensor after processing a NetworkContainmentRequest event from the cloud. The Status field indicates the success or failure of the containment operation.

**Platforms:** Windows, Linux, macOS, iOS, Android

---

### SAMHashDumpFromUnsignedModule

**Description:** This event contains information about an unsigned module that accessed protected SAM account registry keys. It combines relevant information from the RegNtPostOpenKeyEx and SignInfoWithCertAndContext events

**Platforms:** Windows

---

### QuarantinedFileState

**Description:** This event reports the state of a file quarantined by Falcon Prevent.

**Platforms:** Windows, macOS, Linux, Kubernetes, Vmcluster

---

### OsfmDownloadComplete

**Description:** Sent by LFODownloadActor when new OSFM data is downloaded.

**Platforms:** Windows

---

### InstalledUpdates

**Description:** An event that describes the updates installed on the system. The Status field will indicate if some error occurred when attempting to find installed updates. PendingUpdateIds will be an empty string if none are pending. The event is emitted once at startup, and then periodically after that.

**Platforms:** Windows

---

### UserFontLoad

**Description:** An event that is sent when a user mode program attempts to add a font.

**Platforms:** Windows

---

### NullPageUnmapAttempt

**Description:** An event that indicates that an attempt was made to unmap the NULL page.

**Platforms:** Windows

---

### UmppaErrorEvent

**Description:** 

**Platforms:** Windows

---

### NullPageProtectionModificationAttempt

**Description:** An event that indicates that an attempt was made to modify the protection of the NULL page.

**Platforms:** Windows

---

### RansomwareOpenFile

**Description:** A reified LocalFsPostCreate event so the cloud can route these events for ransomware support.

**Platforms:** Windows

---

### RegNtPostOpenKeyEx

**Description:** Registry post open key operation event.

**Platforms:** Windows

---

### FsPostCreate

**Description:** This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing data for these events will still appear, but new sensors utilize the FileCreateInfo event. This event is generated when a file is created by a process.

**Platforms:** Windows

---

### ManifestDownloadComplete

**Description:** Sent by LFODownloadActor when a new configuration manifest has been downloaded.

**Platforms:** Windows, macOS, Linux, Falcon Container, Kubernetes, Vmcluster

---

### ConfigDownloadComplete

**Description:** Sent by LFODownloadActor when a new binary configuration has been downloaded as part of a configuration update.

**Platforms:** Windows, macOS, Linux, Falcon Container, Kubernetes, Vmcluster

---

### FsPostOpen

**Description:** This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing data for these events will still appear, but new sensors utilize the FileOpenInfo event. This event is generated when a file is opened by a process. This event is only sent to the cloud for processes inside of a detection tree.

**Platforms:** Windows

---

### ModuleDownloadComplete

**Description:** Sent by LFODownloadActor when a new module has been downloaded as part of a configuration update.

**Platforms:** Windows, macOS, Linux

---

### ECBDownloadComplete

**Description:** Sent by LFODownloadActor when a new ECB module has been downloaded as part of a configuration update.

**Platforms:** Windows, macOS, Linux, Windows

---

### RegKeySecurityDecreasedFromUnsignedModule

**Description:** This event contains information about a protected registry security object whose security was decreased. It combines relevant information from the RegKeySecurityDecreased and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### ChannelDataDownloadComplete

**Description:** Sent by LFODownloadActor when a new channel data file has been downloaded.

**Platforms:** Windows, Android, Linux, Falcon Container, macOS, Kubernetes, iOS, Vmcluster

---

### FsPostOpenSnapshotFile

**Description:** Information about a file opened on a snapshot volume.

**Platforms:** Windows

---

### PrivilegedProcessHandle

**Description:** Indicates a process has opened a handle to a privileged process with special access rights.

**Platforms:** Windows

---

### FsPostOpenUpImpersonating

**Description:** A reified FsPostOpen event that occurred in the context of a thread up-impersonating another user, and the context process was not a privileged account.

**Platforms:** Windows

---

### RegNtPostOpenKeyExUpImpersonating

**Description:** A reified RegNtPostOpenKeyEx event that occurred in the context of a thread up-impersonating another user, and the context process was not a privileged account.

**Platforms:** Windows

---

### PrivilegedProcessHandleFromUnsignedModule

**Description:** This event contains information about a privileged process handle created from an unsigned module.

**Platforms:** Windows, Windows

---

### ConfigurationLoaded

**Description:** Thrown when a new configuration has been successfully loaded but before any Event Sources are started. Fields: Android, iOS

**Platforms:** Android, iOS

---

### OciImageInfo

**Description:** An event that contains information about this image used in a container.

**Platforms:** Linux, Falcon Container

---

### CsUmProcessCrashSummaryEvent

**Description:** A event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field.

**Platforms:** Windows

---

### FirewallRuleApplicationFailed

**Description:** An event that indicates that the application of a firewall rule has failed. An event that indicates that the application of a firewall rule has failed.

**Platforms:** Windows, macOS, Linux

---

### FalconServiceStatus

**Description:** A message from CsFalconService regarding the service and its servlets' lifecycle events.

**Platforms:** Windows, Windows

---

### RemediationActionServiceRemoval

**Description:** Notification of a service persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### CidMigrationError

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### CidMigrationManifestDownloadComplete

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### AmsBytePatternScanTelemetry

**Description:** 

**Platforms:** Windows

---

### AmsBytePatternScanResult

**Description:** 

**Platforms:** Windows

---

### RecoveryActionDeleteFilesComplete

**Description:** 

**Platforms:** Windows, Linux, Falcon Container, Kubernetes, macOS

---

### RecoveryActionRegistryDeleteValueKeyComplete

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistryDeleteKeyComplete

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistryDeleteKeyReply

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistryCreateKeyComplete

**Description:** 

**Platforms:** Windows

---

### RecoveryActionManipulateModuleTableComplete

**Description:** 

**Platforms:** Linux, Falcon Container, macOS, Windows

---

### RecoveryActionKillProcessesComplete

**Description:** 

**Platforms:** Linux, Falcon Container, Kubernetes, Windows, macOS

---

### RecoveryActionKillProcessesReply

**Description:** Fields: Kubernetes, Windows, macOS, Linux, Falcon Container

**Platforms:** Kubernetes, Windows, macOS, Linux, Falcon Container

---

### PackageManagerDownloadComplete

**Description:** Fields: Vmcluster, macOS, Linux, Falcon Container, Windows, Kubernetes

**Platforms:** Vmcluster, macOS, Linux, Falcon Container, Windows, Kubernetes

---

### OciContainerPlumbingSummary

**Description:** 

**Platforms:** Linux

---

### EddScanStatus

**Description:** Sent by sensor periodically to report the status of an on-going scan. Note: This event is currently not supported in macOS. Sent by sensor periodically to report the status of an on-going scan.

**Platforms:** macOS, Windows

---

### LFODownloadComplete

**Description:** 

**Platforms:** macOS, Kubernetes, Vmcluster, Android, iOS, Windows, Linux, Falcon Container

---

### IdpCloudHealthConfigurationsSetResponse

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogConfigurationsSetResponse

**Description:** 

**Platforms:** Windows

---

### RemediationMonitorKillProcess

**Description:** Notification of a kill process remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Linux, macOS, Windows

---

### RemediationActionQuarantineMacroFile

**Description:** 

**Platforms:** Windows

---

### KernelCallbackTablePatch

**Description:** An event that indicates that the KernelCallbackTable has been altered at the specified index. If present, CallstackModuleNames, Buffer, and MiniContext apply to the thread that modified the index, with Buffer being the bytes at the faulting address. MiniContext, if set, contains Edi, Esi, Ebx, Edx, Ecx, Eax, Ebp for 32-bit processes and Rax, Rcx, Rdx, Rbx, Rbp, Rsi, Rdi, R8-R15 on 64-bit.

**Platforms:** Windows

---

### EarlyExploitPivotDetect

**Description:** Telemetry event indicating execution pivoting in an unusual way. Could be indicative of malicious code.

**Platforms:** Windows

---

### SuspiciousUserFontLoad

**Description:** Sent when a UserFontLoad event has been blocked by the sensor.

**Platforms:** Windows

---

### CommsLogReset

**Description:** Sent by Communications indicating that the CommsLog was flushed due to invalid data

**Platforms:** macOS

---

### RecoveryActionRegistrySetValueKeyReply

**Description:** 

**Platforms:** Windows

---

### RecoveryActionSetRuntimeSystemTagsComplete

**Description:** 

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### RecoveryActionSetSystemTagsComplete

**Description:** Fields: Kubernetes, Windows, macOS, Linux, Falcon Container

**Platforms:** Kubernetes, Windows, macOS, Linux, Falcon Container

---

### RecoveryActionGetSystemTagsComplete

**Description:** Fields: Kubernetes, macOS, Linux, Falcon Container, Windows

**Platforms:** Kubernetes, macOS, Linux, Falcon Container, Windows

---

### OpenDirectoryPasswordModification

**Description:** 

**Platforms:** macOS

---

### RecoveryActionDeleteFilesReply

**Description:** Fields: Kubernetes, Windows, macOS, Linux, Falcon Container

**Platforms:** Kubernetes, Windows, macOS, Linux, Falcon Container

---

### RecoveryActionGetModuleTableRecordComplete

**Description:** 

**Platforms:** macOS, Windows, Linux, Falcon Container

---

### OciContainerInfo

**Description:** An event that contains information about this container on creation of the container.

**Platforms:** Linux, Falcon Container

---

### HttpVisibilityStatus

**Description:** An event that indicates that the status of the HTTP Visibility event source has been updated.

**Platforms:** Windows

---

### SSHClientAuthenticated

**Description:** 

**Platforms:** Linux

---

### RecoveryActionGetRuntimeSystemTagsComplete

**Description:** 

**Platforms:** Windows, macOS, Linux, Falcon Container, Windows

---

### DriverPreventFailed

**Description:** Event which indicates we failed (or timed out) attempting to block a driver load.

**Platforms:** Windows

---

### RemediationActionKillProcess

**Description:** Notification of a kill process remediation action attempted by the sensor.

**Platforms:** Windows, Linux, macOS, Windows Legacy

---

### RemediationActionQuarantineFile

**Description:** Notification of a quarantine file remediation action attempted by the sensor.

**Platforms:** Windows

---

### RemediationMonitorQuarantineFile

**Description:** Notification of a quarantine file remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### CreateProcessArgs

**Description:** Full command line argument corresponding to a process creation.

**Platforms:** macOS

---

### CloudScanControl

**Description:** A event to that notifies downstream services of completed tasks. Fields: Public Cloud

**Platforms:** Public Cloud, Windows

---

### RemediationActionRegistryRemoval

**Description:** Notification of a registry persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### BlockThreadFailed

**Description:** A block thread request failed.

**Platforms:** Windows

---

### KillProcessError

**Description:** If KillProcessActor fails to kill a process due to process being marked as system critical or for any other reason, this event is emitted.

**Platforms:** Linux, Falcon Container, macOS, Windows

---

### MacFsEventRecord

**Description:** Mac fsevents record, forensically interesting filesystem logging/information. Fields: Forensics

**Platforms:** Forensics

---

### ExcelDocumentOpened

**Description:** 

**Platforms:** Windows

---

### QuarantineXattribute

**Description:** Fields: Forensics

**Platforms:** Forensics

---

### AppProtocolDetected

**Description:** 

**Platforms:** macOS

---

### RemediationActionQuarantineOfficeMacroFile

**Description:** 

**Platforms:** Windows, Windows

---

### OpenDirectoryCreateUser

**Description:** 

**Platforms:** macOS

---

### ZerologonExploitAttempt

**Description:** 

**Platforms:** Windows

---

### PeLanguageId

**Description:** A language on which a windows Portable Executable resource depends. Fields: Forensics

**Platforms:** Forensics

---

### MsiTransactionExecuted

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistryDeleteValueKeyReply

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistrySetValueKeyComplete

**Description:** 

**Platforms:** Windows

---

### EtwComponentResponse

**Description:** Event sent in when EtwComponent has initialized. AttemptNumber is no longer used.

**Platforms:** Windows

---

### SuspendProcessError

**Description:** This event is emitted if KillProcessActor fails to suspend a process.

**Platforms:** Linux, Falcon Container, Windows, macOS

---

### RemediationActionScheduledTaskRemoval

**Description:** Notification of a scheduled task persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### RecoveryActionRegistryCreateKeyReply

**Description:** 

**Platforms:** Windows, Android, iOS

---

