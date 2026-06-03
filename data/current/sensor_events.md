# CrowdStrike Falcon Sensor Events

**Total Events:** 998

---

## Table of Contents

- [AbnormalTerminationNotification](#abnormalterminationnotification)
- [AccessoryConnected](#accessoryconnected)
- [AccessoryDisconnected](#accessorydisconnected)
- [ActiveDirectoryAccountCreated](#activedirectoryaccountcreated)
- [ActiveDirectoryAccountDepartmentUpdate](#activedirectoryaccountdepartmentupdate)
- [ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate](#activedirectoryaccountdirectcontaininggroupentitiesupdate)
- [ActiveDirectoryAccountDisabled](#activedirectoryaccountdisabled)
- [ActiveDirectoryAccountEnabled](#activedirectoryaccountenabled)
- [ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate](#activedirectoryaccountflattenedcontaininggroupentitiesupdate)
- [ActiveDirectoryAccountLocked](#activedirectoryaccountlocked)
- [ActiveDirectoryAccountNameUpdate](#activedirectoryaccountnameupdate)
- [ActiveDirectoryAccountOuUpdate](#activedirectoryaccountouupdate)
- [ActiveDirectoryAccountPasswordUpdate](#activedirectoryaccountpasswordupdate)
- [ActiveDirectoryAccountUnlocked](#activedirectoryaccountunlocked)
- [ActiveDirectoryAuditGpoModified](#activedirectoryauditgpomodified)
- [ActiveDirectoryAuditGroupMemberModified](#activedirectoryauditgroupmembermodified)
- [ActiveDirectoryAuditGroupModified](#activedirectoryauditgroupmodified)
- [ActiveDirectoryAuditPasswordModificationAttempt](#activedirectoryauditpasswordmodificationattempt)
- [ActiveDirectoryAuditUserModified](#activedirectoryauditusermodified)
- [ActiveDirectoryAuthentication](#activedirectoryauthentication)
- [ActiveDirectoryAuthenticationFailure](#activedirectoryauthenticationfailure)
- [ActiveDirectoryIncomingDceRpcEpmRequest](#activedirectoryincomingdcerpcepmrequest)
- [ActiveDirectoryIncomingDceRpcRequest](#activedirectoryincomingdcerpcrequest)
- [ActiveDirectoryIncomingLdapSearchRequest](#activedirectoryincomingldapsearchrequest)
- [ActiveDirectoryIncomingPsExecExecution2](#activedirectoryincomingpsexecexecution2)
- [ActiveDirectoryInteractiveDomainLogon](#activedirectoryinteractivedomainlogon)
- [ActiveDirectoryServiceAccessRequest](#activedirectoryserviceaccessrequest)
- [ActiveDirectoryServiceAccessRequestFailure](#activedirectoryserviceaccessrequestfailure)
- [AcUninstallConfirmation](#acuninstallconfirmation)
- [AcUnloadConfirmation](#acunloadconfirmation)
- [AdditionalHostInfo](#additionalhostinfo)
- [ADExplorerFileWritten](#adexplorerfilewritten)
- [AgentConnect](#agentconnect)
- [AgenticSessionEnd](#agenticsessionend)
- [AgenticSessionStart](#agenticsessionstart)
- [AgenticSubagentStart](#agenticsubagentstart)
- [AgenticToolRequest](#agentictoolrequest)
- [AgenticUserPromptSubmit](#agenticuserpromptsubmit)
- [AgentOnline](#agentonline)
- [AiAgentClassifyChildTelemetry](#aiagentclassifychildtelemetry)
- [AiAgentClassifyRootTelemetry](#aiagentclassifyroottelemetry)
- [AksAgentPool](#aksagentpool)
- [AksCluster](#akscluster)
- [AksVMSS](#aksvmss)
- [AllocVmEtw](#allocvmetw)
- [AmcacheEntry](#amcacheentry)
- [AmsBytePatternScanResult](#amsbytepatternscanresult)
- [AmsBytePatternScanTelemetry](#amsbytepatternscantelemetry)
- [AmsiRegistrationStatus](#amsiregistrationstatus)
- [AndroidEnterpriseInfo](#androidenterpriseinfo)
- [AndroidInitServiceAdded](#androidinitserviceadded)
- [AndroidInitServiceRemoved](#androidinitserviceremoved)
- [AndroidIntentSentIPC](#androidintentsentipc)
- [AndroidManifestFragmentData](#androidmanifestfragmentdata)
- [AndroidManifestXmlUploaded](#androidmanifestxmluploaded)
- [AndroidModuleStateUpdate](#androidmodulestateupdate)
- [APKMetadata](#apkmetadata)
- [AppleScriptFileWritten](#applescriptfilewritten)
- [AppProtocolDetected](#appprotocoldetected)
- [AppSideLoaded](#appsideloaded)
- [AppUninstalled](#appuninstalled)
- [ArcFileWritten](#arcfilewritten)
- [ArchiveFileContent](#archivefilecontent)
- [ArchiveInfo](#archiveinfo)
- [ArchiveMemberInfo](#archivememberinfo)
- [ArjFileWritten](#arjfilewritten)
- [AsepFileChangeDetectInfo](#asepfilechangedetectinfo)
- [AsepFileChangeScanInfo](#asepfilechangescaninfo)
- [AsepKeyUpdate](#asepkeyupdate)
- [AsepValueUpdate](#asepvalueupdate)
- [AsifFileWritten](#asiffilewritten)
- [ASLRBypassAttempt](#aslrbypassattempt)
- [AspmCollectionStatusUpdate](#aspmcollectionstatusupdate)
- [AssociateIndicator](#associateindicator)
- [AssociateTreeIdWithRoot](#associatetreeidwithroot)
- [AtJobInfo](#atjobinfo)
- [AuditCveKmEtw](#auditcvekmetw)
- [AuditCveUmEtw](#auditcveumetw)
- [AutoRunProcessInfo](#autorunprocessinfo)
- [AwsEc2Image](#awsec2image)
- [AwsEc2Instance](#awsec2instance)
- [AwsEc2NetworkAcl](#awsec2networkacl)
- [AwsEc2NetworkAclEntry](#awsec2networkaclentry)
- [AwsEc2NetworkInterface](#awsec2networkinterface)
- [AwsEc2NetworkInterfacePrivateIP](#awsec2networkinterfaceprivateip)
- [AwsEc2SecurityGroup](#awsec2securitygroup)
- [AwsEc2SecurityGroupRule](#awsec2securitygrouprule)
- [AwsEc2Subnet](#awsec2subnet)
- [AwsEc2Volume](#awsec2volume)
- [AwsEc2Vpc](#awsec2vpc)
- [AwsIamAccountAlias](#awsiamaccountalias)
- [AzureApplicationFirewallRule](#azureapplicationfirewallrule)
- [AzureDisk](#azuredisk)
- [AzureFirewall](#azurefirewall)
- [AzureFirewallRuleCollection](#azurefirewallrulecollection)
- [AzureIpConfiguration](#azureipconfiguration)
- [AzureNatFirewallRule](#azurenatfirewallrule)
- [AzureNetworkFirewallRule](#azurenetworkfirewallrule)
- [AzureNetworkInterface](#azurenetworkinterface)
- [AzureNetworkSecurityGroup](#azurenetworksecuritygroup)
- [AzureNetworkSecurityGroupRule](#azurenetworksecuritygrouprule)
- [AzurePrivateEndpoint](#azureprivateendpoint)
- [AzurePublicIpAddress](#azurepublicipaddress)
- [AzureResourceGroup](#azureresourcegroup)
- [AzureSubnet](#azuresubnet)
- [AzureSubscription](#azuresubscription)
- [AzureVirtualMachine](#azurevirtualmachine)
- [AzureVirtualMachineState](#azurevirtualmachinestate)
- [AzureVirtualNetwork](#azurevirtualnetwork)
- [AzureVirtualNetworkPeering](#azurevirtualnetworkpeering)
- [BamRegAppRunTime](#bamregappruntime)
- [Base64PeFileWritten](#base64pefilewritten)
- [BcmFileWritten](#bcmfilewritten)
- [BehaviorWhitelisted](#behaviorwhitelisted)
- [BillingInfo](#billinginfo)
- [BITSJobCreated](#bitsjobcreated)
- [BITSJobFileInfo](#bitsjobfileinfo)
- [BITSJobInfo](#bitsjobinfo)
- [BITSJobMetadata](#bitsjobmetadata)
- [BlakHoleFileWritten](#blakholefilewritten)
- [BlfFileWritten](#blffilewritten)
- [BlockThreadFailed](#blockthreadfailed)
- [BMLFeatureData](#bmlfeaturedata)
- [BmpFileWritten](#bmpfilewritten)
- [BootLoaderStatus](#bootloaderstatus)
- [BootLoopProtectionTelemetry](#bootloopprotectiontelemetry)
- [BPFCommandIssued](#bpfcommandissued)
- [BrotliFileWritten](#brotlifilewritten)
- [BrowserAccountInfo](#browseraccountinfo)
- [BrowserCookieInfo](#browsercookieinfo)
- [BrowserDownloadEnded](#browserdownloadended)
- [BrowserDownloadStarted](#browserdownloadstarted)
- [BrowserExtensionInfo](#browserextensioninfo)
- [BrowserExtensionStatus](#browserextensionstatus)
- [BrowserHistoryClearInfo](#browserhistoryclearinfo)
- [BrowserHistoryVisit](#browserhistoryvisit)
- [BrowserInjectedThread](#browserinjectedthread)
- [BrowserProxyInfo](#browserproxyinfo)
- [BZip2FileWritten](#bzip2filewritten)
- [CabFileWritten](#cabfilewritten)
- [CertificatePinningCompromised](#certificatepinningcompromised)
- [ChannelActive](#channelactive)
- [ChannelDataDownloadComplete](#channeldatadownloadcomplete)
- [ChannelVersionRequired](#channelversionrequired)
- [CidMigrationComplete](#cidmigrationcomplete)
- [CidMigrationConfirmation](#cidmigrationconfirmation)
- [CidMigrationError](#cidmigrationerror)
- [CidMigrationManifestDownloadComplete](#cidmigrationmanifestdownloadcomplete)
- [ClassifiedModuleLoad](#classifiedmoduleload)
- [ClassifiedProcessStart](#classifiedprocessstart)
- [ClassifiedSensitiveFileAccess](#classifiedsensitivefileaccess)
- [ClipboardCopy](#clipboardcopy)
- [ClipboardPaste](#clipboardpaste)
- [CloudAssociateTreeIdWithRoot](#cloudassociatetreeidwithroot)
- [CloudScanControl](#cloudscancontrol)
- [CodeSigningAltered](#codesigningaltered)
- [CommandHistory](#commandhistory)
- [CommsLogReset](#commslogreset)
- [ConfigDownloadComplete](#configdownloadcomplete)
- [ConfigStateUpdate](#configstateupdate)
- [ConfigurationLoaded](#configurationloaded)
- [ConfigurationProfileModified](#configurationprofilemodified)
- [ConfigurationProvisioningState](#configurationprovisioningstate)
- [ContainerizationUpdate](#containerizationupdate)
- [CrashNotification](#crashnotification)
- [CreateProcessArgs](#createprocessargs)
- [CreateService](#createservice)
- [CreateSocket](#createsocket)
- [CreateThreadKernelNoStartImage](#createthreadkernelnostartimage)
- [CreateThreadNoStartImage](#createthreadnostartimage)
- [CreateThreadReflectiveDll](#createthreadreflectivedll)
- [CriticalEnvironmentVariableChanged](#criticalenvironmentvariablechanged)
- [CriticalFileAccessed](#criticalfileaccessed)
- [CriticalFileModified](#criticalfilemodified)
- [CrxFileWritten](#crxfilewritten)
- [CSAResultsGenericDetectInfo](#csaresultsgenericdetectinfo)
- [CsKmCrashSummaryEvent](#cskmcrashsummaryevent)
- [CsUmProcessCrashAuxiliaryEvent](#csumprocesscrashauxiliaryevent)
- [CsUmProcessCrashSummaryEvent](#csumprocesscrashsummaryevent)
- [CurrentSystemTags](#currentsystemtags)
- [CustomIOABasicProcessDetectionInfoEvent](#customioabasicprocessdetectioninfoevent)
- [CustomIOADomainNameDetectionInfoEvent](#customioadomainnamedetectioninfoevent)
- [CustomIOAFileWrittenDetectionInfoEvent](#customioafilewrittendetectioninfoevent)
- [CustomIOANetworkConnectionDetectionInfoEvent](#customioanetworkconnectiondetectioninfoevent)
- [DataEgress](#dataegress)
- [DataProtectionArchiveAssessed](#dataprotectionarchiveassessed)
- [DataProtectionBrowserConnect](#dataprotectionbrowserconnect)
- [DataProtectionDataEncryption](#dataprotectiondataencryption)
- [DataProtectionPACDiagnostic](#dataprotectionpacdiagnostic)
- [DBusMessage](#dbusmessage)
- [DcBluetoothAuthorizationStatus](#dcbluetoothauthorizationstatus)
- [DcBluetoothDeviceBlocked](#dcbluetoothdeviceblocked)
- [DcBluetoothDeviceConnected](#dcbluetoothdeviceconnected)
- [DcBluetoothDeviceConnectedDetails](#dcbluetoothdeviceconnecteddetails)
- [DcBluetoothDeviceDisconnected](#dcbluetoothdevicedisconnected)
- [DcBluetoothDevicePolicyViolation](#dcbluetoothdevicepolicyviolation)
- [DcBluetoothDeviceProperties](#dcbluetoothdeviceproperties)
- [DcIdentification](#dcidentification)
- [DcOffline](#dcoffline)
- [DcOnline](#dconline)
- [DcRemovableStorageDeviceBlocked](#dcremovablestoragedeviceblocked)
- [DcRemovableStorageDeviceConnected](#dcremovablestoragedeviceconnected)
- [DcRemovableStorageDeviceDisconnected](#dcremovablestoragedevicedisconnected)
- [DcRemovableStorageDevicePolicyViolation](#dcremovablestoragedevicepolicyviolation)
- [DcStatus](#dcstatus)
- [DCSyncAttempted](#dcsyncattempted)
- [DcUsbConfigurationDescriptor](#dcusbconfigurationdescriptor)
- [DcUsbDeviceBlocked](#dcusbdeviceblocked)
- [DcUsbDeviceConnected](#dcusbdeviceconnected)
- [DcUsbDeviceDisconnected](#dcusbdevicedisconnected)
- [DcUsbDevicePolicyViolation](#dcusbdevicepolicyviolation)
- [DcUsbDeviceWhitelisted](#dcusbdevicewhitelisted)
- [DcUsbEndpointDescriptor](#dcusbendpointdescriptor)
- [DcUsbHIDDescriptor](#dcusbhiddescriptor)
- [DcUsbInterfaceDescriptor](#dcusbinterfacedescriptor)
- [DeactivateMobileSensorResponse](#deactivatemobilesensorresponse)
- [DebFileWritten](#debfilewritten)
- [DebuggableFlagTurnedOn](#debuggableflagturnedon)
- [DebuggedState](#debuggedstate)
- [DeliverLocalFXToCloud](#deliverlocalfxtocloud)
- [DeliverRulesEngineResultsToCloud](#deliverrulesengineresultstocloud)
- [DetectionExcluded](#detectionexcluded)
- [DeveloperOptionsStatus](#developeroptionsstatus)
- [DexFileWritten](#dexfilewritten)
- [DirectoryCreate](#directorycreate)
- [DirectoryTraversalOverSMB](#directorytraversaloversmb)
- [DiskCapacity](#diskcapacity)
- [DiskUtilization](#diskutilization)
- [DllInjection](#dllinjection)
- [DmgFileWritten](#dmgfilewritten)
- [DmpFileWritten](#dmpfilewritten)
- [DnsCache](#dnscache)
- [DnsRequest](#dnsrequest)
- [DnsRequestBlocked](#dnsrequestblocked)
- [DNSRequestDetectInfo](#dnsrequestdetectinfo)
- [DnsRequestResult](#dnsrequestresult)
- [DnsServer](#dnsserver)
- [DnsServerSigRedExploitAttemptEtw](#dnsserversigredexploitattemptetw)
- [DocumentProgramInjectedThread](#documentprograminjectedthread)
- [DotnetModuleLoadDetectInfo](#dotnetmoduleloaddetectinfo)
- [DriverLoad](#driverload)
- [DriverLoadBlocked](#driverloadblocked)
- [DriverLoadedV2DetectInfo](#driverloadedv2detectinfo)
- [DriverPreventFailed](#driverpreventfailed)
- [DriverPreventionStatus](#driverpreventionstatus)
- [DuplicateInstallFromPlayStore](#duplicateinstallfromplaystore)
- [DwgFileWritten](#dwgfilewritten)
- [DwmCompositionResourceExploitAttempt](#dwmcompositionresourceexploitattempt)
- [DxfFileWritten](#dxffilewritten)
- [EarlyExploitPivotDetect](#earlyexploitpivotdetect)
- [ECBDownloadComplete](#ecbdownloadcomplete)
- [EddScanStart](#eddscanstart)
- [EddScanStatus](#eddscanstatus)
- [EksCluster](#ekscluster)
- [EksFargateProfile](#eksfargateprofile)
- [EksNodeGroup](#eksnodegroup)
- [ELFFileWritten](#elffilewritten)
- [EmailArchiveFileWritten](#emailarchivefilewritten)
- [EmailFileWritten](#emailfilewritten)
- [EndOfProcess](#endofprocess)
- [EntropyScan](#entropyscan)
- [ErrorEvent](#errorevent)
- [EseFileWritten](#esefilewritten)
- [EtwComponentResponse](#etwcomponentresponse)
- [EtwErrorEvent](#etwerrorevent)
- [EventLogCleared](#eventlogcleared)
- [EventTapInfo](#eventtapinfo)
- [ExcelDocumentOpened](#exceldocumentopened)
- [ExecutableDeleted](#executabledeleted)
- [ExtendedExploitMitigationViolatedDetectInfo](#extendedexploitmitigationviolateddetectinfo)
- [FalconHostFileTamperingInfo](#falconhostfiletamperinginfo)
- [FalconHostRegTamperingInfo](#falconhostregtamperinginfo)
- [FalconProcessHandleOpDetectInfo](#falconprocesshandleopdetectinfo)
- [FalconServiceStatus](#falconservicestatus)
- [FfcBytePatternScanResult](#ffcbytepatternscanresult)
- [FileAccessOperationOverSMB](#fileaccessoperationoversmb)
- [FileContentsChanged](#filecontentschanged)
- [FileCreateInfo](#filecreateinfo)
- [FileDeleted](#filedeleted)
- [FileDeleteInfo](#filedeleteinfo)
- [FileDescriptorMonitor](#filedescriptormonitor)
- [FileDetectInfo](#filedetectinfo)
- [FileEntry](#fileentry)
- [FileExtendedAttrOperation](#fileextendedattroperation)
- [FileHashesEvent](#filehashesevent)
- [FileInfo](#fileinfo)
- [FileIntegrityMonitorRuleMatched](#fileintegritymonitorrulematched)
- [FileOfInterestBasicInfo](#fileofinterestbasicinfo)
- [FileOpenInfo](#fileopeninfo)
- [FileRenameInfo](#filerenameinfo)
- [FileSetMode](#filesetmode)
- [FileSignatureMismatch](#filesignaturemismatch)
- [FileSignatureStatistics](#filesignaturestatistics)
- [FilesStatisticInfo](#filesstatisticinfo)
- [FileStatFsInfo](#filestatfsinfo)
- [FileSystemAttributesStatus](#filesystemattributesstatus)
- [FileSystemContainmentStatus](#filesystemcontainmentstatus)
- [FileSystemOperationBlocked](#filesystemoperationblocked)
- [FileSystemOperationDetectInfo](#filesystemoperationdetectinfo)
- [FileTimestampMetadata](#filetimestampmetadata)
- [FileTimestampsModified](#filetimestampsmodified)
- [FileVaultStatus](#filevaultstatus)
- [FileWrittenAndExecutedInContainer](#filewrittenandexecutedincontainer)
- [FileWrittenWithEntropyHigh](#filewrittenwithentropyhigh)
- [FirewallChangeOption](#firewallchangeoption)
- [FirewallDeleteRule](#firewalldeleterule)
- [FirewallDeleteRuleIP4](#firewalldeleteruleip4)
- [FirewallDeleteRuleIP6](#firewalldeleteruleip6)
- [FirewallDisabled](#firewalldisabled)
- [FirewallEnabled](#firewallenabled)
- [FirewallRuleApplicationFailed](#firewallruleapplicationfailed)
- [FirewallRuleInfo](#firewallruleinfo)
- [FirewallRuleIP4](#firewallruleip4)
- [FirewallRuleIP4Matched](#firewallruleip4matched)
- [FirewallRuleIP6](#firewallruleip6)
- [FirewallRuleIP6Matched](#firewallruleip6matched)
- [FirewallSetRule](#firewallsetrule)
- [FirewallSetRuleIP4](#firewallsetruleip4)
- [FirewallSetRuleIP6](#firewallsetruleip6)
- [FirmwareAnalysisErrorEvent](#firmwareanalysiserrorevent)
- [FirmwareAnalysisHardwareData](#firmwareanalysishardwaredata)
- [FirmwareAnalysisStatus](#firmwareanalysisstatus)
- [FirmwareImageAnalyzed](#firmwareimageanalyzed)
- [FirmwareRegionMeasured](#firmwareregionmeasured)
- [FlashThreadCreateProcess](#flashthreadcreateprocess)
- [ForensicsCollectorLog](#forensicscollectorlog)
- [ForensicsCollectorOffline](#forensicscollectoroffline)
- [ForensicsCollectorOnline](#forensicscollectoronline)
- [FreeArcFileWritten](#freearcfilewritten)
- [FsPostCreate](#fspostcreate)
- [FsPostOpen](#fspostopen)
- [FsPostOpenSnapshotFile](#fspostopensnapshotfile)
- [FsPostOpenUpImpersonating](#fspostopenupimpersonating)
- [FsVolumeMounted](#fsvolumemounted)
- [FsVolumeReadInfo](#fsvolumereadinfo)
- [FsVolumeUnmounted](#fsvolumeunmounted)
- [FtpCommand](#ftpcommand)
- [GcpAsset](#gcpasset)
- [GcpComputeDisk](#gcpcomputedisk)
- [GcpComputeFirewall](#gcpcomputefirewall)
- [GcpComputeImage](#gcpcomputeimage)
- [GcpComputeInstance](#gcpcomputeinstance)
- [GcpComputeNetwork](#gcpcomputenetwork)
- [GcpComputeNetworkInterface](#gcpcomputenetworkinterface)
- [GcpComputeNetworkPeering](#gcpcomputenetworkpeering)
- [GcpComputeSubnetwork](#gcpcomputesubnetwork)
- [GcpIamServiceAccount](#gcpiamserviceaccount)
- [GcpProject](#gcpproject)
- [GenericFileWritten](#genericfilewritten)
- [GetAsyncKeyStateEtwBatch](#getasynckeystateetwbatch)
- [GifFileWritten](#giffilewritten)
- [GroupAccount](#groupaccount)
- [GroupIdentity](#groupidentity)
- [GzipFileWritten](#gzipfilewritten)
- [HarmfulAppData](#harmfulappdata)
- [HeapSprayAttempt](#heapsprayattempt)
- [HookedAndroidMethodFound](#hookedandroidmethodfound)
- [HookedDriverObject](#hookeddriverobject)
- [HostedServiceStarted](#hostedservicestarted)
- [HostedServiceStatusInfo](#hostedservicestatusinfo)
- [HostedServiceStopped](#hostedservicestopped)
- [HostInfo](#hostinfo)
- [HostnameChanged](#hostnamechanged)
- [HostTimeModified](#hosttimemodified)
- [HttpRequest](#httprequest)
- [HttpRequestDetect](#httprequestdetect)
- [HttpRequestV2Detect](#httprequestv2detect)
- [HttpResponse](#httpresponse)
- [HttpVisibilityStatus](#httpvisibilitystatus)
- [IBEBChannelFileEnforcementResponse](#ibebchannelfileenforcementresponse)
- [IdpCloudHealthCheck](#idpcloudhealthcheck)
- [IdpCloudHealthConfigurationsGetResponse](#idpcloudhealthconfigurationsgetresponse)
- [IdpCloudHealthConfigurationsSetResponse](#idpcloudhealthconfigurationssetresponse)
- [IdpCloudHealthStatus](#idpcloudhealthstatus)
- [IdpConnectionsOverloadNotification](#idpconnectionsoverloadnotification)
- [IdpContainerRestarted](#idpcontainerrestarted)
- [IdpDcPerfReport](#idpdcperfreport)
- [IdpDcTiConfiguration](#idpdcticonfiguration)
- [IdpEntityRiskScoreChange](#idpentityriskscorechange)
- [IdpIdaasCorrelate](#idpidaascorrelate)
- [IdpPacketDiversionConnectionsOverloadNotification](#idppacketdiversionconnectionsoverloadnotification)
- [IdpPacketDiversionLdapsConnectionsOverloadNotification](#idppacketdiversionldapsconnectionsoverloadnotification)
- [IdpPolicyAccessRuleMatch](#idppolicyaccessrulematch)
- [IdpPolicyAccountEventRuleMatch](#idppolicyaccounteventrulematch)
- [IdpPolicyAlertRuleMatch](#idppolicyalertrulematch)
- [IdpPolicyCloudAccessRuleMatch](#idppolicycloudaccessrulematch)
- [IdpPolicyFederatedAccessRuleMatch](#idppolicyfederatedaccessrulematch)
- [IdpTelemetryData](#idptelemetrydata)
- [IdpWatchdogConfigurationsGetResponse](#idpwatchdogconfigurationsgetresponse)
- [IdpWatchdogConfigurationsSetResponse](#idpwatchdogconfigurationssetresponse)
- [IdpWatchdogReEnabled](#idpwatchdogreenabled)
- [IdpWatchdogRemediationActionRequest](#idpwatchdogremediationactionrequest)
- [IdpWatchdogRemediationActionTaken](#idpwatchdogremediationactiontaken)
- [IdpWatchdogRemediationActionTakenForCpu](#idpwatchdogremediationactiontakenforcpu)
- [IdpWatchdogRemediationActionTakenForMemory](#idpwatchdogremediationactiontakenformemory)
- [IdwFileWritten](#idwfilewritten)
- [ImageHash](#imagehash)
- [ImapCommand](#imapcommand)
- [ImgExtensionFileWritten](#imgextensionfilewritten)
- [ImpersonationTokenInfo](#impersonationtokeninfo)
- [InboundHttpHeader](#inboundhttpheader)
- [InboundHttpParsingStatus](#inboundhttpparsingstatus)
- [InjectedThread](#injectedthread)
- [InjectedThreadFromUnsignedModule](#injectedthreadfromunsignedmodule)
- [InstallBundleDownloadComplete](#installbundledownloadcomplete)
- [InstalledApplication](#installedapplication)
- [InstalledBrowserExtension](#installedbrowserextension)
- [InstalledUpdates](#installedupdates)
- [InstallFromUnknownSourcesStatus](#installfromunknownsourcesstatus)
- [InstallServiceDownloadComplete](#installservicedownloadcomplete)
- [InstanceMetadata](#instancemetadata)
- [InternetExposureData](#internetexposuredata)
- [IntrusivePackageDiscovered](#intrusivepackagediscovered)
- [IntrusiveProcessDiscovered](#intrusiveprocessdiscovered)
- [IntrusivePropertyDiscovered](#intrusivepropertydiscovered)
- [IOServiceRegister](#ioserviceregister)
- [IoSessionConnected](#iosessionconnected)
- [IoSessionLoggedOn](#iosessionloggedon)
- [IPCDetectInfo](#ipcdetectinfo)
- [IsoExtensionFileWritten](#isoextensionfilewritten)
- [JarFileWritten](#jarfilewritten)
- [JavaClassFileWritten](#javaclassfilewritten)
- [JavaInjectedThread](#javainjectedthread)
- [JpegFileWritten](#jpegfilewritten)
- [JumpListInfo](#jumplistinfo)
- [K8SAdmissionReviewResult](#k8sadmissionreviewresult)
- [K8SAdmissionReviewResultPrime](#k8sadmissionreviewresultprime)
- [K8SCluster](#k8scluster)
- [K8SClusterInfo](#k8sclusterinfo)
- [K8SDaemonSet](#k8sdaemonset)
- [K8SDeployment](#k8sdeployment)
- [K8SEphemeralContainer](#k8sephemeralcontainer)
- [K8SInitContainer](#k8sinitcontainer)
- [K8SInitContainerStatus](#k8sinitcontainerstatus)
- [K8SNode](#k8snode)
- [K8SPod](#k8spod)
- [K8SProductConfig](#k8sproductconfig)
- [K8SReplicaSet](#k8sreplicaset)
- [K8SResource](#k8sresource)
- [K8SRunningContainer](#k8srunningcontainer)
- [K8SRunningContainerStatus](#k8srunningcontainerstatus)
- [K8SService](#k8sservice)
- [K8SSnapshot](#k8ssnapshot)
- [K8SWatchStarted](#k8swatchstarted)
- [K8SWatchStopped](#k8swatchstopped)
- [KernelCallbackTablePatch](#kernelcallbacktablepatch)
- [KernelCallbackTableUpdate](#kernelcallbacktableupdate)
- [KernelExtension](#kernelextension)
- [KernelModeExecImage](#kernelmodeexecimage)
- [KernelModeLoadImage](#kernelmodeloadimage)
- [KernelParameter](#kernelparameter)
- [KernelServiceStarted](#kernelservicestarted)
- [KextLoad](#kextload)
- [KextUnload](#kextunload)
- [KillProcessError](#killprocesserror)
- [LFODownloadComplete](#lfodownloadcomplete)
- [LFODownloadConfirmation](#lfodownloadconfirmation)
- [LfoUploadDataComplete](#lfouploaddatacomplete)
- [LfoUploadDataFailed](#lfouploaddatafailed)
- [LfoUploadDataUnneeded](#lfouploaddataunneeded)
- [LfoUploadStart](#lfouploadstart)
- [LhaFileWritten](#lhafilewritten)
- [LightningUnresponsiveStatus](#lightningunresponsivestatus)
- [LinkFileInfo](#linkfileinfo)
- [LnkFileWritten](#lnkfilewritten)
- [LoadImage](#loadimage)
- [LocalGroupIdentity](#localgroupidentity)
- [LocalIpAddressIP4](#localipaddressip4)
- [LocalIpAddressIP6](#localipaddressip6)
- [LocalIpAddressRemovedIP4](#localipaddressremovedip4)
- [LocalIpAddressRemovedIP6](#localipaddressremovedip6)
- [LocalWindowsUserUpdate](#localwindowsuserupdate)
- [LockdownModeStatus](#lockdownmodestatus)
- [LockScreenStatus](#lockscreenstatus)
- [LogCollectorDeploymentStatus](#logcollectordeploymentstatus)
- [LogEntry](#logentry)
- [LoginItemAdded](#loginitemadded)
- [LogonBehaviorCompositionDetectInfo](#logonbehaviorcompositiondetectinfo)
- [LowILModuleLoadAttempt](#lowilmoduleloadattempt)
- [LRZipFileWritten](#lrzipfilewritten)
- [LsassHandleFromUnsignedModule](#lsasshandlefromunsignedmodule)
- [LSQuarantineEvent](#lsquarantineevent)
- [LZ4FileWritten](#lz4filewritten)
- [LzfseFileWritten](#lzfsefilewritten)
- [LZipFileWritten](#lzipfilewritten)
- [LzmaFileWritten](#lzmafilewritten)
- [LZOFileWritten](#lzofilewritten)
- [MacFsEventRecord](#macfseventrecord)
- [MachOFileWritten](#machofilewritten)
- [MachOHeaderParsed](#machoheaderparsed)
- [MacKnowledgeActivityEnd](#macknowledgeactivityend)
- [MacKnowledgeActivityStart](#macknowledgeactivitystart)
- [MacMRU](#macmru)
- [MacroContentInfo](#macrocontentinfo)
- [MacroDetectInfo](#macrodetectinfo)
- [MalPaths](#malpaths)
- [ManifestDownloadComplete](#manifestdownloadcomplete)
- [MbrOverwriteRawDetectInfo](#mbroverwriterawdetectinfo)
- [MemoryAdvise](#memoryadvise)
- [MemoryLocked](#memorylocked)
- [MemoryMapped](#memorymapped)
- [MemoryProtectionChanged](#memoryprotectionchanged)
- [MemoryProtectionUpdated](#memoryprotectionupdated)
- [MemoryScanEnabled](#memoryscanenabled)
- [MemoryScanErrorEvent](#memoryscanerrorevent)
- [MftBootSector](#mftbootsector)
- [MftRecord](#mftrecord)
- [MobileAppIdentifiers](#mobileappidentifiers)
- [MobileAppsManifest](#mobileappsmanifest)
- [MobileDetection](#mobiledetection)
- [MobileOsForensicsReport](#mobileosforensicsreport)
- [MobileOsIntegrityStatus](#mobileosintegritystatus)
- [MobilePowerStats](#mobilepowerstats)
- [ModifyServiceBinary](#modifyservicebinary)
- [ModuleBlockedEvent](#moduleblockedevent)
- [ModuleBlockedEventWithPatternId](#moduleblockedeventwithpatternid)
- [ModuleCertificateInfo2](#modulecertificateinfo2)
- [ModuleDetectInfo](#moduledetectinfo)
- [ModuleDownloadComplete](#moduledownloadcomplete)
- [ModuleLoadV3DetectInfo](#moduleloadv3detectinfo)
- [MotwWritten](#motwwritten)
- [MountedVolume](#mountedvolume)
- [MpThreat](#mpthreat)
- [MpThreatAction](#mpthreataction)
- [MpThreatDetection](#mpthreatdetection)
- [MpThreatDetectionWMI](#mpthreatdetectionwmi)
- [MpThreatWMI](#mpthreatwmi)
- [MSDocxFileWritten](#msdocxfilewritten)
- [MsiFileWritten](#msifilewritten)
- [MsiTransactionExecuted](#msitransactionexecuted)
- [MSPptxFileWritten](#mspptxfilewritten)
- [MSVsdxFileWritten](#msvsdxfilewritten)
- [MSXlsxFileWritten](#msxlsxfilewritten)
- [NamedMutantHandleClosedTelemetry](#namedmutanthandleclosedtelemetry)
- [NamedPipe](#namedpipe)
- [NamedPipeDetectInfo](#namedpipedetectinfo)
- [NamedSemaphoreHandleClosedTelemetry](#namedsemaphorehandleclosedtelemetry)
- [NamespaceChanged](#namespacechanged)
- [NeighborListIP4](#neighborlistip4)
- [NeighborListIP6](#neighborlistip6)
- [NetShareAdd](#netshareadd)
- [NetShareDelete](#netsharedelete)
- [NetShareInfo](#netshareinfo)
- [NetShareSecurityModify](#netsharesecuritymodify)
- [NetworkCloseIP4](#networkcloseip4)
- [NetworkCloseIP6](#networkcloseip6)
- [NetworkConnectIP4](#networkconnectip4)
- [NetworkConnectIP4Blocked](#networkconnectip4blocked)
- [NetworkConnectIP4DetectInfo](#networkconnectip4detectinfo)
- [NetworkConnectIP6](#networkconnectip6)
- [NetworkConnectIP6Blocked](#networkconnectip6blocked)
- [NetworkConnectIP6DetectInfo](#networkconnectip6detectinfo)
- [NetworkContainmentCompleted](#networkcontainmentcompleted)
- [NetworkDnsSuffix](#networkdnssuffix)
- [NetworkEndPointDataUsage](#networkendpointdatausage)
- [NetworkHostsFileEntry](#networkhostsfileentry)
- [NetworkIcmpDataIP4](#networkicmpdataip4)
- [NetworkIcmpDataIP6](#networkicmpdataip6)
- [NetworkInterfaceStatistics](#networkinterfacestatistics)
- [NetworkLinkConfigGetAddress](#networklinkconfiggetaddress)
- [NetworkLinkConfigGetLink](#networklinkconfiggetlink)
- [NetworkListenIP4](#networklistenip4)
- [NetworkListenIP6](#networklistenip6)
- [NetworkModuleLoadAttempt](#networkmoduleloadattempt)
- [NetworkOutboundPortScanDetectInfo](#networkoutboundportscandetectinfo)
- [NetworkReceiveAcceptIP4](#networkreceiveacceptip4)
- [NetworkReceiveAcceptIP6](#networkreceiveacceptip6)
- [NetworkStatisticsIP4](#networkstatisticsip4)
- [NetworkStatisticsIP6](#networkstatisticsip6)
- [NetworkStatisticsTCP4](#networkstatisticstcp4)
- [NetworkStatisticsTCP6](#networkstatisticstcp6)
- [NetworkStatisticsUDP4](#networkstatisticsudp4)
- [NetworkStatisticsUDP6](#networkstatisticsudp6)
- [NetworkSummary](#networksummary)
- [NetworkUncontainmentCompleted](#networkuncontainmentcompleted)
- [NewExecutableRenamed](#newexecutablerenamed)
- [NewExecutableWritten](#newexecutablewritten)
- [NewScriptWritten](#newscriptwritten)
- [NtfsLinkCreatedDetectInfo](#ntfslinkcreateddetectinfo)
- [NtfsQueryEaExploitAttempt](#ntfsqueryeaexploitattempt)
- [NullPageProtectionModificationAttempt](#nullpageprotectionmodificationattempt)
- [NullPageUnmapAttempt](#nullpageunmapattempt)
- [ObjCRuntimeAltered](#objcruntimealtered)
- [OciContainerComplianceInfo](#ocicontainercomplianceinfo)
- [OciContainerEngineInfo](#ocicontainerengineinfo)
- [OciContainerHeartbeat](#ocicontainerheartbeat)
- [OciContainerInfo](#ocicontainerinfo)
- [OciContainerPlumbingSummary](#ocicontainerplumbingsummary)
- [OciContainerStarted](#ocicontainerstarted)
- [OciContainerStopped](#ocicontainerstopped)
- [OciContainerTelemetry](#ocicontainertelemetry)
- [OciImageHeartbeat](#ociimageheartbeat)
- [OciImageInfo](#ociimageinfo)
- [OdsActionStatus](#odsactionstatus)
- [OdsCancelRequestReceived](#odscancelrequestreceived)
- [OdsMaliciousFileFound](#odsmaliciousfilefound)
- [OdsProfileReceived](#odsprofilereceived)
- [OdsScanComplete](#odsscancomplete)
- [OdsScheduleCanceled](#odsschedulecanceled)
- [OdsScheduleCancelRequestReceived](#odsschedulecancelrequestreceived)
- [OdsScheduleRequestReceived](#odsschedulerequestreceived)
- [OdsStarted](#odsstarted)
- [OdsStartRequestReceived](#odsstartrequestreceived)
- [OdsStatus](#odsstatus)
- [OleFileWritten](#olefilewritten)
- [OoxmlFileWritten](#ooxmlfilewritten)
- [OpenDirectoryAttributeAdd](#opendirectoryattributeadd)
- [OpenDirectoryAttributeRemove](#opendirectoryattributeremove)
- [OpenDirectoryAttributeSet](#opendirectoryattributeset)
- [OpenDirectoryCreateUser](#opendirectorycreateuser)
- [OpenDirectoryDeleteUser](#opendirectorydeleteuser)
- [OpenDirectoryGroupAdd](#opendirectorygroupadd)
- [OpenDirectoryGroupRemove](#opendirectorygroupremove)
- [OpenDirectoryGroupSet](#opendirectorygroupset)
- [OpenDirectoryPasswordModification](#opendirectorypasswordmodification)
- [OsfmDownloadComplete](#osfmdownloadcomplete)
- [OsUpdateTimestamp](#osupdatetimestamp)
- [OsVersionInfo](#osversioninfo)
- [PackageManagerDownloadComplete](#packagemanagerdownloadcomplete)
- [PackedExecutableWritten](#packedexecutablewritten)
- [PacketDiversionConnectionsOverloadConfigurationResponse](#packetdiversionconnectionsoverloadconfigurationresponse)
- [PacketFilterAttached](#packetfilterattached)
- [PathUnexpectedlyReadable](#pathunexpectedlyreadable)
- [PatternHandlingError](#patternhandlingerror)
- [PcaAppLaunchEntry](#pcaapplaunchentry)
- [PcaGeneralDbEntry](#pcageneraldbentry)
- [PdfFileWritten](#pdffilewritten)
- [PeaFileWritten](#peafilewritten)
- [PeCodePageInfo](#pecodepageinfo)
- [PeFileWritten](#pefilewritten)
- [PeFileWrittenDetectInfo](#pefilewrittendetectinfo)
- [PeHeaderInfo](#peheaderinfo)
- [PeHeaderOptionalInfo](#peheaderoptionalinfo)
- [PeLanguageId](#pelanguageid)
- [PemFileWritten](#pemfilewritten)
- [PeSectionInfo](#pesectioninfo)
- [PeVersionInfo](#peversioninfo)
- [PhpBase64Decode](#phpbase64decode)
- [PhpEvalString](#phpevalstring)
- [PhpExecuteScript](#phpexecutescript)
- [PngFileWritten](#pngfilewritten)
- [PodInfo](#podinfo)
- [PodProductConfig](#podproductconfig)
- [Pop3Command](#pop3command)
- [PrefetchFile](#prefetchfile)
- [PrivilegedProcessHandle](#privilegedprocesshandle)
- [PrivilegedProcessHandleFromUnsignedModule](#privilegedprocesshandlefromunsignedmodule)
- [ProcessActivitySummary](#processactivitysummary)
- [ProcessAncestryInformation](#processancestryinformation)
- [ProcessBlocked](#processblocked)
- [ProcessControl](#processcontrol)
- [ProcessDataUsage](#processdatausage)
- [ProcessEnvironmentEmpty](#processenvironmentempty)
- [ProcessExecOnPackedExecutable](#processexeconpackedexecutable)
- [ProcessExecOnRDPFile](#processexeconrdpfile)
- [ProcessExecOnSMBFile](#processexeconsmbfile)
- [ProcessExecOnWinRMFile](#processexeconwinrmfile)
- [ProcessHandleOpDetectInfo](#processhandleopdetectinfo)
- [ProcessHandleOpDowngraded](#processhandleopdowngraded)
- [ProcessHandleTableEntry](#processhandletableentry)
- [ProcessInjection](#processinjection)
- [ProcessOpenedFileDescriptor](#processopenedfiledescriptor)
- [ProcessPatternTelemetry](#processpatterntelemetry)
- [ProcessRollup](#processrollup)
- [ProcessRollup2](#processrollup2)
- [ProcessRollup2Stats](#processrollup2stats)
- [ProcessSelfDeleted](#processselfdeleted)
- [ProcessSessionCreated](#processsessioncreated)
- [ProcessSignal](#processsignal)
- [ProcessState](#processstate)
- [ProcessSubstituteUser](#processsubstituteuser)
- [ProcessTokenPrivilegesEdited](#processtokenprivilegesedited)
- [ProcessTokenStolen](#processtokenstolen)
- [ProcessTrace](#processtrace)
- [ProcessTreeCompositionPatternTelemetry](#processtreecompositionpatterntelemetry)
- [ProcessWitness](#processwitness)
- [PromiscuousBindIP4](#promiscuousbindip4)
- [PromiscuousBindIP6](#promiscuousbindip6)
- [ProtectVmEtw](#protectvmetw)
- [ProvisioningChannelVersionRequired](#provisioningchannelversionrequired)
- [ProvisioningEnded](#provisioningended)
- [ProvisioningStarted](#provisioningstarted)
- [ProvisioningStatusUpdate](#provisioningstatusupdate)
- [PtActivationStatus](#ptactivationstatus)
- [PtTelemetry](#pttelemetry)
- [PtyAttached](#ptyattached)
- [PtyCreated](#ptycreated)
- [PtyDetached](#ptydetached)
- [PythonFileWritten](#pythonfilewritten)
- [QuarantineActionResult](#quarantineactionresult)
- [QuarantinedFile](#quarantinedfile)
- [QuarantinedFileState](#quarantinedfilestate)
- [QuarantineXattribute](#quarantinexattribute)
- [QueueApcEtw](#queueapcetw)
- [QuickAssistCookieInfo](#quickassistcookieinfo)
- [QuickAssistDownloadEnded](#quickassistdownloadended)
- [QuickAssistDownloadStarted](#quickassistdownloadstarted)
- [QuickAssistHistoryVisit](#quickassisthistoryvisit)
- [RansomwareCreateFile](#ransomwarecreatefile)
- [RansomwareFileAccessPattern](#ransomwarefileaccesspattern)
- [RansomwareOpenFile](#ransomwareopenfile)
- [RansomwareRenameFile](#ransomwarerenamefile)
- [RarFileWritten](#rarfilewritten)
- [RawBindIP4](#rawbindip4)
- [RawBindIP6](#rawbindip6)
- [RecentExecutionTimestamp](#recentexecutiontimestamp)
- [RecentlyModifiedFileExecutedInContainer](#recentlymodifiedfileexecutedincontainer)
- [RecoveryActionDeleteFilesComplete](#recoveryactiondeletefilescomplete)
- [RecoveryActionDeleteFilesReply](#recoveryactiondeletefilesreply)
- [RecoveryActionGetModuleTableRecordComplete](#recoveryactiongetmoduletablerecordcomplete)
- [RecoveryActionGetRuntimeSystemTagsComplete](#recoveryactiongetruntimesystemtagscomplete)
- [RecoveryActionGetSystemTagsComplete](#recoveryactiongetsystemtagscomplete)
- [RecoveryActionKillProcessesComplete](#recoveryactionkillprocessescomplete)
- [RecoveryActionKillProcessesReply](#recoveryactionkillprocessesreply)
- [RecoveryActionManipulateModuleTableComplete](#recoveryactionmanipulatemoduletablecomplete)
- [RecoveryActionRegistryCreateKeyComplete](#recoveryactionregistrycreatekeycomplete)
- [RecoveryActionRegistryCreateKeyReply](#recoveryactionregistrycreatekeyreply)
- [RecoveryActionRegistryDeleteKeyComplete](#recoveryactionregistrydeletekeycomplete)
- [RecoveryActionRegistryDeleteKeyReply](#recoveryactionregistrydeletekeyreply)
- [RecoveryActionRegistryDeleteValueKeyComplete](#recoveryactionregistrydeletevaluekeycomplete)
- [RecoveryActionRegistryDeleteValueKeyReply](#recoveryactionregistrydeletevaluekeyreply)
- [RecoveryActionRegistrySetValueKeyComplete](#recoveryactionregistrysetvaluekeycomplete)
- [RecoveryActionRegistrySetValueKeyReply](#recoveryactionregistrysetvaluekeyreply)
- [RecoveryActionSetRuntimeSystemTagsComplete](#recoveryactionsetruntimesystemtagscomplete)
- [RecoveryActionSetSystemTagsComplete](#recoveryactionsetsystemtagscomplete)
- [ReflectiveDllLoaded](#reflectivedllloaded)
- [ReflectiveDllOpenProcess](#reflectivedllopenprocess)
- [ReflectiveDotnetModuleLoad](#reflectivedotnetmoduleload)
- [RegCredAccessDetectInfo](#regcredaccessdetectinfo)
- [RegCrowdstrikeKeyUpdate](#regcrowdstrikekeyupdate)
- [RegCrowdstrikeValueUpdate](#regcrowdstrikevalueupdate)
- [RegFeatureUsageInfo](#regfeatureusageinfo)
- [RegGenericInfo](#reggenericinfo)
- [RegGenericKeyUpdate](#reggenerickeyupdate)
- [RegGenericValueUpdate](#reggenericvalueupdate)
- [RegisterRawInputDevicesEtw](#registerrawinputdevicesetw)
- [RegistryHiveFileWritten](#registryhivefilewritten)
- [RegistryOperationBlocked](#registryoperationblocked)
- [RegistryOperationDetectInfo](#registryoperationdetectinfo)
- [RegKeySecurityDecreasedFromUnsignedModule](#regkeysecuritydecreasedfromunsignedmodule)
- [RegNtPostOpenKeyEx](#regntpostopenkeyex)
- [RegNtPostOpenKeyExUpImpersonating](#regntpostopenkeyexupimpersonating)
- [RegShimCache](#regshimcache)
- [RegSystemConfigKeyUpdate](#regsystemconfigkeyupdate)
- [RegSystemConfigValueUpdate](#regsystemconfigvalueupdate)
- [RegValueQueryDetectInfo](#regvaluequerydetectinfo)
- [RemediationActionKillIP4Connection](#remediationactionkillip4connection)
- [RemediationActionKillIP6Connection](#remediationactionkillip6connection)
- [RemediationActionKillProcess](#remediationactionkillprocess)
- [RemediationActionQuarantineFile](#remediationactionquarantinefile)
- [RemediationActionQuarantineMacroFile](#remediationactionquarantinemacrofile)
- [RemediationActionQuarantineOfficeMacroFile](#remediationactionquarantineofficemacrofile)
- [RemediationActionRegistryRemoval](#remediationactionregistryremoval)
- [RemediationActionScheduledTaskRemoval](#remediationactionscheduledtaskremoval)
- [RemediationActionServiceRemoval](#remediationactionserviceremoval)
- [RemediationMonitorKillProcess](#remediationmonitorkillprocess)
- [RemediationMonitorQuarantineFile](#remediationmonitorquarantinefile)
- [RemediationMonitorRegistryRemoval](#remediationmonitorregistryremoval)
- [RemediationMonitorScheduledTaskRemoval](#remediationmonitorscheduledtaskremoval)
- [RemediationMonitorServiceRemoval](#remediationmonitorserviceremoval)
- [RemoteBruteForceDetectInfo](#remotebruteforcedetectinfo)
- [RemoteCommandResponse](#remotecommandresponse)
- [RemoteProcessMemoryRead](#remoteprocessmemoryread)
- [RemoteProcessMemoryWrite](#remoteprocessmemorywrite)
- [RemoteThreadCreate](#remotethreadcreate)
- [RemovableDiskModuleLoadAttempt](#removablediskmoduleloadattempt)
- [RemovableMediaFileWritten](#removablemediafilewritten)
- [RemovableMediaVolumeMounted](#removablemediavolumemounted)
- [RemovableMediaVolumeUnmounted](#removablemediavolumeunmounted)
- [ResourceLimit](#resourcelimit)
- [ResourceUtilization](#resourceutilization)
- [RootkitDetectionResponse](#rootkitdetectionresponse)
- [RouteIP4](#routeip4)
- [RouteIP6](#routeip6)
- [RpmFileWritten](#rpmfilewritten)
- [RtfFileWritten](#rtffilewritten)
- [RuntimeEnvironmentVariable](#runtimeenvironmentvariable)
- [SafetyNetCheckFailed](#safetynetcheckfailed)
- [SafetyNetCompatibilityStatus](#safetynetcompatibilitystatus)
- [SafetyNetVerifyAppsStatus](#safetynetverifyappsstatus)
- [SAMHashDumpFromUnsignedModule](#samhashdumpfromunsignedmodule)
- [ScheduledTaskDeleted](#scheduledtaskdeleted)
- [ScheduledTaskInfo](#scheduledtaskinfo)
- [ScheduledTaskModified](#scheduledtaskmodified)
- [ScheduledTaskRegistered](#scheduledtaskregistered)
- [ScheduledTaskTamperingRegistryOperation](#scheduledtasktamperingregistryoperation)
- [ScheduledTaskTemplateDetectInfo](#scheduledtasktemplatedetectinfo)
- [ScreenshotTakenEtw](#screenshottakenetw)
- [ScriptControlBlocked](#scriptcontrolblocked)
- [ScriptControlDetectInfo](#scriptcontroldetectinfo)
- [ScriptControlDetectInvalidInfo](#scriptcontroldetectinvalidinfo)
- [ScriptControlDotNetMetadata](#scriptcontroldotnetmetadata)
- [ScriptControlErrorEvent](#scriptcontrolerrorevent)
- [ScriptControlScanInfo](#scriptcontrolscaninfo)
- [ScriptControlScanTelemetry](#scriptcontrolscantelemetry)
- [ScriptFileContentsDetectInfo](#scriptfilecontentsdetectinfo)
- [ScriptFileWrittenInfo](#scriptfilewritteninfo)
- [SecureTrafficDecrypted](#securetrafficdecrypted)
- [SEHOverWriteAttempt](#sehoverwriteattempt)
- [SELinuxStatus](#selinuxstatus)
- [SensitiveWmiQuery](#sensitivewmiquery)
- [SensorAntiTamperState](#sensorantitamperstate)
- [SensorEnteredSafemode](#sensorenteredsafemode)
- [SensorGroupingTagsUpdate](#sensorgroupingtagsupdate)
- [SensorHeartbeat](#sensorheartbeat)
- [SensorMetadataUpdate](#sensormetadataupdate)
- [SensorSelfDiagnosticAlert](#sensorselfdiagnosticalert)
- [SensorSelfDiagnosticTelemetry](#sensorselfdiagnostictelemetry)
- [SensorSettingsUpdate](#sensorsettingsupdate)
- [SensorTampering](#sensortampering)
- [ServicesStatusInfo](#servicesstatusinfo)
- [ServiceStarted](#servicestarted)
- [ServiceStopped](#servicestopped)
- [SessionPatternTelemetry](#sessionpatterntelemetry)
- [SetThreadCtxEtw](#setthreadctxetw)
- [SetWindowsHook](#setwindowshook)
- [SetWindowsHookExEtw](#setwindowshookexetw)
- [SetWinEventHookEtw](#setwineventhooketw)
- [SevenZipFileWritten](#sevenzipfilewritten)
- [SharedObjectLoaded](#sharedobjectloaded)
- [ShellBagFileTimeStampMetadata](#shellbagfiletimestampmetadata)
- [ShellBagInfo](#shellbaginfo)
- [ShellCommandLineInfo](#shellcommandlineinfo)
- [ShimDbTag](#shimdbtag)
- [SignInfo](#signinfo)
- [SignInfoWithCertAndContext](#signinfowithcertandcontext)
- [SignInfoWithContext](#signinfowithcontext)
- [SigningIdentity](#signingidentity)
- [SigningPublicKey](#signingpublickey)
- [SldFileWritten](#sldfilewritten)
- [SmbClientNamedPipeConnectEtw](#smbclientnamedpipeconnectetw)
- [SmbClientShareClosedEtw](#smbclientshareclosedetw)
- [SmbClientShareLogonBruteForceLowThreshold](#smbclientsharelogonbruteforcelowthreshold)
- [SmbClientShareLogonBruteForceSuspected](#smbclientsharelogonbruteforcesuspected)
- [SmbClientShareOpenedEtw](#smbclientshareopenedetw)
- [SmbServerLocalNamedPipeOpenedEtw](#smbserverlocalnamedpipeopenedetw)
- [SmbServerShareOpenedEtw](#smbservershareopenedetw)
- [SmbServerV1AuditEtw](#smbserverv1auditetw)
- [SmtpAttachment](#smtpattachment)
- [SmtpCommand](#smtpcommand)
- [SmtpEmailMessage](#smtpemailmessage)
- [SnapshotVolumeMounted](#snapshotvolumemounted)
- [SourceCodeFileWritten](#sourcecodefilewritten)
- [SpotlightEntityBatch](#spotlightentitybatch)
- [SpotlightEntityBatchHeader](#spotlightentitybatchheader)
- [SpotlightEntitySystemState](#spotlightentitysystemstate)
- [SpotlightSearchEntry](#spotlightsearchentry)
- [SruApplicationResourceUsage](#sruapplicationresourceusage)
- [SruApplicationTimelineProvider](#sruapplicationtimelineprovider)
- [SruNetworkConnectivityUsage](#srunetworkconnectivityusage)
- [SruNetworkDataUsage](#srunetworkdatausage)
- [SSHClientAuthenticated](#sshclientauthenticated)
- [SsoApplicationAccess](#ssoapplicationaccess)
- [SsoApplicationAccessFailure](#ssoapplicationaccessfailure)
- [SsoUserLogon](#ssouserlogon)
- [SsoUserLogonFailure](#ssouserlogonfailure)
- [StaticAnalysisContainerTelemetry](#staticanalysiscontainertelemetry)
- [StaticConfigurationError](#staticconfigurationerror)
- [StorageEncryptionStatus](#storageencryptionstatus)
- [SudoCommandAttempt](#sudocommandattempt)
- [SuperfetchAppInfo](#superfetchappinfo)
- [SuperfetchAppSchedule](#superfetchappschedule)
- [SuspectCreateThreadStack](#suspectcreatethreadstack)
- [SuspendProcessError](#suspendprocesserror)
- [SuspiciousAndroidActivityFound](#suspiciousandroidactivityfound)
- [SuspiciousAndroidLogcatMessageFound](#suspiciousandroidlogcatmessagefound)
- [SuspiciousAndroidStackTraceElementFound](#suspiciousandroidstacktraceelementfound)
- [SuspiciousAndroidSystemPropertyFound](#suspiciousandroidsystempropertyfound)
- [SuspiciousAppFound](#suspiciousappfound)
- [SuspiciousCreateSymbolicLink](#suspiciouscreatesymboliclink)
- [SuspiciousCredentialModuleLoad](#suspiciouscredentialmoduleload)
- [SuspiciousDnsRequest](#suspiciousdnsrequest)
- [SuspiciousEseFileWritten](#suspiciousesefilewritten)
- [SuspiciousLackOfProcessRollupEvents](#suspiciouslackofprocessrollupevents)
- [SuspiciousPeFileWritten](#suspiciouspefilewritten)
- [SuspiciousPrivilegedProcessHandle](#suspiciousprivilegedprocesshandle)
- [SuspiciousRawDiskRead](#suspiciousrawdiskread)
- [SuspiciousRawDiskReadFromUnsignedModule](#suspiciousrawdiskreadfromunsignedmodule)
- [SuspiciousRegAsepUpdate](#suspiciousregasepupdate)
- [SuspiciousUserFontLoad](#suspicioususerfontload)
- [SuspiciousUserRemoteAPCAttempt](#suspicioususerremoteapcattempt)
- [SyntheticPR2Stats](#syntheticpr2stats)
- [SyntheticProcessRollup2](#syntheticprocessrollup2)
- [SyntheticProcessTrace](#syntheticprocesstrace)
- [SyntheticSharedObjectLoaded](#syntheticsharedobjectloaded)
- [SyntheticSystemdServiceCreated](#syntheticsystemdservicecreated)
- [SyntheticSystemdTimerCreated](#syntheticsystemdtimercreated)
- [SyntheticVirtualMemoryArea](#syntheticvirtualmemoryarea)
- [SyscacheEntry](#syscacheentry)
- [SysConfigInfo](#sysconfiginfo)
- [SystemCapacity](#systemcapacity)
- [SystemdServiceCreated](#systemdservicecreated)
- [SystemdServiceDeleted](#systemdservicedeleted)
- [SystemdServicePropertiesChanged](#systemdservicepropertieschanged)
- [SystemdTimerCreated](#systemdtimercreated)
- [SystemdTimerDeleted](#systemdtimerdeleted)
- [SystemdTimerPropertiesChanged](#systemdtimerpropertieschanged)
- [SystemExtension](#systemextension)
- [SystemPartitionAltered](#systempartitionaltered)
- [SystemPartitionStatus](#systempartitionstatus)
- [SystemTokenStolen](#systemtokenstolen)
- [SystemUpdatesBlockedByDNS](#systemupdatesblockedbydns)
- [SystemUpdatesBlockedByFilesystem](#systemupdatesblockedbyfilesystem)
- [SystemUpdatesBlockedByHTTP](#systemupdatesblockedbyhttp)
- [TarFileWritten](#tarfilewritten)
- [TccModification](#tccmodification)
- [TcgPcrInfo](#tcgpcrinfo)
- [TerminalSavedStateInfo](#terminalsavedstateinfo)
- [TerminateProcess](#terminateprocess)
- [TerminateRemoteProcessEtw](#terminateremoteprocessetw)
- [ThreadBlocked](#threadblocked)
- [ThreadPreviousModeMismatch](#threadpreviousmodemismatch)
- [TiffFileWritten](#tifffilewritten)
- [TlsClientHello](#tlsclienthello)
- [TokenImpersonated](#tokenimpersonated)
- [TrampolineDetected](#trampolinedetected)
- [TriggeredMemoryDumpResponse](#triggeredmemorydumpresponse)
- [UACAxisElevation](#uacaxiselevation)
- [UACCOMElevation](#uaccomelevation)
- [UACCredentialCaptureElevation](#uaccredentialcaptureelevation)
- [UACExeElevation](#uacexeelevation)
- [UACMSIElevation](#uacmsielevation)
- [UmppaErrorEvent](#umppaerrorevent)
- [UmppcDetectInfo](#umppcdetectinfo)
- [UmppcEntryAnomaly](#umppcentryanomaly)
- [UnclassifiedRegValueUpdate](#unclassifiedregvalueupdate)
- [UncontainerizeAppResponse](#uncontainerizeappresponse)
- [UnexpectedDynamicLibraryLoaded](#unexpecteddynamiclibraryloaded)
- [UnexpectedEnvironmentVariable](#unexpectedenvironmentvariable)
- [UnexpectedFileFound](#unexpectedfilefound)
- [UnixFileWritten](#unixfilewritten)
- [UnixName](#unixname)
- [UnsignedModuleLoad](#unsignedmoduleload)
- [UpdateManifestDownloadComplete](#updatemanifestdownloadcomplete)
- [UsbDeviceInfo](#usbdeviceinfo)
- [UserAccessLogEntry](#useraccesslogentry)
- [UserAccount](#useraccount)
- [UserAccountAddedToGroup](#useraccountaddedtogroup)
- [UserAccountCreated](#useraccountcreated)
- [UserAccountDeleted](#useraccountdeleted)
- [UserAccountRemovedFromGroup](#useraccountremovedfromgroup)
- [UserAssistAppLaunchInfo](#userassistapplaunchinfo)
- [UserEatAccessMonitoring](#usereataccessmonitoring)
- [UserExceptionDEP](#userexceptiondep)
- [UserFontLoad](#userfontload)
- [UserGroupCreated](#usergroupcreated)
- [UserGroupDeleted](#usergroupdeleted)
- [UserIdentity](#useridentity)
- [UserInformationEtw](#userinformationetw)
- [UserLogoff](#userlogoff)
- [UserLogon](#userlogon)
- [UserLogonFailed](#userlogonfailed)
- [UserLogonFailed2](#userlogonfailed2)
- [UserSetProcessBreakOnTermination](#usersetprocessbreakontermination)
- [USNRecord](#usnrecord)
- [VdiFileWritten](#vdifilewritten)
- [VerifyAppsDisabled](#verifyappsdisabled)
- [VirtualMemoryArea](#virtualmemoryarea)
- [VMClusterInfo](#vmclusterinfo)
- [VmcSensorStatus](#vmcsensorstatus)
- [VmcVmAsset](#vmcvmasset)
- [VmdkFileWritten](#vmdkfilewritten)
- [VolumeSnapshotCreated](#volumesnapshotcreated)
- [VolumeSnapshotDeleted](#volumesnapshotdeleted)
- [VolumeSnapshotOperationBlocked](#volumesnapshotoperationblocked)
- [VulnerableDriverDetectInfo](#vulnerabledriverdetectinfo)
- [WebScriptFileWritten](#webscriptfilewritten)
- [WebShellDetected](#webshelldetected)
- [WfpFilterTamperingFilterAdded](#wfpfiltertamperingfilteradded)
- [WfpFilterTamperingFilterDeleted](#wfpfiltertamperingfilterdeleted)
- [WiFiConnect](#wificonnect)
- [WiFiDisconnect](#wifidisconnect)
- [WindowsTimelineEntry](#windowstimelineentry)
- [WindowsTimelineEntryTimestamp](#windowstimelineentrytimestamp)
- [WlanInterfaceInfo](#wlaninterfaceinfo)
- [WmiCreateProcess](#wmicreateprocess)
- [WmiFilterConsumerBindingEtw](#wmifilterconsumerbindingetw)
- [WmiProviderRegistrationEtw](#wmiproviderregistrationetw)
- [WmiQuery](#wmiquery)
- [WmiQueryDetectInfo](#wmiquerydetectinfo)
- [WroteExeAndGeneratedServiceEvent](#wroteexeandgeneratedserviceevent)
- [WSLDistributionRegistered](#wsldistributionregistered)
- [WSLDistributionStarted](#wsldistributionstarted)
- [WSLDistributionStopping](#wsldistributionstopping)
- [WSLDistributionUnregistered](#wsldistributionunregistered)
- [WSLMetadata](#wslmetadata)
- [WSLVMStarted](#wslvmstarted)
- [WSLVMStopping](#wslvmstopping)
- [XarFileWritten](#xarfilewritten)
- [XProtectAction](#xprotectaction)
- [XumdHookEvent](#xumdhookevent)
- [XumdStatus](#xumdstatus)
- [XzFileWritten](#xzfilewritten)
- [Yz1FileWritten](#yz1filewritten)
- [ZerologonExploitAttempt](#zerologonexploitattempt)
- [ZipFileWritten](#zipfilewritten)
- [ZpaqFileWritten](#zpaqfilewritten)
- [ZstdFileWritten](#zstdfilewritten)

---

## Summary Table

| Header | Description | Platforms |
|--------|-------------|------------|
| AbnormalTerminationNotification |  | Kubernetes, Linux, Falcon Container, Vmcluster |
| AccessoryConnected | Sent when the device connects to an external accessory. This event will only be sent if the Connecte... | Android, iOS |
| AccessoryDisconnected | Sent when a device disconnects from an external accessory. This event will only be sent if the Conne... | Android, iOS |
| ActiveDirectoryAccountCreated | Indicates the creation of the subject account. | Windows |
| ActiveDirectoryAccountDepartmentUpdate | Indicates a change to the subject account's department. | Windows |
| ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate |  | Windows |
| ActiveDirectoryAccountDisabled | Indicates the subject account has been disabled. | Windows |
| ActiveDirectoryAccountEnabled | Indicates the subject account has been enabled. | Windows |
| ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate |  | Windows |
| ActiveDirectoryAccountLocked | Indicates the subject account has been locked. | Windows |
| ActiveDirectoryAccountNameUpdate | Indicates a change to the subject account's SAM account name. | Windows |
| ActiveDirectoryAccountOuUpdate | Indicates a change to the subject account's organizational unit. | Windows |
| ActiveDirectoryAccountPasswordUpdate | Indicates a change to the subject account's password. | Windows |
| ActiveDirectoryAccountUnlocked | Indicates the subject account has been unlocked. | Windows |
| ActiveDirectoryAuditGpoModified |  | Windows |
| ActiveDirectoryAuditGroupMemberModified |  | Windows |
| ActiveDirectoryAuditGroupModified |  | Windows |
| ActiveDirectoryAuditPasswordModificationAttempt |  | Windows |
| ActiveDirectoryAuditUserModified |  | Windows |
| ActiveDirectoryAuthentication | Indicates that the Domain Controller handled one or more successful authentications by an account on... | Windows |
| ActiveDirectoryAuthenticationFailure | Indicates that the Domain Controller handled one or more failed authentications by an account on an ... | Windows |
| ActiveDirectoryIncomingDceRpcEpmRequest | Indicates that the Domain Controller must handle one or more incoming DCE/RPC EPM (Endpoint Manager)... | Windows |
| ActiveDirectoryIncomingDceRpcRequest | Indicates that the Domain Controller must handle one or more incoming DCE/RPC requests from an accou... | Windows |
| ActiveDirectoryIncomingLdapSearchRequest | Indicates that the Domain Controller must handle one or more LDAP search requests from an account on... | Windows |
| ActiveDirectoryIncomingPsExecExecution2 | Indicates remote code execution on a domain controller using PsExec. This event is generated based o... | Windows |
| ActiveDirectoryInteractiveDomainLogon | Indicates an interactive logon to an Active Directry domain handled by a Domain Controller. The inte... | Windows |
| ActiveDirectoryServiceAccessRequest | Indicates that the Domain Controller handled one or more successful service requests from an account... | Windows |
| ActiveDirectoryServiceAccessRequestFailure | Indicates that the Domain Controller handled one or more failed service requests from an account on ... | Windows |
| AcUninstallConfirmation | This event is generated when a Falcon sensor is uninstalled from a host. Important: The Falcon senso... | Windows, Linux, macOS |
| AcUnloadConfirmation | The cloud will respond with this event as acknowledgement that a sensor was uninstalled. | Windows, Linux, macOS |
| AdditionalHostInfo | Serves as an addition to kernel-driven HostInfo event. Provides host-specific machine information fr... | Windows |
| ADExplorerFileWritten |  | Windows |
| AgentConnect | This event is generated when the sensor successfully connects to the cloud. Platforms: Windows Legac... | Windows, Linux, Falcon Container, iOS, Kubernetes, macOS, Android |
| AgenticSessionEnd |  | Windows |
| AgenticSessionStart |  | Windows |
| AgenticSubagentStart |  | Windows |
| AgenticToolRequest |  | Windows |
| AgenticUserPromptSubmit |  | Windows |
| AgentOnline | This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor ... | Windows, Linux, Falcon Container, macOS, ChromeOS, Android, Kubernetes |
| AiAgentClassifyChildTelemetry |  | Windows, macOS |
| AiAgentClassifyRootTelemetry |  | Windows, macOS |
| AksAgentPool | Snapshot of an Azure AKS Agent Pool. | Public Cloud |
| AksCluster | Snapshot of an Azure AKS cluster. | Public Cloud |
| AksVMSS | Snapshot of an Azure Virtual Machine Scale Sets. | Public Cloud |
| AllocVmEtw | A windows-only internal event that represents kernel initiated memory allocation. Captured using the... | Windows |
| AmcacheEntry | Metadata related to PE execution and program installation on Windows 7 and Server 2008 R2 and above. | Forensics |
| AmsBytePatternScanResult |  | Windows |
| AmsBytePatternScanTelemetry |  | Windows |
| AmsiRegistrationStatus | Event to record status in AMSI module. | Windows |
| AndroidEnterpriseInfo | This event contains metadata related to the state of the device as reported by the Android Managemen... | Android |
| AndroidInitServiceAdded | An event that indicates that a new init (boot) service has been added to the system configuration. T... | Android |
| AndroidInitServiceRemoved | An event that indicates that an init (boot) service has been removed from the system configuration. ... | Android |
| AndroidIntentSentIPC | This event is sent when an Android Intent is fired from the container | Android |
| AndroidManifestFragmentData | An event that's sent by the sensor along with AndroidManifestXmlUploaded that contains a logical por... | Android |
| AndroidManifestXmlUploaded | An event that indicates the LFO upload of the AndroidManifest of an android application package was ... | Android |
| AndroidModuleStateUpdate | Status information of modules for the Android sensor. AndroidModuleId lists available modules. | Android |
| APKMetadata | Sent from mobile sensor in PlayStore mode when a new APK file is present on the device, as a result ... | Android |
| AppleScriptFileWritten |  | macOS, Linux, Windows |
| AppProtocolDetected |  | macOS |
| AppSideLoaded | An event that contains the package name and installer info of the app that has been installed outsid... | Android |
| AppUninstalled | An event that contains information about an app that has been uninstalled from the device. | Android |
| ArcFileWritten | Emitted when a process is done writing a ARC file. | Linux, Windows, macOS |
| ArchiveFileContent |  | macOS, Windows |
| ArchiveInfo | Archive file information. | Forensics |
| ArchiveMemberInfo | Archive member file information. | Forensics |
| ArjFileWritten | Emitted when a process is done writing a ARJ file. | Windows, macOS, Linux |
| AsepFileChangeDetectInfo | Rollup indicating an ASEP file has been created or modified and there was a template detection on th... | macOS |
| AsepFileChangeScanInfo | Rollup indicating an ASEP file has been created or modified but there was no template detection on t... | macOS |
| AsepKeyUpdate | Generated when an Auto Start Execution Point registry key is updated. | Windows |
| AsepValueUpdate | This event is generated when a Microsoft Auto Start Execution Point registry key has been updated. | Windows |
| AsifFileWritten |  | macOS |
| ASLRBypassAttempt | Emitted when a process that applied ForceASLR to a module detects an invalid execution attempt. This... | Windows |
| AspmCollectionStatusUpdate |  | Linux |
| AssociateIndicator | This event is generated when the sensor generates an indicator. An indicator is like a detection eve... | Windows, Linux, Falcon Container, macOS |
| AssociateTreeIdWithRoot | This event is generated when there is a detection in the sensor. This event has a data field called ... | Windows, Windows Legacy, macOS, Linux, Falcon Container |
| AtJobInfo | Windows At jobs in use. | Forensics |
| AuditCveKmEtw | An event that indicates that a driver or the kernel reported a known CVE (Common Vulnerabilities and... | Windows |
| AuditCveUmEtw | An event that indicates that an application reported a known CVE (Common Vulnerabilities and Exposur... | Windows |
| AutoRunProcessInfo | Describes a process that is automatically executed. | Forensics |
| AwsEc2Image | This event provides key metadata regarding images (AMIs, AKIs, and ARIs) available in AWS. CrowdStri... | Windows, Public Cloud |
| AwsEc2Instance | This event provides key metadata regarding EC2 instances in AWS. CrowdStrike retrieves this informat... | Windows, Public Cloud |
| AwsEc2NetworkAcl | Platforms: Public Cloud | Windows |
| AwsEc2NetworkAclEntry | Information from AWS API call DescribeNetworkAcls. | Windows, Public Cloud |
| AwsEc2NetworkInterface | This event provides key metadata regarding network interfaces in AWS. CrowdStrike retrieves this inf... | Windows, Public Cloud |
| AwsEc2NetworkInterfacePrivateIP | This event provides key metadata regarding private IP addresses in AWS. CrowdStrike retrieves this i... | Windows, Public Cloud |
| AwsEc2SecurityGroup | This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this inform... | Windows, Public Cloud |
| AwsEc2SecurityGroupRule | This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this inform... | Windows, Public Cloud |
| AwsEc2Subnet | This event provides key metadata regarding subnets configured in AWS. CrowdStrike retrieves this inf... | Windows, Public Cloud |
| AwsEc2Volume | This event provides key metadata regarding EBS volumes configured in AWS. CrowdStrike retrieves this... | Windows, Public Cloud |
| AwsEc2Vpc | This event provides key metadata regarding virtual private clouds (VPCs) configured in AWS. CrowdStr... | Windows, Public Cloud |
| AwsIamAccountAlias | Information from AWS API call ListAccountAliases. | Windows, Public Cloud |
| AzureApplicationFirewallRule | An event that contains firewall rules for https traffic or Azure SQL traffic. | Public Cloud |
| AzureDisk | An event that contains a list of Azure disks and their attributes. | Public Cloud |
| AzureFirewall | An event that contains information about Azure cloud-based network security service. | Public Cloud |
| AzureFirewallRuleCollection | An event that contains Azure firewall rule collections for application, NAT (network address transla... | Public Cloud |
| AzureIpConfiguration | An event that contains a list of Azure IP configurations and attributes of the Azure IP configuratio... | Public Cloud |
| AzureNatFirewallRule | An event that contains Azure firewall rules for LAN. | Public Cloud |
| AzureNetworkFirewallRule | An event that contains Azure network filtering rules. | Public Cloud |
| AzureNetworkInterface | An event that contains a list of Azure network interfaces and the Azure network interface attributes... | Public Cloud |
| AzureNetworkSecurityGroup | An event that contains information about an Azure Network Security Group. | Public Cloud |
| AzureNetworkSecurityGroupRule | An event that contains Azure security rules in the specified network security group. | Public Cloud |
| AzurePrivateEndpoint | An event that connects Azure Network interface to other services with private links. | Public Cloud |
| AzurePublicIpAddress | An event that contains Azure public IP addresses. | Public Cloud |
| AzureResourceGroup | An event that contains a list of Azure Resource Groups. | Public Cloud |
| AzureSubnet | An event that contains Azure sub-networks in the virtual network. | Public Cloud |
| AzureSubscription | An event that contains a list of Azure subscriptions. | Public Cloud |
| AzureVirtualMachine | An event that contains a list of Azure virtual machines and the Azure virtual machine attributes. | Public Cloud |
| AzureVirtualMachineState | An event that contains the machine state for any Azure virtual machine. | Public Cloud |
| AzureVirtualNetwork | An event that contains a list of the Azure virtual networks and the Azure virtual network attributes... | Public Cloud |
| AzureVirtualNetworkPeering | An event that contains a list of the Azure virtual networks and the Azure virtual network attributes... | Public Cloud |
| BamRegAppRunTime | Recent program execution timeline from Background Activity Moderator (BAM) system service registry. ... | Forensics |
| Base64PeFileWritten |  | Windows |
| BcmFileWritten |  | Windows |
| BehaviorWhitelisted | Indicates that a behavior has been whitelisted. | Linux, macOS, Windows |
| BillingInfo | Sensor sends this event to inform the cloud about the sensor billing type. Platforms: macOS | Linux, Falcon Container, Windows |
| BITSJobCreated | The event is generated when a Background Intelligent Transfer Service (BITS) download is created and... | Windows |
| BITSJobFileInfo | Background Intelligent Transfer Service (BITS) job file information. | Forensics |
| BITSJobInfo | Background Intelligent Transfer Service (BITS) job information. | Forensics |
| BITSJobMetadata | Background Intelligent Transfer Service (BITS) job metadata: times, proxy. | Forensics |
| BlakHoleFileWritten |  | Windows |
| BlfFileWritten | Emitted when a process is done writing an BLF file. | Windows, macOS, Linux |
| BlockThreadFailed | A block thread request failed. | Windows |
| BMLFeatureData |  | Linux, Falcon Container, Windows, macOS |
| BmpFileWritten | Emitted when a process is done writing a BMP image file. | macOS, Linux, Windows |
| BootLoaderStatus | An event that contains info about the device's bootloader. | Android |
| BootLoopProtectionTelemetry |  | Windows |
| BPFCommandIssued | Emitted when a process executes bpf syscall. | Linux, Falcon Container |
| BrotliFileWritten |  | Windows |
| BrowserAccountInfo | Browser user account information. | Forensics |
| BrowserCookieInfo | Browser tracking cookie information. | Forensics |
| BrowserDownloadEnded | Browser downloaded file information signifying download end time. | Forensics |
| BrowserDownloadStarted | Browser downloaded file information signifying download start time. | Forensics |
| BrowserExtensionInfo | Browser extension/addon information. | Forensics |
| BrowserExtensionStatus |  | macOS |
| BrowserHistoryClearInfo | Browser history clearing event information. | Forensics |
| BrowserHistoryVisit | Browser history hit information. | Forensics |
| BrowserInjectedThread | Indicates a browser process injected a thread into some other process. | Windows |
| BrowserProxyInfo | Browser proxy information. | Forensics |
| BZip2FileWritten | Emitted when a process is done writing a BZip2 file. | macOS, Windows, Linux |
| CabFileWritten | Emitted when a process is done writing a Microsoft Cabinet (CAB) file. | Windows, Linux, macOS |
| CertificatePinningCompromised | An event that indicates that the certificate pinning methods/functions on the device have been tampe... | iOS |
| ChannelActive |  | Windows |
| ChannelDataDownloadComplete | Sent by LFODownloadActor when a new channel data file has been downloaded. Platforms: iOS, Kubernete... | Windows, Linux, Falcon Container, Android, macOS |
| ChannelVersionRequired | This event informs the cloud information about the state of a channel on the sensor. The cloud will ... | Windows, macOS, Linux, Falcon Container, Android |
| CidMigrationComplete |  | Windows, macOS, Linux |
| CidMigrationConfirmation |  | Linux, Windows, macOS |
| CidMigrationError |  | Linux, Windows, macOS |
| CidMigrationManifestDownloadComplete |  | Linux, macOS, Windows |
| ClassifiedModuleLoad | The ClassifiedModuleLoad event provides information about a module which has been loaded into a proc... | Windows |
| ClassifiedProcessStart |  | Windows |
| ClassifiedSensitiveFileAccess |  | Windows |
| ClipboardCopy | Sent when content is copied to the clipboard. | Android, iOS |
| ClipboardPaste | Sent when content is pasted from the clipboard. | Android |
| CloudAssociateTreeIdWithRoot | This event is generated when there is a detection in the CrowdStrike cloud. This event has a data fi... | Windows, Linux, Falcon Container, macOS, ChromeOS |
| CloudScanControl | A event to that notifies downstream services of completed tasks. | Public Cloud |
| CodeSigningAltered | An event that indicates the code signing flags of the current application have unexpected flags or a... | iOS |
| CommandHistory | This event includes the full command history associated with one of the consoles in a process that h... | Windows |
| CommsLogReset | Sent by Communications indicating that the CommsLog was flushed due to invalid data | macOS |
| ConfigDownloadComplete | Sent by LFODownloadActor when a new binary configuration has been downloaded as part of a configurat... | Windows, Linux, Falcon Container, macOS |
| ConfigStateUpdate | Sent periodically and when dynamic config is updated. Analysts can find out which config was active ... | macOS, Linux, Falcon Container, Windows |
| ConfigurationLoaded | Thrown when a new configuration has been successfully loaded but before any Event Sources are starte... | iOS, Android |
| ConfigurationProfileModified |  | macOS |
| ConfigurationProvisioningState |  | Linux |
| ContainerizationUpdate | Sent following an LFODownload of a new APK to be installed or updated in the container, containing r... | Android |
| CrashNotification | The sensor sends this to the cloud when the Diagnostics Actor notices that the machine has booted wi... | Windows, macOS |
| CreateProcessArgs | Full command line argument corresponding to a process creation. | macOS |
| CreateService | Generated when a Windows service is created. | Windows |
| CreateSocket | This event is created whenever a process creates a socket. | Forensics, Linux, Falcon Container |
| CreateThreadKernelNoStartImage | Emitted when a new system thread is created outside of a loaded driver. | Windows |
| CreateThreadNoStartImage | This event is used to indicate the target start address of a CreateThread attempt is not within the ... | Windows |
| CreateThreadReflectiveDll | This event is used to indicate the presence of a reflectively loaded dll in the callstack for a Crea... | Windows |
| CriticalEnvironmentVariableChanged | A process set a critical environment variable. | Linux, Falcon Container |
| CriticalFileAccessed | A critical file was accessed. Platforms: ChromeOS | Linux, Falcon Container, macOS |
| CriticalFileModified | A critical file was modified. Platforms: ChromeOS | Linux, Falcon Container, macOS |
| CrxFileWritten |  | macOS, Windows, Linux |
| CSAResultsGenericDetectInfo |  | Windows |
| CsKmCrashSummaryEvent |  | Windows |
| CsUmProcessCrashAuxiliaryEvent | An event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field... | Windows |
| CsUmProcessCrashSummaryEvent | A event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field. | Windows |
| CurrentSystemTags | This event is sent from the sensor to inform the cloud about the system tag state. Platforms: Vmclus... | macOS, Linux, Falcon Container, iOS, Android, Windows, Kubernetes |
| CustomIOABasicProcessDetectionInfoEvent | An event triggered by a Process Creation custom IOA rule. | Linux, Falcon Container, Windows, macOS |
| CustomIOADomainNameDetectionInfoEvent | Platforms: Windows An event triggered by a Domain Name custom IOA rule. | Linux, macOS |
| CustomIOAFileWrittenDetectionInfoEvent | An event triggered by a File Creation custom IOA rule. | Windows, macOS, Linux |
| CustomIOANetworkConnectionDetectionInfoEvent | An event triggered by a Network Connection custom IOA rule. Platforms: Linux | macOS, Windows |
| DataEgress | Description of a data egress observed on the sensor. | macOS, Windows |
| DataProtectionArchiveAssessed | Describes an archive processed by Data Protection assessment. Top level event fields are properties ... | Windows, macOS |
| DataProtectionBrowserConnect |  | Windows, macOS |
| DataProtectionDataEncryption |  | Windows |
| DataProtectionPACDiagnostic |  | Windows |
| DBusMessage | An event that generates telemetry that provides visibility into D-Bus messages flowing over local Un... | Linux |
| DcBluetoothAuthorizationStatus |  | macOS |
| DcBluetoothDeviceBlocked |  | macOS |
| DcBluetoothDeviceConnected | This event represents a connected Bluetooth device. Platforms: macOS | Windows |
| DcBluetoothDeviceConnectedDetails |  | macOS, Windows |
| DcBluetoothDeviceDisconnected | Platforms: Windows This event represents a disconnected Bluetooth device. | macOS |
| DcBluetoothDevicePolicyViolation |  | macOS |
| DcBluetoothDeviceProperties | This event contains properties for a connected Bluetooth device. Platforms: macOS | Windows |
| DcIdentification | This event enables monitoring of domain controllers (DCs) and the passing of identifying information... | Windows |
| DcOffline | An event that indicates the Device Control plug-and-play driver interface has gone offline. It is se... | Windows, macOS, Linux |
| DcOnline | An event that indicates the Device Control plug-and-play driver interface has come online. It is sen... | macOS, Linux, Windows |
| DcRemovableStorageDeviceBlocked |  | Windows, macOS |
| DcRemovableStorageDeviceConnected |  | Windows, macOS |
| DcRemovableStorageDeviceDisconnected |  | macOS, Windows |
| DcRemovableStorageDevicePolicyViolation |  | Windows, macOS |
| DcStatus | An event that contains the status information for the Device Control plug-and-play driver. It is sen... | Windows, macOS, Linux |
| DCSyncAttempted | Directory Services changes were replicated. If the source host is not a Domain Controller, this coul... | Windows |
| DcUsbConfigurationDescriptor | An event that describes a configuration descriptor extracted from the firmware of a USB device. This... | macOS, Linux, Windows |
| DcUsbDeviceBlocked | An event that indicates a USB device that was blocked by a policy. | Linux, macOS, Windows |
| DcUsbDeviceConnected | An event that describes a connected USB device to which Device Control is attached. It is sent each ... | Linux, macOS, Windows |
| DcUsbDeviceDisconnected | An event that describes a disconnected USB device to which Device Control has previously attached. I... | Linux, macOS, Windows |
| DcUsbDevicePolicyViolation | An event that indicates a USB device that matched a rule in a policy but was not blocked due to the ... | macOS, Linux, Windows |
| DcUsbDeviceWhitelisted | An event that indicates a USB device was added to an allowlist by a Device Control policy. The Devic... | Windows, macOS, Linux |
| DcUsbEndpointDescriptor | An event that describes an endpoint descriptor extracted from the firmware of a USB device. An inter... | macOS, Linux, Windows |
| DcUsbHIDDescriptor | This event describes a HID (Human Interface Device) descriptor extracted from the firmware of a USB ... | macOS, Linux, Windows |
| DcUsbInterfaceDescriptor | An event that describes an interface descriptor extracted from the firmware of a USB device. There a... | macOS, Linux, Windows |
| DeactivateMobileSensorResponse | Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. Platforms: Android Se... | iOS |
| DebFileWritten |  | Linux, macOS, Windows |
| DebuggableFlagTurnedOn | An event that indicates a debuggable flag has been turned on for a non-dev build of an app. | Android |
| DebuggedState | An event that indicates a process is in the state of being debugged (i.e., has a debugger attached t... | iOS |
| DeliverLocalFXToCloud | DeliverLocalFXToCloud conveys feature extraction (FX) data to the cloud from the sensor. Platforms: ... | macOS, Windows |
| DeliverRulesEngineResultsToCloud |  | macOS, Linux, Windows |
| DetectionExcluded | This event indicates that a detection has been excluded, either by customer exclusions or by CrowdSt... | macOS, Linux, Falcon Container, Windows, iOS, Android |
| DeveloperOptionsStatus | An event that contains info about developer-related settings on the device. Platforms: iOS | Android |
| DexFileWritten | Emitted when a file has been written that contains a real Dex image header. | Android |
| DirectoryCreate | This event is generated when a process creates a new folder. Platforms: Linux | Windows, macOS |
| DirectoryTraversalOverSMB | This event indicates Directory traversal over an SMB session detected. | Windows |
| DiskCapacity | An event that contains information about disks, the quantity of disks, and the storage capability of... | Linux |
| DiskUtilization | An event that contains the used and available storage space for each mounted logical drive or volume... | Linux |
| DllInjection | This event indicates that DLL injection occurred in the target process. | Windows |
| DmgFileWritten |  | Linux, Windows, macOS |
| DmpFileWritten | Emitted when a process is done writing a dump file. PidFromCommandLine will be enhanced in some case... | Windows, Linux, macOS |
| DnsCache | An entry observed within the system's DNS Cache. | Forensics |
| DnsRequest | When a process on a host generates a DNS query, the sensor waits for the response, to generate a Dns... | Android |
| DnsRequestBlocked | This event is sent whenever a DnsRequest is blocked. Connection to either the IP or the domain in th... | Android, iOS |
| DNSRequestDetectInfo | This event is sent whenever a malicious DnsRequest is detected. Platforms: Linux | iOS, Android |
| DnsRequestResult | An event that contains DNS request results after a DNS request. | Android, iOS |
| DnsServer | DNS server IP addresses. | Forensics |
| DnsServerSigRedExploitAttemptEtw |  | Windows |
| DocumentProgramInjectedThread | Indicates a document program process injected a thread into some other process. | Windows |
| DotnetModuleLoadDetectInfo |  | Windows |
| DriverLoad | An event to notify of a driver load that will be used for detection. | Forensics, Windows |
| DriverLoadBlocked | Event which indicates we successfully blocked a driver from loading. | Windows |
| DriverLoadedV2DetectInfo |  | Windows |
| DriverPreventFailed | Event which indicates we failed (or timed out) attempting to block a driver load. | Windows |
| DriverPreventionStatus |  | Windows |
| DuplicateInstallFromPlayStore | An event that indicates a containerized app is also installed outside the container. | Android |
| DwgFileWritten | An event that is emitted when a process is done writing to a DWG file. | Windows |
| DwmCompositionResourceExploitAttempt |  | Windows |
| DxfFileWritten |  | Windows |
| EarlyExploitPivotDetect | Telemetry event indicating execution pivoting in an unusual way. Could be indicative of malicious co... | Windows |
| ECBDownloadComplete | Sent by LFODownloadActor when a new ECB module has been downloaded as part of a configuration update... | Windows, Linux, macOS |
| EddScanStart | Sent by sensor to indicate the start of a new EDD scan run. Note: This event is currently not suppor... | macOS |
| EddScanStatus | Sent by sensor periodically to report the status of an on-going scan. Platforms: macOS Sent by senso... | Windows |
| EksCluster | Snapshot of an AWS EKS cluster. | Public Cloud |
| EksFargateProfile | Snapshot of an AWS EKS Fargate profile. | Public Cloud |
| EksNodeGroup | Snapshot of an AWS EKS node group. | Public Cloud |
| ELFFileWritten | Emitted when a file has been written that contains a real ELF image header. | Android, macOS, Linux, Windows |
| EmailArchiveFileWritten |  | macOS |
| EmailFileWritten |  | Linux, Windows, macOS |
| EndOfProcess | When a process that’s running on a host finishes, the sensor will count all of the events that were ... | Linux, Falcon Container, macOS, Windows |
| EntropyScan | File contents entropy, useful for identifying potentially malicious files. | Forensics |
| ErrorEvent | Event indicating a sensor error. Platforms: Kubernetes Platforms: Vmcluster | Windows, Linux, Falcon Container, macOS |
| EseFileWritten |  | Linux, Windows, macOS |
| EtwComponentResponse | Event sent in when EtwComponent has initialized. AttemptNumber is no longer used. | Windows |
| EtwErrorEvent | An event that indicates that an error occurred which associated is with the ETW consumer. | Windows |
| EventLogCleared | This event is generated when a Windows event log is cleared. | Windows |
| EventTapInfo | Describes a macOS Event Tap. Event Taps allow for capturing of keyboard and mouse HID events. | Forensics |
| ExcelDocumentOpened |  | Windows |
| ExecutableDeleted | This event indicates that an executable was deleted from the host. Platforms: Linux | Windows, macOS |
| ExtendedExploitMitigationViolatedDetectInfo |  | Windows |
| FalconHostFileTamperingInfo | An event that describes the file event that triggered a Falcon sensor tampering indicator. | Windows |
| FalconHostRegTamperingInfo | An event that describes the registry event that triggered a Falcon sensor tampering indicator. | Windows |
| FalconProcessHandleOpDetectInfo |  | Windows |
| FalconServiceStatus | A message from CsFalconService regarding the service and its servlets' lifecycle events. | Windows |
| FfcBytePatternScanResult | Describes a scanning result performed by the Falcon Forensics Collector. | Forensics |
| FileAccessOperationOverSMB | File access operations over a SMB user session. | Windows |
| FileContentsChanged |  | Linux |
| FileCreateInfo | This event is generated when a file is created by a process. | Windows, macOS, Linux, Falcon Container |
| FileDeleted | This event has been deprecated as of Falcon Sensor for Windows 4.16.7903, and Falcon Sensor for Mac ... | Windows |
| FileDeleteInfo | This event is generated when a file deletion for a full file occurs. ADS deletions are not currently... | Windows, macOS, Linux |
| FileDescriptorMonitor |  | Forensics |
| FileDetectInfo |  | Linux, Windows, macOS |
| FileEntry | Some portion of a text file, either a single line or matched regular expression. | Forensics |
| FileExtendedAttrOperation |  | macOS |
| FileHashesEvent |  | Forensics |
| FileInfo | Error event for FileInfo response. Platforms: macOS FileInfo response with information about a file. | Forensics |
| FileIntegrityMonitorRuleMatched | An event that contains data about a change to a directory, file, or registry key. Used with the File... | Windows, Linux |
| FileOfInterestBasicInfo |  | Linux, Windows, macOS |
| FileOpenInfo | This event is generated when a file is opened by a process. | Windows, macOS, Linux, Falcon Container |
| FileRenameInfo | This event is generated when a file is renamed. Only sent as part of a detection. | Windows, macOS, Linux, Falcon Container |
| FileSetMode | Indicates the file permissions have been modified via chmod/fchmod/fchmodat. | Linux, Falcon Container |
| FileSignatureMismatch | On-demand scan for files with name extensions and header magic values. | Forensics |
| FileSignatureStatistics | On-demand scan for files with name extensions and header magic values. | Forensics |
| FilesStatisticInfo | Files statistic information. | Forensics |
| FileStatFsInfo |  | Linux |
| FileSystemAttributesStatus | An event that contains info about the Filesystem attributes of the device. | iOS |
| FileSystemContainmentStatus |  | Windows |
| FileSystemOperationBlocked | An event that indicates that a file system operation has been blocked. Platforms: macOS | Windows |
| FileSystemOperationDetectInfo | Informational event for a file system operation detection. | Windows |
| FileTimestampMetadata | FileTime event is emitted per timestamp for a given file. This helps analysts build a timeline of fi... | Forensics |
| FileTimestampsModified | An event that is emitted when a change occurs to the timestamps of a file. | Windows |
| FileVaultStatus | Contains information regarding the system FileVault (encrypted) state. | macOS |
| FileWrittenAndExecutedInContainer | A file was written and later executed in a container. | Linux, Falcon Container |
| FileWrittenWithEntropyHigh |  | Windows, Linux |
| FirewallChangeOption | A firewall configuration option has been changed, such as enabling or disabling the firewall. The da... | Windows |
| FirewallDeleteRule | A firewall rule has been deleted, such as removing a rule preventing inbound RDP connections. The da... | Windows |
| FirewallDeleteRuleIP4 | An event that notifies that an Ipv4 firewall rule has been deleted. The field 'IsUnique' will be TRU... | macOS |
| FirewallDeleteRuleIP6 | An event that notifies that an Ipv6 firewall rule has been deleted. The field 'IsUnique' will be TRU... | macOS |
| FirewallDisabled | An event that is sent from the sensor when packet filter is disabled. | macOS |
| FirewallEnabled | An event that is sent from the sensor when packet filter is enabled. | macOS |
| FirewallRuleApplicationFailed | An event that indicates that the application of a firewall rule has failed. Platforms: macOS An even... | Windows |
| FirewallRuleInfo |  | Forensics |
| FirewallRuleIP4 |  | Forensics |
| FirewallRuleIP4Matched | An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations ... | Windows |
| FirewallRuleIP6 |  | Forensics |
| FirewallRuleIP6Matched | An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations ... | macOS |
| FirewallSetRule | A firewall rule has been created or modified, such as a rule allowing inbound RDP connections. The d... | Windows |
| FirewallSetRuleIP4 | An event that indicates an IPv4 firewall rule has been created. The field 'IsUnique' will be TRUE if... | macOS |
| FirewallSetRuleIP6 | An event that indicates an IPv6 firewall rule has been created. The field 'IsUnique' will be TRUE if... | macOS |
| FirmwareAnalysisErrorEvent | Indicates an occurrence of error associated with the Firmware Analysis feature. | macOS, Windows |
| FirmwareAnalysisHardwareData | This event contains hardware data collected by Firmware Analysis. | macOS, Windows |
| FirmwareAnalysisStatus | This event contains status of the FPnP filter driver. | macOS, Windows |
| FirmwareImageAnalyzed | Indicates that analysis of a firmware image was completed. | macOS, Windows |
| FirmwareRegionMeasured | Indicates that a certain region of a firmware image was measured. Platforms: Windows | macOS |
| FlashThreadCreateProcess | Thread associated with Flash activity created a process. | macOS, Windows |
| ForensicsCollectorLog | A log entry emitted by the Falcon Forensics Collector process. | Forensics |
| ForensicsCollectorOffline | Final event of a Forensics collection. | Forensics |
| ForensicsCollectorOnline | Marks the beginning of a Forensics collection. | Forensics |
| FreeArcFileWritten |  | Windows |
| FsPostCreate | This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing... | Windows |
| FsPostOpen | This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing... | Windows |
| FsPostOpenSnapshotFile | Information about a file opened on a snapshot volume. | Windows |
| FsPostOpenUpImpersonating | A reified FsPostOpen event that occurred in the context of a thread up-impersonating another user, a... | Windows |
| FsVolumeMounted | Provides information about a mounted volume. Platforms: Forensics | Windows, macOS, iOS, Linux, Falcon Container |
| FsVolumeReadInfo |  | Windows |
| FsVolumeUnmounted | Provides information about an unmounted volume. | Windows, macOS, iOS, Linux, Falcon Container |
| FtpCommand |  | Linux |
| GcpAsset | An event that contains GCP (Google Cloud Platform) Organization Metadata. | Public Cloud |
| GcpComputeDisk | An event that contains GCP (Google Cloud Platform) Compute Disk Configuration details. | Public Cloud |
| GcpComputeFirewall | An event that contains GCP (Google Cloud Platform) Compute Image configuration details. | Public Cloud |
| GcpComputeImage | An event that contains GCP (Google Cloud Platform) Compute Image configuration details. | Public Cloud |
| GcpComputeInstance | An event that contains GCP (Google Cloud Platform) Compute Instance configuration information. | Public Cloud |
| GcpComputeNetwork | An event that contains GCP (Google Cloud Platform) Compute Network configuration information. | Public Cloud |
| GcpComputeNetworkInterface | An event that contains GCP (Google Cloud Platform) Compute Network Interface configuration informati... | Public Cloud |
| GcpComputeNetworkPeering | An event that contains GCP (Google Cloud Platform) Compute Network Peering configuration details. | Public Cloud |
| GcpComputeSubnetwork | An event that contains GCP (Google Cloud Platform) Compute Subnetwork configuration details. | Public Cloud |
| GcpIamServiceAccount | An event that contains GCP (Google Cloud Platform) IAM Service Account configuration details. | Public Cloud |
| GcpProject | An event that contains GCP (Google Cloud Platform) Project metadata. | Public Cloud |
| GenericFileWritten | An event that is emitted when a process is done writing to a file that doesn't match a more specific... | Windows |
| GetAsyncKeyStateEtwBatch | An event that indicates that an application called the GetAsyncKeyState API multiple times. | Windows |
| GifFileWritten | Emitted when a process is done writing a GIF image file. | Linux, Windows, macOS |
| GroupAccount | Describes an observed group account. | Forensics |
| GroupIdentity | Provides the sensor boot unique mapping between GID, AuthenticationId, UserPrincipal, and UserSid. P... | macOS |
| GzipFileWritten | Emitted when a file has been written that contains a real Gzip image header. | Linux, Windows, macOS |
| HarmfulAppData | An event that contains the name, hash, and category of the harmful app. | Android |
| HeapSprayAttempt | Emitted when a process that had HeapSpray protections applied detects an invalid execution attempt. | Windows |
| HookedAndroidMethodFound | An event that indicates that a hooking framework such as Xposed has been found to have been loaded b... | Android |
| HookedDriverObject | This event describes the presence of a hooked pointer in a DRIVER_OBJECT structure. | Windows |
| HostedServiceStarted | This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is star... | Windows |
| HostedServiceStatusInfo | Status information includes loaded DLL for a hosted service. | Forensics |
| HostedServiceStopped | This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is stop... | Windows |
| HostInfo | This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a ... | Windows |
| HostnameChanged | Sent by the hostname awareness actor to communicate change in hostname. Platforms: macOS | Linux, Falcon Container |
| HostTimeModified |  | Linux, Falcon Container |
| HttpRequest |  | macOS, Linux |
| HttpRequestDetect | An event that indicates a detection on an HTTP(S) request. | Windows |
| HttpRequestV2Detect |  | Windows |
| HttpResponse |  | Linux, macOS |
| HttpVisibilityStatus | An event that indicates that the status of the HTTP Visibility event source has been updated. | Windows |
| IBEBChannelFileEnforcementResponse | An event that sent installed browser extension blocking (IBEB) channel file policy enforcement respo... | macOS, Windows |
| IdpCloudHealthCheck |  | Windows |
| IdpCloudHealthConfigurationsGetResponse |  | Windows |
| IdpCloudHealthConfigurationsSetResponse |  | Windows |
| IdpCloudHealthStatus |  | Windows |
| IdpConnectionsOverloadNotification | IDP Traffic Inspection detected more than 15,000 concurrent connections in active enforcement mode. | Windows |
| IdpContainerRestarted |  | Windows |
| IdpDcPerfReport | This event reports Domain Controller performance counter. | Windows |
| IdpDcTiConfiguration |  | Windows |
| IdpEntityRiskScoreChange |  | Public Cloud |
| IdpIdaasCorrelate |  | Windows, macOS |
| IdpPacketDiversionConnectionsOverloadNotification |  | Windows |
| IdpPacketDiversionLdapsConnectionsOverloadNotification |  | Windows |
| IdpPolicyAccessRuleMatch |  | Windows |
| IdpPolicyAccountEventRuleMatch |  | Public Cloud |
| IdpPolicyAlertRuleMatch |  | Public Cloud |
| IdpPolicyCloudAccessRuleMatch |  | Public Cloud |
| IdpPolicyFederatedAccessRuleMatch |  | Public Cloud |
| IdpTelemetryData |  | Windows |
| IdpWatchdogConfigurationsGetResponse |  | Windows |
| IdpWatchdogConfigurationsSetResponse |  | Windows |
| IdpWatchdogReEnabled |  | Windows |
| IdpWatchdogRemediationActionRequest |  | Windows |
| IdpWatchdogRemediationActionTaken |  | Windows |
| IdpWatchdogRemediationActionTakenForCpu |  | Windows |
| IdpWatchdogRemediationActionTakenForMemory |  | Windows |
| IdwFileWritten | Emitted when a process is done writing an IDW file. | Windows |
| ImageHash | This event is generated for each DLL or executable loaded into a process’ memory. | Windows, Linux, Falcon Container, macOS |
| ImapCommand |  | Linux, Windows |
| ImgExtensionFileWritten |  | Windows |
| ImpersonationTokenInfo | ImpersonationTokenInfo represents a security context for a general impersonation activity. Each Impe... | Windows |
| InboundHttpHeader |  | Windows, Linux, macOS |
| InboundHttpParsingStatus |  | macOS, Windows, Linux |
| InjectedThread | This event is generated when one process injects an execution thread into another process. While oft... | Windows |
| InjectedThreadFromUnsignedModule | This event contains information about a thread that was injected into a process from an unsigned mod... | Windows |
| InstallBundleDownloadComplete | An install bundle download has completed. | Windows |
| InstalledApplication | An event that describes a single application. E.g. representing a newly installed application, one j... | Windows |
| InstalledBrowserExtension | An event that contains information about installed browser extensions, including updates and removal... | Windows, macOS |
| InstalledUpdates | An event that describes the updates installed on the system. The Status field will indicate if some ... | Windows |
| InstallFromUnknownSourcesStatus | An event that contains info about third-party app installers on Android. | Android |
| InstallServiceDownloadComplete | An install service download has completed. | Windows |
| InstanceMetadata | Metadata information about the instance on which the sensor is running. Platforms: Kubernetes, macOS | Windows, Linux, Falcon Container |
| InternetExposureData |  | Windows, Linux, macOS |
| IntrusivePackageDiscovered |  | Android |
| IntrusiveProcessDiscovered |  | iOS |
| IntrusivePropertyDiscovered |  | Android |
| IOServiceRegister | This event describes an IOService being registered with a notification handler. | macOS |
| IoSessionConnected | An event that is emitted when an IO session has been connected. | Windows |
| IoSessionLoggedOn | An event that is emitted when an IO session has been logged off. | Windows |
| IPCDetectInfo |  | Windows |
| IsoExtensionFileWritten |  | Windows |
| JarFileWritten | This event is generated when a Java executable archive (.jar) file type is written to disk. | Windows, macOS, Linux, Android |
| JavaClassFileWritten | Emitted when a process is done writing a Java Class file. | Windows, macOS, Linux |
| JavaInjectedThread | This event is generated when Java injects a thread into another process. | Windows |
| JpegFileWritten | Emitted when a process is done writing a Jpeg image file. | macOS, Linux, Windows |
| JumpListInfo |  | Forensics |
| K8SAdmissionReviewResult |  | Kubernetes |
| K8SAdmissionReviewResultPrime |  | Public Cloud |
| K8SCluster | Snapshot of Kubernetes cluster for mapping Kubernetes cluster id and name. | Public Cloud |
| K8SClusterInfo |  | Kubernetes |
| K8SDaemonSet | Snapshot of a Daemon Set object in Kubernetes. | Public Cloud |
| K8SDeployment | Snapshot of a deployment object in Kubernetes. | Public Cloud |
| K8SEphemeralContainer | Snapshot of an ephemeral Container belonging to a Pod. | Public Cloud |
| K8SInitContainer | Snapshot of status for an Initialization(Init) Container inside a Pod. | Public Cloud |
| K8SInitContainerStatus | Snapshot of an Initialization(Init) Container belonging to a Pod | Public Cloud |
| K8SNode | Snapshot of a Node object in Kubernetes. | Public Cloud |
| K8SPod | Snapshot of a Pod object in Kubernetes. | Public Cloud |
| K8SProductConfig |  | Kubernetes |
| K8SReplicaSet | Snapshot of a Replica Set object in Kubernetes. | Public Cloud |
| K8SResource |  | Kubernetes |
| K8SRunningContainer | Snapshot of a running Container belonging to a Pod. | Public Cloud |
| K8SRunningContainerStatus | Snapshot of status for a running Container inside a Pod. | Public Cloud |
| K8SService | Snapshot of a Service object in Kubernetes. | Public Cloud |
| K8SSnapshot |  | Kubernetes |
| K8SWatchStarted |  | Kubernetes |
| K8SWatchStopped |  | Kubernetes |
| KernelCallbackTablePatch | An event that indicates that the KernelCallbackTable has been altered at the specified index. If pre... | Windows |
| KernelCallbackTableUpdate | An event that indicates that the ProcessEnvironmentBlock KernelCallbackTable field has been changed ... | Windows |
| KernelExtension | Describes a macOS kernel extension identified by the collector. | Forensics |
| KernelModeExecImage | Indicates a kernel Image has been loaded into memory. | Linux, Falcon Container |
| KernelModeLoadImage | Indicates a kernel-mode module has been loaded into memory. | Windows, Forensics, Linux, Falcon Container, macOS |
| KernelParameter |  | Forensics |
| KernelServiceStarted | Indicated that a kernel service was started locally or remotely. | Windows |
| KextLoad | Signals a Kernel Extension (KEXT) Load, triggered via a MAC hook. | macOS |
| KextUnload | Signals a Kernel Extension (KEXT) Unload, triggered via a MAC hook. | macOS |
| KillProcessError | If KillProcessActor fails to kill a process due to process being marked as system critical or for an... | Windows, macOS, Linux, Falcon Container |
| LFODownloadComplete |  | Android, Vmcluster, Windows, iOS, Kubernetes, macOS, Linux, Falcon Container |
| LFODownloadConfirmation | Thrown when the agent receives an LFODownload event. Platforms: iOS Platforms: Vmcluster, Kubernetes | Windows, Linux, Falcon Container, macOS, Android |
| LfoUploadDataComplete | Platforms: macOS, Android, Windows, Linux Emitted when the LFOUploadActor has successfully uploaded ... | Vmcluster, Kubernetes |
| LfoUploadDataFailed | Emitted when the sensor has detected error(s) and has decided not to stop uploading a file to the cl... | macOS, Android, Linux, Windows |
| LfoUploadDataUnneeded | Emitted when the sensor initiates a file upload, but the cloud has determined the file is not needed... | Windows, Linux, macOS, Android |
| LfoUploadStart | Emitted when the sensor initiates a file upload. Platforms: Vmcluster, Kubernetes | macOS, Windows, Android, Linux |
| LhaFileWritten |  | Windows |
| LightningUnresponsiveStatus |  | Windows, macOS |
| LinkFileInfo | Link file information. | Forensics |
| LnkFileWritten |  | Windows, Linux, macOS |
| LoadImage | Indicates a module has been loaded into memory. | Windows, macOS, Linux, Falcon Container |
| LocalGroupIdentity | Group identity information includes user group name, GID, and names, UIDs and sid of user members. | Forensics |
| LocalIpAddressIP4 | This event is generated when a host uses a new IPv4 network address. Platforms: Forensics | macOS, iOS, Linux, Falcon Container, Windows, Android |
| LocalIpAddressIP6 | This event is generated when a host uses a new IPv6 network address. Platforms: Forensics | macOS, Linux, Falcon Container, iOS, Windows, Android |
| LocalIpAddressRemovedIP4 | This event is generated when a host loses its IPv4 network address. | Linux, Falcon Container, iOS, Windows, Android, macOS |
| LocalIpAddressRemovedIP6 | This event is generated when a host loses its IPv6 network address. | macOS, iOS, Android, Linux, Falcon Container, Windows |
| LocalWindowsUserUpdate |  | Windows |
| LockdownModeStatus |  | iOS |
| LockScreenStatus | An event that contains info about the device lock screen mechanism. | Android, iOS |
| LogCollectorDeploymentStatus |  | macOS, Linux, Windows |
| LogEntry | A log entry observed on an endpoint. | Forensics |
| LoginItemAdded |  | macOS |
| LogonBehaviorCompositionDetectInfo |  | Windows |
| LowILModuleLoadAttempt | An event that indicates that a non-LowIL process attempted to load an untrusted LowIL module. | Windows |
| LRZipFileWritten |  | Windows, macOS, Linux |
| LsassHandleFromUnsignedModule | This event contains information about a handle that was created to LSASS from an unsigned module. | Windows |
| LSQuarantineEvent |  | Forensics |
| LZ4FileWritten |  | Linux, macOS, Windows |
| LzfseFileWritten |  | Linux, macOS, Windows |
| LZipFileWritten |  | Linux, Windows, macOS |
| LzmaFileWritten |  | Windows, macOS, Linux |
| LZOFileWritten |  | Windows, macOS, Linux |
| MacFsEventRecord | Mac fsevents record, forensically interesting filesystem logging/information. | Forensics |
| MachOFileWritten | Emitted when a process is done writing a MachO file. | macOS, Linux, Windows |
| MachOHeaderParsed | A MachO file was read into memory from disk and its header was parsed. | macOS |
| MacKnowledgeActivityEnd | An entry from a knowledgeC database indicating the end of some user activity on a MacOs system. | Forensics |
| MacKnowledgeActivityStart | An entry from a knowledgeC database indicating the start of some user activity on a MacOs system. | Forensics |
| MacMRU | A digital forensics record derived from Apple SharedFileList (.sfl/.sfl2) files. This event helps id... | Forensics |
| MacroContentInfo | Description: Provides information about a macro extracted when an Office file is written or opened C... | Windows |
| MacroDetectInfo | Event description: Provides more context around the macro content that was detected. ContextProcessI... | Windows |
| MalPaths | Malicious DLL or executable image name conflicts found in different or unexpected folders. | Forensics |
| ManifestDownloadComplete | Sent by LFODownloadActor when a new configuration manifest has been downloaded. Platforms: Kubernete... | Windows, Linux, Falcon Container, macOS |
| MbrOverwriteRawDetectInfo |  | Windows |
| MemoryAdvise |  | Linux |
| MemoryLocked |  | Linux |
| MemoryMapped | Triggers when an executable memory region is mapped. | Linux, Falcon Container |
| MemoryProtectionChanged |  | Linux |
| MemoryProtectionUpdated | Triggers if a new executable memory region is mapped which is writable or mapped from a file. | Linux, Falcon Container |
| MemoryScanEnabled |  | Windows |
| MemoryScanErrorEvent |  | Windows |
| MftBootSector | Windows Master File Table (MFT) Boot sector. | Forensics |
| MftRecord | Windows Master File Table (MFT) record. | Forensics |
| MobileAppIdentifiers | An event that describes details about a mobile application package. | Android |
| MobileAppsManifest | Delivers information about apps. | Android |
| MobileDetection | An event that's sent by the sensor when a sensor-level detection occurs. | iOS, Android |
| MobileOsForensicsReport |  | iOS, Android |
| MobileOsIntegrityStatus | Describes the integrity of the mobile OS (eg. jailbroken/rooted) | Android, iOS |
| MobilePowerStats | Sent when power level in a mobile device changes, also contains duration when the sensor is in foreg... | Android, iOS |
| ModifyServiceBinary | Indicates a Windows service's binary was changed. | Windows |
| ModuleBlockedEvent | This event is sent to inform cloud about the fact that given module (identified by hash) was blocked... | Windows, Linux, Falcon Container, macOS |
| ModuleBlockedEventWithPatternId | This event adds a potential reason for blocking (as a PatternId) to module blocking information. | Windows, Linux, Falcon Container, macOS |
| ModuleCertificateInfo2 |  | Windows |
| ModuleDetectInfo | This event identifies a scenario that would be a blocking prevention if more rigorous settings were ... | Linux, Falcon Container, Windows, macOS |
| ModuleDownloadComplete | Sent by LFODownloadActor when a new module has been downloaded as part of a configuration update. | Windows, Linux, macOS |
| ModuleLoadV3DetectInfo | Additional information for detections from the Module Load V3 template. | Windows |
| MotwWritten |  | Windows |
| MountedVolume |  | Windows |
| MpThreat | Microsoft protection threat. | Forensics |
| MpThreatAction | Report when a particular threat action type has occurred. | Forensics |
| MpThreatDetection | Microsoft protection threat detection. | Forensics |
| MpThreatDetectionWMI |  | Forensics |
| MpThreatWMI |  | Forensics |
| MSDocxFileWritten |  | macOS, Windows, Linux |
| MsiFileWritten |  | Linux, Windows, macOS |
| MsiTransactionExecuted |  | Windows |
| MSPptxFileWritten |  | macOS, Windows, Linux |
| MSVsdxFileWritten |  | macOS, Windows, Linux |
| MSXlsxFileWritten |  | Windows, macOS, Linux |
| NamedMutantHandleClosedTelemetry | An event that indicates that a process closed a handle to a known bad named mutex. | Windows |
| NamedPipe | Named pipe information. | Forensics |
| NamedPipeDetectInfo | Named pipe detect telemetry event | Windows |
| NamedSemaphoreHandleClosedTelemetry | An event that indicates that a process closed a handle to a known bad named semaphore. | Windows |
| NamespaceChanged |  | Linux, Falcon Container |
| NeighborListIP4 | This event shows the IPv4 network addresses and MAC addresses of other devices on the host's network... | macOS, Linux, Falcon Container, Forensics, Windows |
| NeighborListIP6 | This event shows the MAC addresses and IPv6 network addresses of other devices on the host's network... | macOS, Linux, Falcon Container, Windows |
| NetShareAdd | This event is generated when a network share is added or modified on a host. | Windows |
| NetShareDelete | This event is generated when a network share is removed from a host. | Windows |
| NetShareInfo | Shared resource information. | Forensics |
| NetShareSecurityModify | This event is generated when the security descriptor of a network share is changed. | Windows |
| NetworkCloseIP4 | An event that is generated by an application using a connection-oriented or connectionless protocol ... | Windows, Android, Forensics |
| NetworkCloseIP6 | An event that is generated by an application using a connection-oriented or connectionless protocol ... | Windows, Forensics |
| NetworkConnectIP4 | This event is generated when an application attempts a remote connection. Platforms: Forensics, Chro... | Windows, iOS, Linux, Falcon Container, macOS, Android |
| NetworkConnectIP4Blocked | This event is created whenever a NetworkConnectIP4 event is blocked. Platforms: iOS This event is cr... | Android, Windows, macOS |
| NetworkConnectIP4DetectInfo | This event is sent whenever a connection to malicious IP4 address is detected. | iOS, Android |
| NetworkConnectIP6 | This event is created whenever an application using a connection-oriented protocol attempts a remote... | Windows, iOS, Android, macOS |
| NetworkConnectIP6Blocked | This event is created whenever a NetworkConnectIP6 event is blocked because of the IP or the domain/... | iOS |
| NetworkConnectIP6DetectInfo | This event is sent whenever a connection to malicious IP6 address is detected. | iOS, Android |
| NetworkContainmentCompleted | This event is sent by the sensor after processing a NetworkContainmentRequest event from the cloud. ... | macOS, Linux, Windows |
| NetworkDnsSuffix | A network suffix name in the configured DNS suffix list. | Forensics |
| NetworkEndPointDataUsage | This event has total counts of sent/received octets/packets to/from the network-attached end point d... | Forensics |
| NetworkHostsFileEntry | A host name entry in the network hosts file. | Forensics |
| NetworkIcmpDataIP4 |  | Linux |
| NetworkIcmpDataIP6 |  | Linux |
| NetworkInterfaceStatistics |  | Forensics |
| NetworkLinkConfigGetAddress |  | Linux |
| NetworkLinkConfigGetLink |  | Linux |
| NetworkListenIP4 | This event is generated when an application establishes a socket in listening mode Platforms: Forens... | Windows, macOS, Android |
| NetworkListenIP6 | This event is created whenever an application using a connection-oriented protocol establishes a soc... | Windows, Android, Linux, Falcon Container, macOS |
| NetworkModuleLoadAttempt | An event that indicates that a process whose primary image was not on a network attempted to load a ... | Windows |
| NetworkOutboundPortScanDetectInfo |  | Windows |
| NetworkReceiveAcceptIP4 | This event is generated when an application using a connection-oriented protocol attempts to accept ... | Windows, Android, Linux, Falcon Container, macOS |
| NetworkReceiveAcceptIP6 | This event is created whenever an application using a connection-oriented protocol attempts to accep... | Windows, Android, Linux, Falcon Container, macOS |
| NetworkStatisticsIP4 |  | Forensics |
| NetworkStatisticsIP6 |  | Forensics |
| NetworkStatisticsTCP4 |  | Forensics |
| NetworkStatisticsTCP6 |  | Forensics |
| NetworkStatisticsUDP4 |  | Forensics |
| NetworkStatisticsUDP6 |  | Forensics |
| NetworkSummary |  | Windows |
| NetworkUncontainmentCompleted | Platforms: Linux, Windows, macOS This event is sent by the sensor after processing a NetworkUncontai... | Android, iOS |
| NewExecutableRenamed | This event is generated when an executable is renamed. | Windows, macOS |
| NewExecutableWritten | This event is generated when an executable file extension is written, whether or not it is truly an ... | Windows, Linux, macOS |
| NewScriptWritten | This event is generated when a new script is written (e.g. .js, .aspx, .bat, .ps1, .vbs, .lua). Plat... | Windows |
| NtfsLinkCreatedDetectInfo |  | Windows |
| NtfsQueryEaExploitAttempt |  | Windows |
| NullPageProtectionModificationAttempt | An event that indicates that an attempt was made to modify the protection of the NULL page. | Windows |
| NullPageUnmapAttempt | An event that indicates that an attempt was made to unmap the NULL page. | Windows |
| ObjCRuntimeAltered | An event that indicates an Obj-C method has been tampered with. MethodSignature indicates which Obj-... | iOS |
| OciContainerComplianceInfo |  | Linux, Falcon Container |
| OciContainerEngineInfo | An event that contains information about this container engine. | Linux, Falcon Container |
| OciContainerHeartbeat | An event that is sent by the sensor to indicate this container engine is still being used. This even... | Linux, Falcon Container |
| OciContainerInfo | An event that contains information about this container on creation of the container. | Linux, Falcon Container |
| OciContainerPlumbingSummary |  | Linux |
| OciContainerStarted | An event that is sent by the sensor to indicate a container has started when the container is create... | Linux, Falcon Container |
| OciContainerStopped | An event sent to indicate a container has stopped when the container is deleted. | Linux, Falcon Container |
| OciContainerTelemetry | An event that contains telemetry information on a container. | Linux, Falcon Container |
| OciImageHeartbeat | An event that is sent by the sensor to indicate this image is still being used. | Linux, Falcon Container |
| OciImageInfo | An event that contains information about this image used in a container. | Linux, Falcon Container |
| OdsActionStatus | Platforms: Windows | macOS |
| OdsCancelRequestReceived | Platforms: macOS | Windows |
| OdsMaliciousFileFound | Platforms: Windows | macOS |
| OdsProfileReceived | Platforms: Windows | macOS |
| OdsScanComplete | On-demand scan for files with name extensions and header magic values. | Forensics |
| OdsScheduleCanceled | Platforms: macOS | Windows |
| OdsScheduleCancelRequestReceived | Platforms: macOS | Windows |
| OdsScheduleRequestReceived | Platforms: macOS | Windows |
| OdsStarted | Platforms: Windows | macOS |
| OdsStartRequestReceived | Platforms: macOS | Windows |
| OdsStatus | Platforms: Windows | macOS |
| OleFileWritten | This event is generated when a file a Microsoft Office (Pre-Office 2007) file type is written to dis... | Windows, macOS, Linux |
| OoxmlFileWritten | This event is generated when a Microsoft Office (Post-Office 2007) file type is written to disk. | Windows, macOS, Linux |
| OpenDirectoryAttributeAdd |  | macOS |
| OpenDirectoryAttributeRemove |  | macOS |
| OpenDirectoryAttributeSet |  | macOS |
| OpenDirectoryCreateUser |  | macOS |
| OpenDirectoryDeleteUser |  | macOS |
| OpenDirectoryGroupAdd |  | macOS |
| OpenDirectoryGroupRemove |  | macOS |
| OpenDirectoryGroupSet |  | macOS |
| OpenDirectoryPasswordModification |  | macOS |
| OsfmDownloadComplete | Sent by LFODownloadActor when new OSFM data is downloaded. | Windows |
| OsUpdateTimestamp | Operating system update timestamp. | Forensics |
| OsVersionInfo | This event is generated during any one of the following scenarios: A host is turned on or rebooted A... | Windows, Linux, Falcon Container, Android, iOS, macOS |
| PackageManagerDownloadComplete |  | Kubernetes, Vmcluster, Windows, macOS, Linux, Falcon Container |
| PackedExecutableWritten | An event that indicates that a packed executable was written to disk. The packer type is indicated b... | Windows |
| PacketDiversionConnectionsOverloadConfigurationResponse |  | Windows |
| PacketFilterAttached |  | Linux |
| PathUnexpectedlyReadable | An event that indicates a system file or directory can be opened for reading. On a non-jailbroken sy... | iOS |
| PatternHandlingError | This event is emitted when an error occurs in processing a behavior. | macOS, Linux, Falcon Container, Windows |
| PcaAppLaunchEntry | An application launch entry in windows Program Compatibility Assistant (PCA) file PcaAppLaunchDic.tx... | Forensics |
| PcaGeneralDbEntry | An application launch entry in windows Program Compatibility Assistant (PCA) database PcaGeneralDb[0... | Forensics |
| PdfFileWritten | This event is generated when a PDF file type (.pdf) is written to disk. | Windows, Linux, macOS |
| PeaFileWritten |  | Windows |
| PeCodePageInfo | A code page that is used to decode code point values within a windows Portable Executable resource. | Forensics |
| PeFileWritten | This event is generated when a Windows Portable Executable file type is written to disk. The differe... | Windows, macOS, Linux |
| PeFileWrittenDetectInfo |  | Windows |
| PeHeaderInfo | Portable Executable header information from a Windows executable. | Forensics |
| PeHeaderOptionalInfo | Portable Executable optional header information from a Windows executable. | Forensics |
| PeLanguageId | A language on which a windows Portable Executable resource depends. | Forensics |
| PemFileWritten |  | macOS, Linux, Windows |
| PeSectionInfo | Windows Portable Executable (PE) section information. | Forensics |
| PeVersionInfo | An event that describes file version information from a Portable Executable file resource location, ... | Windows |
| PhpBase64Decode |  | Linux |
| PhpEvalString |  | Linux |
| PhpExecuteScript |  | Linux |
| PngFileWritten |  | macOS, Linux, Windows |
| PodInfo | Metadata associated with a Kubernetes pod. | Linux, Falcon Container |
| PodProductConfig |  | Linux, Falcon Container |
| Pop3Command |  | Windows, Linux |
| PrefetchFile | Prefetch or Layout file records 8 most recent execution times of a Windows application. | Forensics |
| PrivilegedProcessHandle | Indicates a process has opened a handle to a privileged process with special access rights. | Windows |
| PrivilegedProcessHandleFromUnsignedModule | This event contains information about a privileged process handle created from an unsigned module. | Windows |
| ProcessActivitySummary | A rollup event created when a process terminates. Includes statistical information about what a proc... | Windows, macOS |
| ProcessAncestryInformation | The ProcessAncestryInformation event captures unique process lineage chains (process, parent, grandp... | macOS, Linux, Falcon Container, Windows |
| ProcessBlocked | This event is generated when a process is blocked based on a prevention policy. Platforms: Windows L... | Windows, Linux, Falcon Container, macOS |
| ProcessControl |  | Linux, Falcon Container |
| ProcessDataUsage | Measurements and statistics of data traffic sent and received to/from the target process. | Forensics |
| ProcessEnvironmentEmpty |  | Linux |
| ProcessExecOnPackedExecutable | An event that contains telemetry data emitted on execution of a PE file which is known to be packed.... | Windows |
| ProcessExecOnRDPFile | A PE file was written and executed from an RDP session. | Windows |
| ProcessExecOnSMBFile | An event that contains telemetry data emitted on execution of a PE file which was written by SMB. | Windows |
| ProcessExecOnWinRMFile |  | Windows |
| ProcessHandleOpDetectInfo | An event that describes the operation on a Process handle that triggered a detection. | Windows |
| ProcessHandleOpDowngraded | An event that describes the operation on a Process handle where the AccessMask was downgraded. | Windows |
| ProcessHandleTableEntry | An entry in a process handle table referencing a kernel object. | Forensics |
| ProcessInjection | An event that indicates that a remote process wrote and executed code. | Windows |
| ProcessOpenedFileDescriptor |  | Forensics |
| ProcessPatternTelemetry | Platforms: Windows | Linux, macOS |
| ProcessRollup | An event that contains information from several sources and combines it into one event. The event de... | Windows |
| ProcessRollup2 | This event (often called "PR2" for short) is generated for a process that is running or has finished... | Windows |
| ProcessRollup2Stats | Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only... | macOS |
| ProcessSelfDeleted | This event indicates when a process self-delete situation is detected. It will be thrown when a proc... | macOS, Windows, Linux |
| ProcessSessionCreated |  | Linux, Falcon Container |
| ProcessSignal |  | Linux |
| ProcessState | Running process observed at collection time. | Forensics |
| ProcessSubstituteUser |  | macOS |
| ProcessTokenPrivilegesEdited |  | Windows |
| ProcessTokenStolen | An event that describes a process token stealing detection. ContextProcessId has been detected steal... | Windows |
| ProcessTrace |  | Linux, Falcon Container |
| ProcessTreeCompositionPatternTelemetry |  | Windows |
| ProcessWitness | Emitted when the sensor witnesses a process is running. This event is not an indication that a proce... | iOS |
| PromiscuousBindIP4 | This is a reified NetworkBindIP4 indicating a socket is in promiscuous mode. | Windows |
| PromiscuousBindIP6 |  | Windows |
| ProtectVmEtw | A virtual memory protect event generated from ETW data. | Windows |
| ProvisioningChannelVersionRequired | This event informs the cloud about the state of a channel on the sensor during provisioning. It is o... | Windows, Linux, Falcon Container, macOS |
| ProvisioningEnded | Sent when provisioning is completed. | Windows |
| ProvisioningStarted | Sent when sensor begins provisioning. | Windows |
| ProvisioningStatusUpdate | Sent every 2 minutes during provisioning. | Windows |
| PtActivationStatus | Reports host's compatibility with the Processor Trace feature. | Windows |
| PtTelemetry |  | Windows |
| PtyAttached |  | Linux |
| PtyCreated | An event that notifies that a pty has been created. | macOS |
| PtyDetached |  | Linux |
| PythonFileWritten |  | Windows |
| QuarantineActionResult | This event reports the result of a file quarantine triggered by Falcon Prevent. | Linux, macOS, Windows |
| QuarantinedFile | This event is generated when a file is quarantined by Falcon Prevent. | macOS, Linux, Windows |
| QuarantinedFileState | This event reports the state of a file quarantined by Falcon Prevent. | macOS, Linux, Windows |
| QuarantineXattribute |  | Forensics |
| QueueApcEtw |  | Windows |
| QuickAssistCookieInfo |  | Forensics |
| QuickAssistDownloadEnded |  | Forensics |
| QuickAssistDownloadStarted |  | Forensics |
| QuickAssistHistoryVisit |  | Forensics |
| RansomwareCreateFile | A reified LocalFsPostCreate event so the cloud can route these events for ransomware support. | Windows |
| RansomwareFileAccessPattern | Helper event for ransomware file access patterns. | Windows |
| RansomwareOpenFile | A reified LocalFsPostCreate event so the cloud can route these events for ransomware support. | Windows |
| RansomwareRenameFile | A reified LocalFsPostRename event so the cloud can route these events for ransomware support. | Windows |
| RarFileWritten | Emitted when a process is done writing a RAR file. | Windows, Linux, macOS |
| RawBindIP4 | An event that is created when an application using a connection-oriented or connectionless protocol ... | Windows, Android, Linux, Falcon Container, macOS |
| RawBindIP6 | An event that is created when an application using a connection-oriented or connectionless protocol ... | Linux, Falcon Container, Android, macOS, Windows |
| RecentExecutionTimestamp | Recent execution timestamp from a Forensics artifact. | Forensics |
| RecentlyModifiedFileExecutedInContainer | Emitted by the Falcon sensor for Linux when: A new or modified binary executable is run in a contain... | Linux, Falcon Container |
| RecoveryActionDeleteFilesComplete |  | Linux, Falcon Container, Kubernetes, macOS, Windows |
| RecoveryActionDeleteFilesReply |  | macOS, Linux, Falcon Container, Kubernetes, Windows |
| RecoveryActionGetModuleTableRecordComplete |  | macOS, Windows, Linux, Falcon Container |
| RecoveryActionGetRuntimeSystemTagsComplete |  | macOS, Windows, Linux, Falcon Container |
| RecoveryActionGetSystemTagsComplete |  | macOS, Linux, Falcon Container, Windows, Kubernetes |
| RecoveryActionKillProcessesComplete |  | macOS, Linux, Falcon Container, Kubernetes, Windows |
| RecoveryActionKillProcessesReply |  | Kubernetes, Linux, Falcon Container, macOS, Windows |
| RecoveryActionManipulateModuleTableComplete |  | Windows, Linux, Falcon Container, macOS |
| RecoveryActionRegistryCreateKeyComplete |  | Windows |
| RecoveryActionRegistryCreateKeyReply |  | Windows |
| RecoveryActionRegistryDeleteKeyComplete |  | Windows |
| RecoveryActionRegistryDeleteKeyReply |  | Windows |
| RecoveryActionRegistryDeleteValueKeyComplete |  | Windows |
| RecoveryActionRegistryDeleteValueKeyReply |  | Windows |
| RecoveryActionRegistrySetValueKeyComplete |  | Windows |
| RecoveryActionRegistrySetValueKeyReply |  | Windows |
| RecoveryActionSetRuntimeSystemTagsComplete |  | macOS, Linux, Falcon Container, Windows |
| RecoveryActionSetSystemTagsComplete |  | Linux, Falcon Container, macOS, Kubernetes, Windows |
| ReflectiveDllLoaded | An event that indicates that a user space thread reflectively loaded DLL. | Windows |
| ReflectiveDllOpenProcess | A userspace thread attempted to open a process which appeared to originate from a reflectively loade... | Windows |
| ReflectiveDotnetModuleLoad | Event generated when .NET module is reflectively (e.g. from a byte array) loaded in a process. | Windows |
| RegCredAccessDetectInfo |  | Windows |
| RegCrowdstrikeKeyUpdate |  | Windows |
| RegCrowdstrikeValueUpdate |  | Windows |
| RegFeatureUsageInfo |  | Forensics |
| RegGenericInfo | Registry entry generic information. | Forensics |
| RegGenericKeyUpdate |  | Windows |
| RegGenericValueUpdate | An event that indicates that a registry value has been updated. | Windows |
| RegisterRawInputDevicesEtw | An event that indicates that an application called the RegisterRawInputDevices API. Captured using t... | Windows |
| RegistryHiveFileWritten |  | Windows |
| RegistryOperationBlocked | An event that indicates that a registry operation has been blocked using a callback filter. | Windows |
| RegistryOperationDetectInfo | An event that describes a registry operation blocked using a callback filter. | Windows |
| RegKeySecurityDecreasedFromUnsignedModule | This event contains information about a protected registry security object whose security was decrea... | Windows |
| RegNtPostOpenKeyEx | Registry post open key operation event. | Windows |
| RegNtPostOpenKeyExUpImpersonating | A reified RegNtPostOpenKeyEx event that occurred in the context of a thread up-impersonating another... | Windows |
| RegShimCache | Shim cache registry entry. | Forensics |
| RegSystemConfigKeyUpdate |  | Windows |
| RegSystemConfigValueUpdate | An event that indicates that a registry value related to system configuration or security has been u... | Windows |
| RegValueQueryDetectInfo |  | Windows |
| RemediationActionKillIP4Connection | Sensor attempted to kill a connection to a malicious IPv4 address. No further data will be sent or r... | iOS, Android |
| RemediationActionKillIP6Connection | Sensor attempted to kill a connection to a malicious IPv6 address. No further data will be sent or r... | iOS, Android |
| RemediationActionKillProcess | Notification of a kill process remediation action attempted by the sensor. Platforms: macOS, Windows... | Windows |
| RemediationActionQuarantineFile | Notification of a quarantine file remediation action attempted by the sensor. | Windows |
| RemediationActionQuarantineMacroFile |  | Windows |
| RemediationActionQuarantineOfficeMacroFile |  | Windows |
| RemediationActionRegistryRemoval | Notification of a registry persistence removal remediation action attempted by the sensor. | Windows |
| RemediationActionScheduledTaskRemoval | Notification of a scheduled task persistence removal remediation action attempted by the sensor. | Windows |
| RemediationActionServiceRemoval | Notification of a service persistence removal remediation action attempted by the sensor. | Windows |
| RemediationMonitorKillProcess | Platforms: Windows Notification of a kill process remediation action that would have been attempted ... | Linux, macOS |
| RemediationMonitorQuarantineFile | Notification of a quarantine file remediation action that would have been attempted by the sensor bu... | Windows |
| RemediationMonitorRegistryRemoval | Notification of a registry persistence removal remediation action that would have been attempted by ... | Windows |
| RemediationMonitorScheduledTaskRemoval | Notification of a scheduled task persistence removal remediation action that would have been attempt... | Windows |
| RemediationMonitorServiceRemoval | Notification of a service persistence removal remediation action that would have been attempted by t... | Windows |
| RemoteBruteForceDetectInfo | An event that describes a remote brute force detection. | Windows |
| RemoteCommandResponse |  | Windows, macOS, Linux |
| RemoteProcessMemoryRead |  | Linux |
| RemoteProcessMemoryWrite |  | Linux |
| RemoteThreadCreate |  | macOS |
| RemovableDiskModuleLoadAttempt | An event that indicates that a process with a primary image that is not on a removable disk attempte... | Windows |
| RemovableMediaFileWritten | An event that is emitted for files written to removable media on Android devices. | Android |
| RemovableMediaVolumeMounted | This event provides information about a removable media volume that was just mounted. | Windows, Android |
| RemovableMediaVolumeUnmounted | An event that contains information about a removable media volume that was just unmounted. | Android |
| ResourceLimit |  | Linux |
| ResourceUtilization | Platforms: Linux, Falcon Container An event that contains CPU and RAM utilization data for a system.... | macOS, Kubernetes |
| RootkitDetectionResponse |  | Windows |
| RouteIP4 | IPv4 Route entry. | Forensics |
| RouteIP6 | IPv6 Route entry. | Forensics |
| RpmFileWritten |  | macOS, Windows, Linux |
| RtfFileWritten | Emitted when a process is done writing an RTF file. | Windows, macOS, Linux |
| RuntimeEnvironmentVariable | Environment Variable provided to a process; In the context of falcon forensics, this is an environme... | Forensics |
| SafetyNetCheckFailed | An event that indicates the SafetyNet check could not be completed. | Android |
| SafetyNetCompatibilityStatus | An event that contains the SafetyNet compatibility status obtained via the Google SafetyNet API. | Android |
| SafetyNetVerifyAppsStatus | An event that contains information about the status of SafetyNet Verify Apps (Google Play Protect) o... | Android |
| SAMHashDumpFromUnsignedModule | This event contains information about an unsigned module that accessed protected SAM account registr... | Windows |
| ScheduledTaskDeleted | This event is sent when Falcon has detected that a scheduled task has been removed from the machine.... | Windows |
| ScheduledTaskInfo | Scheduled windows tasks. | Forensics |
| ScheduledTaskModified | Event sent when EAEP has determined a new scheduled task was modified to the local machine. The RPC ... | Windows |
| ScheduledTaskRegistered | This event is sent when Falcon detects that a scheduled task has been added to the machine, either l... | Windows |
| ScheduledTaskTamperingRegistryOperation |  | Windows |
| ScheduledTaskTemplateDetectInfo |  | Windows |
| ScreenshotTakenEtw | An event that indicates that partial or full screenshot has been taken. Captured using the ETW consu... | Windows |
| ScriptControlBlocked | This event is sent when Falcon Host has blocked malicious script content from being executed on the ... | Windows |
| ScriptControlDetectInfo | This event is sent when Falcon has detected malicious script content being executed on the host. Thi... | Windows, macOS, Linux, Falcon Container |
| ScriptControlDetectInvalidInfo |  | macOS, Linux, Falcon Container |
| ScriptControlDotNetMetadata | Contains the last 56kb of ScriptContent from a .NET AMSI scan. | Windows |
| ScriptControlErrorEvent | An event that contains telemetry data containing up to 56 KB ScriptContent field data from AMSI (Ant... | Windows |
| ScriptControlScanInfo |  | Windows, Linux, Falcon Container, macOS |
| ScriptControlScanTelemetry |  | Windows |
| ScriptFileContentsDetectInfo |  | Windows |
| ScriptFileWrittenInfo |  | Windows |
| SecureTrafficDecrypted | An event that contains certificate info for the compromised network connection. | Android, iOS |
| SEHOverWriteAttempt | An event that is emitted when a UserException event has failed a SEH (Structured Exception Handler) ... | Windows |
| SELinuxStatus | An event that contains info about the SELinus status. | Android |
| SensitiveWmiQuery | An event that indicates that a client process executed a sensitive WMI query. | Windows |
| SensorAntiTamperState |  | Windows |
| SensorEnteredSafemode |  | Linux, Falcon Container, macOS, Windows |
| SensorGroupingTagsUpdate |  | Windows, Android |
| SensorHeartbeat | Sent periodically to inform the cloud that the sensor is active. Platforms: Linux, Falcon Container ... | Windows, macOS, Android, iOS |
| SensorMetadataUpdate |  | Linux |
| SensorSelfDiagnosticAlert |  | Linux, Windows, macOS |
| SensorSelfDiagnosticTelemetry |  | Windows, macOS, Linux |
| SensorSettingsUpdate |  | Linux, Falcon Container, Windows, macOS, Kubernetes, Vmcluster |
| SensorTampering | Thrown when a tampering event occurs on the sensor. | Linux |
| ServicesStatusInfo | Detailed information and status of a windows service. Platforms: Windows | Forensics |
| ServiceStarted | This event is generated when a standalone service is started by the service control manager (SCM). S... | Windows |
| ServiceStopped | This event is emitted when a standalone service is stopped by the service control manager (SCM). Unf... | Windows |
| SessionPatternTelemetry |  | macOS, Linux |
| SetThreadCtxEtw |  | Windows |
| SetWindowsHook | An event that is sent from the sensor when a user mode program attempts to set a windows hook. | Windows |
| SetWindowsHookExEtw | An event that indicates that an application called SetWinEventHookEx API. Captured using the ETW con... | Windows |
| SetWinEventHookEtw | An event that indicates that an application called the SetWinEventHook API. Captured using the ETW c... | Windows |
| SevenZipFileWritten | This event is generated when a 7ZIP file type (.7zip) is written to disk. | macOS, Linux, Windows |
| SharedObjectLoaded |  | Linux |
| ShellBagFileTimeStampMetadata | One event is emitted per timestamp from a ShellBag registry entry. | Forensics |
| ShellBagInfo | Windows ShellBag MRU registry entry. | Forensics |
| ShellCommandLineInfo |  | Linux |
| ShimDbTag | A tag entry in the Shim database. | Forensics |
| SignInfo | Sent by FalconForensicsCollector containing information about the signing-state of an image. Platfor... | Forensics |
| SignInfoWithCertAndContext | Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains... | Windows, macOS |
| SignInfoWithContext | Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains... | macOS, Windows |
| SigningIdentity |  | iOS |
| SigningPublicKey |  | Android, iOS |
| SldFileWritten |  | Windows |
| SmbClientNamedPipeConnectEtw | An event that indicates when a machine connects to a remote SMB (Server Message Block) named pipe. T... | Windows |
| SmbClientShareClosedEtw | An event that indicates when a machine disconnects from a remote share. This event is supported on a... | Windows |
| SmbClientShareLogonBruteForceLowThreshold |  | Windows |
| SmbClientShareLogonBruteForceSuspected |  | Windows |
| SmbClientShareOpenedEtw | An event that indicates when a machine connects to a remote share. This event is supported on all Wi... | Windows |
| SmbServerLocalNamedPipeOpenedEtw |  | Windows |
| SmbServerShareOpenedEtw | An event that indicates a remote machine opening a local share. This event is supported on all Windo... | Windows |
| SmbServerV1AuditEtw | An event that indicates that a client attempted to connect to this machine using the Server Message ... | Windows |
| SmtpAttachment |  | Linux |
| SmtpCommand |  | Linux |
| SmtpEmailMessage |  | Windows |
| SnapshotVolumeMounted | Information about a snapshot volume that was just mounted. | Windows |
| SourceCodeFileWritten |  | Windows, macOS |
| SpotlightEntityBatch | Single Event consisting of a list of Spotlight Entity State data packaged for optimal size and part ... | Windows, macOS |
| SpotlightEntityBatchHeader | Spotlight Batch header to indicate all required metadata of incoming batch along with information to... | Windows, macOS |
| SpotlightEntitySystemState | Spotlight Entity heart-beat event to notify cloud of current state with last synced batch and Channe... | Windows, macOS |
| SpotlightSearchEntry | Per-user spotlight search information. | Forensics |
| SruApplicationResourceUsage | System Resource Utilization Monitor: application resource usage per user. | Forensics |
| SruApplicationTimelineProvider | System Resource Utilization Monitor: application resource usage timeline. | Forensics |
| SruNetworkConnectivityUsage | System Resource Utilization Monitor: connection time per local network interface, application and us... | Forensics |
| SruNetworkDataUsage | System Resource Utilization Monitor: bytes sent/received per local network interface, application an... | Forensics |
| SSHClientAuthenticated |  | Linux |
| SsoApplicationAccess | Indicates successful access to an application through an SSO facilitator, which could be either an I... | Public Cloud |
| SsoApplicationAccessFailure | Indicates failed access to an application through an SSO facilitator, which could be either an IDaaS... | Public Cloud |
| SsoUserLogon | Indicates an initial, successful sign-in to an SSO facilitator, which could be either an IDaaS direc... | Public Cloud |
| SsoUserLogonFailure | Indicates an initial, failed sign-in to an SSO facilitator, which could be either an IDaaS directory... | Public Cloud |
| StaticAnalysisContainerTelemetry | Cloudable event in response to a telemetry query for the static analysis containers. | Windows |
| StaticConfigurationError |  | Linux |
| StorageEncryptionStatus | An event that contains information about the Device Storage encryption. | Android |
| SudoCommandAttempt |  | macOS |
| SuperfetchAppInfo | Application entry from Windows Superfetch AgForegroundAppHistory.db. | Forensics |
| SuperfetchAppSchedule | Application running schedule/period recently updated from Windows Superfetch AgGlobalHistory.db. | Forensics |
| SuspectCreateThreadStack | This event is used to indicate that suspicious data has been discovered in the context of a CreateTh... | Windows |
| SuspendProcessError | This event is emitted if KillProcessActor fails to suspend a process. | macOS, Windows, Linux, Falcon Container |
| SuspiciousAndroidActivityFound | An event that indicates that a currently installed application on the device has been found providin... | Android |
| SuspiciousAndroidLogcatMessageFound | An event that indicates that an application log message originating from a suspicious source has bee... | Android |
| SuspiciousAndroidStackTraceElementFound | An event that indicates that a hooking framework has been found via stacktrace analysis and that the... | Android |
| SuspiciousAndroidSystemPropertyFound | An event that indicates that a suspicious system property has been found. This might indicate the OS... | Android |
| SuspiciousAppFound | An event that indicates that a suspicious application has been found to be installed on the device. | Android |
| SuspiciousCreateSymbolicLink | An event that indicates the creation of a suspicious symbolic link. | Windows |
| SuspiciousCredentialModuleLoad | An indicator event fired when suspicious credential module activity is detected, which means the pro... | Windows |
| SuspiciousDnsRequest | This event is generated when the sensor detects a suspicious DNS request. A request is suspicious if... | Windows, Linux, macOS |
| SuspiciousEseFileWritten | This event indicates that a possible domain credential file (NTDS.dit) was copied from a volume snap... | Windows |
| SuspiciousLackOfProcessRollupEvents | This event is emitted if we don't see any ProcessRollup2 events for a long time. | Windows |
| SuspiciousPeFileWritten | A suspicious PE image file was written to disk. | Windows |
| SuspiciousPrivilegedProcessHandle | Indicates a process has opened a handle to a privileged process with special access rights. | Windows |
| SuspiciousRawDiskRead | This event indicates a process successfully read a target file using raw disk access. | Windows |
| SuspiciousRawDiskReadFromUnsignedModule | This event contains information about an unsigned module reading a target file using raw disk access... | Windows |
| SuspiciousRegAsepUpdate | An event that describes the registry activity that triggered a suspicious registry ASEP (Autostart E... | Windows |
| SuspiciousUserFontLoad | Sent when a UserFontLoad event has been blocked by the sensor. | Windows |
| SuspiciousUserRemoteAPCAttempt | An event that indicates that a remote APC (Asynchronous Procedure Call) that is classified as potent... | Windows |
| SyntheticPR2Stats |  | macOS |
| SyntheticProcessRollup2 | This event provides data similar to what is available in a ProcessRollup2. SyntheticProcessRollup2 e... | Windows, Linux, Falcon Container, macOS |
| SyntheticProcessTrace |  | Linux |
| SyntheticSharedObjectLoaded |  | Linux |
| SyntheticSystemdServiceCreated |  | Linux |
| SyntheticSystemdTimerCreated |  | Linux |
| SyntheticVirtualMemoryArea |  | Linux |
| SyscacheEntry | An entry in windows syscache hive. | Forensics |
| SysConfigInfo |  | Linux, Falcon Container |
| SystemCapacity | An event that describes the CPU and RAM capacity of the system. The event is sent when the sensor co... | Windows, macOS |
| SystemdServiceCreated |  | Linux |
| SystemdServiceDeleted |  | Linux |
| SystemdServicePropertiesChanged |  | Linux |
| SystemdTimerCreated |  | Linux |
| SystemdTimerDeleted |  | Linux |
| SystemdTimerPropertiesChanged |  | Linux |
| SystemExtension | Describes a macOS system extension identified by the collector. | Forensics |
| SystemPartitionAltered | An event that indicates a system partition has been altered and is in an unexpected state. | iOS |
| SystemPartitionStatus | An event that contains information about the device system partition. This event is deprecated as of... | Android |
| SystemTokenStolen | An event that indicates that system token stealing was detected. | Windows |
| SystemUpdatesBlockedByDNS | Indicates that OS updates have been blocked via DNS. | iOS |
| SystemUpdatesBlockedByFilesystem | Indicates that OS updates have been blocked via the filesystem. | iOS |
| SystemUpdatesBlockedByHTTP | Indicates that OS updates have been blocked via HTTP. | iOS |
| TarFileWritten | Emitted when a process is done writing a Tar file. | macOS, Linux, Windows |
| TccModification |  | macOS |
| TcgPcrInfo | An event that contains the Platform Configuration Register (PCR) values. | Windows |
| TerminalSavedStateInfo | MacOS terminal saved state information. | Forensics |
| TerminateProcess | This event is thrown when a process exits normally or is forcibly terminated. Platforms: ChromeOS | Windows, macOS, Linux, Falcon Container |
| TerminateRemoteProcessEtw |  | Windows |
| ThreadBlocked | Reports the status of a block thread attempt. | Windows |
| ThreadPreviousModeMismatch |  | Windows |
| TiffFileWritten |  | Linux, macOS, Windows |
| TlsClientHello | Platforms: macOS | Linux, Windows |
| TokenImpersonated | An event that contains detailed before and after impersonation information for detection telemetry. | Windows |
| TrampolineDetected | An event that indicates a C function has been tampered with. In iOS jailbreak, functions are modifie... | iOS |
| TriggeredMemoryDumpResponse |  | Windows |
| UACAxisElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target Act... | Windows |
| UACCOMElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target COM... | Windows |
| UACCredentialCaptureElevation | This UAC event indicates the UAC consent.exe application was used by Windows to refresh the smart ca... | Windows |
| UACExeElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target exe... | Windows |
| UACMSIElevation | This UAC event indicates an attempt has been made to elevate the security privileges of a target MSI... | Windows |
| UmppaErrorEvent |  | Windows |
| UmppcDetectInfo | An event that describes a UMPPC-based detection. | Windows |
| UmppcEntryAnomaly |  | Windows |
| UnclassifiedRegValueUpdate |  | Windows |
| UncontainerizeAppResponse | Sent in response to UncontainerizeApp, containing response information for the operation. | Android |
| UnexpectedDynamicLibraryLoaded | An event that indicates that an unexpected dynamic library was loaded at runtime. | iOS |
| UnexpectedEnvironmentVariable | An event that indicates some dangerous environment variables have made it to the app at runtime. | iOS |
| UnexpectedFileFound | An event that indicates a file that should not exist on the device has been found. Platforms: Androi... | iOS |
| UnixFileWritten |  | Android |
| UnixName |  | Linux |
| UnsignedModuleLoad | This event contains information about an unsigned module that was loaded into a target process. It c... | Windows |
| UpdateManifestDownloadComplete | An update manifest download has completed. | Windows |
| UsbDeviceInfo | Information on each USB device attachment. | Forensics |
| UserAccessLogEntry | Per-user access log information for the year for a service role and IP address pair on Windows serve... | Forensics |
| UserAccount | Describes an observed user account. | Forensics |
| UserAccountAddedToGroup | This event is generated when an existing user account is added to an existing group. The data will i... | Windows |
| UserAccountCreated | Platforms: Windows This event is generated when a new user account is created. The data will indicat... | Linux |
| UserAccountDeleted | This event is generated when a user account is deleted. The data will indicate the initial process (... | Windows |
| UserAccountRemovedFromGroup |  | Windows, Linux |
| UserAssistAppLaunchInfo | Application launched via user-assisted GUI menu. | Forensics |
| UserEatAccessMonitoring |  | Windows |
| UserExceptionDEP | This event is emitted when a userspace process is detected as having has a DEP or NX-related excepti... | Windows |
| UserFontLoad | An event that is sent when a user mode program attempts to add a font. | Windows |
| UserGroupCreated |  | Linux |
| UserGroupDeleted |  | Linux |
| UserIdentity | The UserIdentity event is generated when a user logs in to a host. It conveys important security-rel... | Windows, macOS |
| UserInformationEtw | An event that indicates the password of a user was changed or set and other user information taken f... | Windows |
| UserLogoff | This event is generated when a user logs off from a host. Platforms: ChromeOS, Linux | macOS, Windows |
| UserLogon | This event is generated when a user logs on to a host. Platforms: ChromeOS | Linux, macOS, Windows |
| UserLogonFailed | This event is generated when a user logon fails. | Windows |
| UserLogonFailed2 | An event that indicates that a local user attempted to logon, but failed due to bad password. LogonT... | Windows |
| UserSetProcessBreakOnTermination |  | Windows |
| USNRecord |  | Forensics |
| VdiFileWritten |  | macOS, Linux, Windows |
| VerifyAppsDisabled | This event has been deprecated. | Android |
| VirtualMemoryArea |  | Linux |
| VMClusterInfo | Event sent periodically to let the cloud know that the sensor is running with the following VM clust... | Vmcluster |
| VmcSensorStatus | This event is sent to provide VMC sensor operational status. | Vmcluster |
| VmcVmAsset | This event is sent to provide VMware vCenter VM information. | Vmcluster |
| VmdkFileWritten |  | macOS, Windows, Linux |
| VolumeSnapshotCreated | A volume snapshot has been created. | Windows |
| VolumeSnapshotDeleted | A volume snapshot has been deleted. | Windows |
| VolumeSnapshotOperationBlocked | Event describing a snapshot volume block operation. IFN and CL are based upon the RpcProcessId, in V... | Windows |
| VulnerableDriverDetectInfo |  | Windows |
| WebScriptFileWritten |  | Linux, Windows, macOS |
| WebShellDetected | To identify webshell script files in a target folder, the content of each text file is matched again... | Forensics |
| WfpFilterTamperingFilterAdded | This event is created whenever WFP indicates to our callout driver that a new filter that references... | Windows |
| WfpFilterTamperingFilterDeleted | This event is created whenever WFP indicates to our callout driver that a filter that references one... | Windows |
| WiFiConnect | Sent when a device connects to a WiFi network. This event is only sent if the Connected Wi-Fi networ... | Android, iOS |
| WiFiDisconnect | Sent when a device disconnects from a WiFi network. This event is only sent if the Connected Wi-Fi n... | Android, iOS |
| WindowsTimelineEntry |  | Forensics |
| WindowsTimelineEntryTimestamp |  | Forensics |
| WlanInterfaceInfo |  | Forensics |
| WmiCreateProcess | Windows Management Instrumentation (WMI) is a default service installed on machines with Windows XP ... | Windows |
| WmiFilterConsumerBindingEtw | An event that is emitted when a WMI (Windows Management Instrumentation) consumer instance gets boun... | Windows |
| WmiProviderRegistrationEtw | An event that is emitted when a WMI (Windows Management Instrumentation) provider gets registered. C... | Windows |
| WmiQuery | Windows Management Instrumentation (WMI) query status. | Forensics |
| WmiQueryDetectInfo |  | Windows |
| WroteExeAndGeneratedServiceEvent | Indicates a process both wrote an executable and generated a service event. | Windows |
| WSLDistributionRegistered | A user registers a Linux distribution but hasn’t started it yet. | Windows |
| WSLDistributionStarted | The Linux distribution starts. | Windows |
| WSLDistributionStopping | The Linux distribution is stopping. | Windows |
| WSLDistributionUnregistered | A user unregisters a Linux distribution. | Windows |
| WSLMetadata |  | Linux |
| WSLVMStarted | The Linux Virtual Machine Root Namespace starts. | Windows |
| WSLVMStopping | The Linux Virtual Machine Root Namespace is stopping. | Windows |
| XarFileWritten | Emitted when a process is done writing a Xar file. macOS installer files are of this type. | macOS, Linux, Windows |
| XProtectAction |  | macOS |
| XumdHookEvent |  | Windows |
| XumdStatus |  | Windows |
| XzFileWritten |  | macOS, Linux, Windows |
| Yz1FileWritten |  | Windows |
| ZerologonExploitAttempt |  | Windows |
| ZipFileWritten | This event is generated when a ZIP file type (.zip) is written to disk. | Windows, macOS, Linux |
| ZpaqFileWritten |  | Windows |
| ZstdFileWritten |  | Linux, macOS, Windows |


## Detailed Event Information

### AbnormalTerminationNotification

**Description:** 

**Platforms:** Kubernetes, Linux, Falcon Container, Vmcluster

---

### AccessoryConnected

**Description:** Sent when the device connects to an external accessory. This event will only be sent if the Connected Bluetooth devices setting is enabled in Mobile Policies.

**Platforms:** Android, iOS

---

### AccessoryDisconnected

**Description:** Sent when a device disconnects from an external accessory. This event will only be sent if the Connected Bluetooth devices setting is enabled in Mobile Policies.

**Platforms:** Android, iOS

---

### ActiveDirectoryAccountCreated

**Description:** Indicates the creation of the subject account.

**Platforms:** Windows

---

### ActiveDirectoryAccountDepartmentUpdate

**Description:** Indicates a change to the subject account's department.

**Platforms:** Windows

---

### ActiveDirectoryAccountDirectContainingGroupEntitiesUpdate

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAccountDisabled

**Description:** Indicates the subject account has been disabled.

**Platforms:** Windows

---

### ActiveDirectoryAccountEnabled

**Description:** Indicates the subject account has been enabled.

**Platforms:** Windows

---

### ActiveDirectoryAccountFlattenedContainingGroupEntitiesUpdate

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAccountLocked

**Description:** Indicates the subject account has been locked.

**Platforms:** Windows

---

### ActiveDirectoryAccountNameUpdate

**Description:** Indicates a change to the subject account's SAM account name.

**Platforms:** Windows

---

### ActiveDirectoryAccountOuUpdate

**Description:** Indicates a change to the subject account's organizational unit.

**Platforms:** Windows

---

### ActiveDirectoryAccountPasswordUpdate

**Description:** Indicates a change to the subject account's password.

**Platforms:** Windows

---

### ActiveDirectoryAccountUnlocked

**Description:** Indicates the subject account has been unlocked.

**Platforms:** Windows

---

### ActiveDirectoryAuditGpoModified

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuditGroupMemberModified

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuditGroupModified

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuditPasswordModificationAttempt

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuditUserModified

**Description:** 

**Platforms:** Windows

---

### ActiveDirectoryAuthentication

**Description:** Indicates that the Domain Controller handled one or more successful authentications by an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryAuthenticationFailure

**Description:** Indicates that the Domain Controller handled one or more failed authentications by an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryIncomingDceRpcEpmRequest

**Description:** Indicates that the Domain Controller must handle one or more incoming DCE/RPC EPM (Endpoint Manager) requests from an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryIncomingDceRpcRequest

**Description:** Indicates that the Domain Controller must handle one or more incoming DCE/RPC requests from an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryIncomingLdapSearchRequest

**Description:** Indicates that the Domain Controller must handle one or more LDAP search requests from an account on an endpoint.

**Platforms:** Windows

---

### ActiveDirectoryIncomingPsExecExecution2

**Description:** Indicates remote code execution on a domain controller using PsExec. This event is generated based on a REMOTE_INTERACTIVE type ActiveDirectoryIncomingDceRpcEpmRequest event that correlates with an ActiveDirectoryServiceAccessRequest event to the Common Internet File System (CIFS) or a host Service Principal Name (SPN). This event replaces the ActiveDirectoryIncomingPsExecExecution event, which is now obsolete.

**Platforms:** Windows

---

### ActiveDirectoryInteractiveDomainLogon

**Description:** Indicates an interactive logon to an Active Directry domain handled by a Domain Controller. The interactive logon is combined of initial authentication following by some service access events.

**Platforms:** Windows

---

### ActiveDirectoryServiceAccessRequest

**Description:** Indicates that the Domain Controller handled one or more successful service requests from an account on an endpoint. The requests were to a service identified by an Active Directory account.

**Platforms:** Windows

---

### ActiveDirectoryServiceAccessRequestFailure

**Description:** Indicates that the Domain Controller handled one or more failed service requests from an account on an endpoint. The requests were to a service identified by an Active Directory account.

**Platforms:** Windows

---

### AcUninstallConfirmation

**Description:** This event is generated when a Falcon sensor is uninstalled from a host. Important: The Falcon sensor stores events locally in a cache, which enables you to maintain data integrity even if connection to the cloud is interrupted. The cache holds a maximum of 20,000 events and sends them after a host re-establishes a connection with the cloud. However, if you reboot, the cache is lost. This means that if you uninstall a sensor off network and reboot, the cache storing those events is lost, including any AcUninstallConfirmation events.

**Platforms:** Windows, Linux, macOS

---

### AcUnloadConfirmation

**Description:** The cloud will respond with this event as acknowledgement that a sensor was uninstalled.

**Platforms:** Windows, Linux, macOS

---

### AdditionalHostInfo

**Description:** Serves as an addition to kernel-driven HostInfo event. Provides host-specific machine information from user mode. ObjectGuid is optional because a given host may not be joined to a domain. Platforms: macOS

**Platforms:** Windows

---

### ADExplorerFileWritten

**Description:** 

**Platforms:** Windows

---

### AgentConnect

**Description:** This event is generated when the sensor successfully connects to the cloud. Platforms: Windows Legacy

**Platforms:** Windows, Linux, Falcon Container, iOS, Kubernetes, macOS, Android

---

### AgenticSessionEnd

**Description:** 

**Platforms:** Windows

---

### AgenticSessionStart

**Description:** 

**Platforms:** Windows

---

### AgenticSubagentStart

**Description:** 

**Platforms:** Windows

---

### AgenticToolRequest

**Description:** 

**Platforms:** Windows

---

### AgenticUserPromptSubmit

**Description:** 

**Platforms:** Windows

---

### AgentOnline

**Description:** This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor is installed on a host 3. An existing sensor is updated This event can help to determine when a host was last rebooted. However, it's not intended for gathering report data, such as uptime of long-running servers or counting all active hosts. For reports, use Falcon Investigate's Sensor Report. Platforms: iOS This event is generated when any of these occur: 1. A host is turned on or rebooted 2. A new sensor is installed on a host 3. An existing sensor is updated 4. The managed configuration changes This event can help to determine when a host was last rebooted. However, it's not intended for gathering report data, such as uptime of long-running servers or counting all active hosts. Platforms: Windows Legacy, Vmcluster

**Platforms:** Windows, Linux, Falcon Container, macOS, ChromeOS, Android, Kubernetes

---

### AiAgentClassifyChildTelemetry

**Description:** 

**Platforms:** Windows, macOS

---

### AiAgentClassifyRootTelemetry

**Description:** 

**Platforms:** Windows, macOS

---

### AksAgentPool

**Description:** Snapshot of an Azure AKS Agent Pool.

**Platforms:** Public Cloud

---

### AksCluster

**Description:** Snapshot of an Azure AKS cluster.

**Platforms:** Public Cloud

---

### AksVMSS

**Description:** Snapshot of an Azure Virtual Machine Scale Sets.

**Platforms:** Public Cloud

---

### AllocVmEtw

**Description:** A windows-only internal event that represents kernel initiated memory allocation. Captured using the ETW consumer.

**Platforms:** Windows

---

### AmcacheEntry

**Description:** Metadata related to PE execution and program installation on Windows 7 and Server 2008 R2 and above.

**Platforms:** Forensics

---

### AmsBytePatternScanResult

**Description:** 

**Platforms:** Windows

---

### AmsBytePatternScanTelemetry

**Description:** 

**Platforms:** Windows

---

### AmsiRegistrationStatus

**Description:** Event to record status in AMSI module.

**Platforms:** Windows

---

### AndroidEnterpriseInfo

**Description:** This event contains metadata related to the state of the device as reported by the Android Management API (AMAPI).

**Platforms:** Android

---

### AndroidInitServiceAdded

**Description:** An event that indicates that a new init (boot) service has been added to the system configuration. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted.

**Platforms:** Android

---

### AndroidInitServiceRemoved

**Description:** An event that indicates that an init (boot) service has been removed from the system configuration. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted.

**Platforms:** Android

---

### AndroidIntentSentIPC

**Description:** This event is sent when an Android Intent is fired from the container

**Platforms:** Android

---

### AndroidManifestFragmentData

**Description:** An event that's sent by the sensor along with AndroidManifestXmlUploaded that contains a logical portion of AndroidManifest encoded as JSON after a process is installed or after it is opened.

**Platforms:** Android

---

### AndroidManifestXmlUploaded

**Description:** An event that indicates the LFO upload of the AndroidManifest of an android application package was successful and maps the package name to the upload ID.

**Platforms:** Android

---

### AndroidModuleStateUpdate

**Description:** Status information of modules for the Android sensor. AndroidModuleId lists available modules.

**Platforms:** Android

---

### APKMetadata

**Description:** Sent from mobile sensor in PlayStore mode when a new APK file is present on the device, as a result of an installation or an update

**Platforms:** Android

---

### AppleScriptFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### AppProtocolDetected

**Description:** 

**Platforms:** macOS

---

### AppSideLoaded

**Description:** An event that contains the package name and installer info of the app that has been installed outside of the Google PlayStore.

**Platforms:** Android

---

### AppUninstalled

**Description:** An event that contains information about an app that has been uninstalled from the device.

**Platforms:** Android

---

### ArcFileWritten

**Description:** Emitted when a process is done writing a ARC file.

**Platforms:** Linux, Windows, macOS

---

### ArchiveFileContent

**Description:** 

**Platforms:** macOS, Windows

---

### ArchiveInfo

**Description:** Archive file information.

**Platforms:** Forensics

---

### ArchiveMemberInfo

**Description:** Archive member file information.

**Platforms:** Forensics

---

### ArjFileWritten

**Description:** Emitted when a process is done writing a ARJ file.

**Platforms:** Windows, macOS, Linux

---

### AsepFileChangeDetectInfo

**Description:** Rollup indicating an ASEP file has been created or modified and there was a template detection on the contents.

**Platforms:** macOS

---

### AsepFileChangeScanInfo

**Description:** Rollup indicating an ASEP file has been created or modified but there was no template detection on the contents.

**Platforms:** macOS

---

### AsepKeyUpdate

**Description:** Generated when an Auto Start Execution Point registry key is updated.

**Platforms:** Windows

---

### AsepValueUpdate

**Description:** This event is generated when a Microsoft Auto Start Execution Point registry key has been updated.

**Platforms:** Windows

---

### AsifFileWritten

**Description:** 

**Platforms:** macOS

---

### ASLRBypassAttempt

**Description:** Emitted when a process that applied ForceASLR to a module detects an invalid execution attempt. This should only happen during an exploit, when the initial ROP chain is designed to defeat ASLR. In the case of a typical ALSR bypass attempt (trying to utilize code in a rebased image as part of a ROP chain), TargetAddress and ExceptionAddress will likely be identical, as will ImageFileName and SourceFileName.

**Platforms:** Windows

---

### AspmCollectionStatusUpdate

**Description:** 

**Platforms:** Linux

---

### AssociateIndicator

**Description:** This event is generated when the sensor generates an indicator. An indicator is like a detection event (AssociateTreeIdWithRoot) except that it is not necessarily malicious, either because it is just an indicator (e.g. when a process opens the Recycle Bin) or because CrowdStrike is not yet confident enough in the indicator to trigger it as a detection. Note that a detection, unlike an indicator, establishes a detection tree (AssociateTreeIdWithRoot) which causes the sensor to send additional information for that process tree for analysis/hunting purposes. An indicator is just a single event that has no other sensor impact.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### AssociateTreeIdWithRoot

**Description:** This event is generated when there is a detection in the sensor. This event has a data field called PatternId that contains a pattern ID. Pattern IDs correspond to a detection.

**Platforms:** Windows, Windows Legacy, macOS, Linux, Falcon Container

---

### AtJobInfo

**Description:** Windows At jobs in use.

**Platforms:** Forensics

---

### AuditCveKmEtw

**Description:** An event that indicates that a driver or the kernel reported a known CVE (Common Vulnerabilities and Exposures id). Captured using the ETW consumer.

**Platforms:** Windows

---

### AuditCveUmEtw

**Description:** An event that indicates that an application reported a known CVE (Common Vulnerabilities and Exposures id). Captured using the ETW consumer.

**Platforms:** Windows

---

### AutoRunProcessInfo

**Description:** Describes a process that is automatically executed.

**Platforms:** Forensics

---

### AwsEc2Image

**Description:** This event provides key metadata regarding images (AMIs, AKIs, and ARIs) available in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeImages API on your behalf. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Instance

**Description:** This event provides key metadata regarding EC2 instances in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeInstances API on your behalf. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkAcl

**Description:** Platforms: Public Cloud

**Platforms:** Windows

---

### AwsEc2NetworkAclEntry

**Description:** Information from AWS API call DescribeNetworkAcls.

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkInterface

**Description:** This event provides key metadata regarding network interfaces in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeNetworkInterfaces API on your behalf. Network interfaces can either be in detached or attached state. When attached, they have an associated EC2 instance ID which can be used to correlate between the two events. Note that multiple network interface objects can also be associated to a single EC2 instance. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2NetworkInterfacePrivateIP

**Description:** This event provides key metadata regarding private IP addresses in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeNetworkInterfaces API on your behalf. Multiple private IPs can be assigned to a single network interface. The AwsNetworkInterfaceId field can be used to correlate these private IPs to the associated AwsEc2NetworkInterface event. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2SecurityGroup

**Description:** This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSecurityGroups API on your behalf. Security groups control the level of network based access to resources within a VPC and can typically associated to network interfaces and their attached EC2 instances. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2SecurityGroupRule

**Description:** This event provides key metadata regarding security groups in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSecurityGroups API on your behalf. Each event represents a specific rule/ACL defined within a security group and are associated based on the AwsGroupId field. Rules represent the actual logic or ACL applied to the group. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Subnet

**Description:** This event provides key metadata regarding subnets configured in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeSubnets API on your behalf. Subnets represent a level of network segmentation and are created within a VPC to control and manage routing configurations. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Volume

**Description:** This event provides key metadata regarding EBS volumes configured in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeVolumes API on your behalf. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsEc2Vpc

**Description:** This event provides key metadata regarding virtual private clouds (VPCs) configured in AWS. CrowdStrike retrieves this information by processing the response from AWS's DescribeVpcs API on your behalf. This event is only generated for Discover for AWS customers. It's generated either when Discover for AWS observes new or related activity via CloudTrail or during Discover for AWS's weekly full scan.

**Platforms:** Windows, Public Cloud

---

### AwsIamAccountAlias

**Description:** Information from AWS API call ListAccountAliases.

**Platforms:** Windows, Public Cloud

---

### AzureApplicationFirewallRule

**Description:** An event that contains firewall rules for https traffic or Azure SQL traffic.

**Platforms:** Public Cloud

---

### AzureDisk

**Description:** An event that contains a list of Azure disks and their attributes.

**Platforms:** Public Cloud

---

### AzureFirewall

**Description:** An event that contains information about Azure cloud-based network security service.

**Platforms:** Public Cloud

---

### AzureFirewallRuleCollection

**Description:** An event that contains Azure firewall rule collections for application, NAT (network address translation) and network firewall rules.

**Platforms:** Public Cloud

---

### AzureIpConfiguration

**Description:** An event that contains a list of Azure IP configurations and attributes of the Azure IP configurations.

**Platforms:** Public Cloud

---

### AzureNatFirewallRule

**Description:** An event that contains Azure firewall rules for LAN.

**Platforms:** Public Cloud

---

### AzureNetworkFirewallRule

**Description:** An event that contains Azure network filtering rules.

**Platforms:** Public Cloud

---

### AzureNetworkInterface

**Description:** An event that contains a list of Azure network interfaces and the Azure network interface attributes.

**Platforms:** Public Cloud

---

### AzureNetworkSecurityGroup

**Description:** An event that contains information about an Azure Network Security Group.

**Platforms:** Public Cloud

---

### AzureNetworkSecurityGroupRule

**Description:** An event that contains Azure security rules in the specified network security group.

**Platforms:** Public Cloud

---

### AzurePrivateEndpoint

**Description:** An event that connects Azure Network interface to other services with private links.

**Platforms:** Public Cloud

---

### AzurePublicIpAddress

**Description:** An event that contains Azure public IP addresses.

**Platforms:** Public Cloud

---

### AzureResourceGroup

**Description:** An event that contains a list of Azure Resource Groups.

**Platforms:** Public Cloud

---

### AzureSubnet

**Description:** An event that contains Azure sub-networks in the virtual network.

**Platforms:** Public Cloud

---

### AzureSubscription

**Description:** An event that contains a list of Azure subscriptions.

**Platforms:** Public Cloud

---

### AzureVirtualMachine

**Description:** An event that contains a list of Azure virtual machines and the Azure virtual machine attributes.

**Platforms:** Public Cloud

---

### AzureVirtualMachineState

**Description:** An event that contains the machine state for any Azure virtual machine.

**Platforms:** Public Cloud

---

### AzureVirtualNetwork

**Description:** An event that contains a list of the Azure virtual networks and the Azure virtual network attributes.

**Platforms:** Public Cloud

---

### AzureVirtualNetworkPeering

**Description:** An event that contains a list of the Azure virtual networks and the Azure virtual network attributes.

**Platforms:** Public Cloud

---

### BamRegAppRunTime

**Description:** Recent program execution timeline from Background Activity Moderator (BAM) system service registry. BAM key is written on system shutdown.

**Platforms:** Forensics

---

### Base64PeFileWritten

**Description:** 

**Platforms:** Windows

---

### BcmFileWritten

**Description:** 

**Platforms:** Windows

---

### BehaviorWhitelisted

**Description:** Indicates that a behavior has been whitelisted.

**Platforms:** Linux, macOS, Windows

---

### BillingInfo

**Description:** Sensor sends this event to inform the cloud about the sensor billing type. Platforms: macOS

**Platforms:** Linux, Falcon Container, Windows

---

### BITSJobCreated

**Description:** The event is generated when a Background Intelligent Transfer Service (BITS) download is created and a new file is dropped on the system.

**Platforms:** Windows

---

### BITSJobFileInfo

**Description:** Background Intelligent Transfer Service (BITS) job file information.

**Platforms:** Forensics

---

### BITSJobInfo

**Description:** Background Intelligent Transfer Service (BITS) job information.

**Platforms:** Forensics

---

### BITSJobMetadata

**Description:** Background Intelligent Transfer Service (BITS) job metadata: times, proxy.

**Platforms:** Forensics

---

### BlakHoleFileWritten

**Description:** 

**Platforms:** Windows

---

### BlfFileWritten

**Description:** Emitted when a process is done writing an BLF file.

**Platforms:** Windows, macOS, Linux

---

### BlockThreadFailed

**Description:** A block thread request failed.

**Platforms:** Windows

---

### BMLFeatureData

**Description:** 

**Platforms:** Linux, Falcon Container, Windows, macOS

---

### BmpFileWritten

**Description:** Emitted when a process is done writing a BMP image file.

**Platforms:** macOS, Linux, Windows

---

### BootLoaderStatus

**Description:** An event that contains info about the device's bootloader.

**Platforms:** Android

---

### BootLoopProtectionTelemetry

**Description:** 

**Platforms:** Windows

---

### BPFCommandIssued

**Description:** Emitted when a process executes bpf syscall.

**Platforms:** Linux, Falcon Container

---

### BrotliFileWritten

**Description:** 

**Platforms:** Windows

---

### BrowserAccountInfo

**Description:** Browser user account information.

**Platforms:** Forensics

---

### BrowserCookieInfo

**Description:** Browser tracking cookie information.

**Platforms:** Forensics

---

### BrowserDownloadEnded

**Description:** Browser downloaded file information signifying download end time.

**Platforms:** Forensics

---

### BrowserDownloadStarted

**Description:** Browser downloaded file information signifying download start time.

**Platforms:** Forensics

---

### BrowserExtensionInfo

**Description:** Browser extension/addon information.

**Platforms:** Forensics

---

### BrowserExtensionStatus

**Description:** 

**Platforms:** macOS

---

### BrowserHistoryClearInfo

**Description:** Browser history clearing event information.

**Platforms:** Forensics

---

### BrowserHistoryVisit

**Description:** Browser history hit information.

**Platforms:** Forensics

---

### BrowserInjectedThread

**Description:** Indicates a browser process injected a thread into some other process.

**Platforms:** Windows

---

### BrowserProxyInfo

**Description:** Browser proxy information.

**Platforms:** Forensics

---

### BZip2FileWritten

**Description:** Emitted when a process is done writing a BZip2 file.

**Platforms:** macOS, Windows, Linux

---

### CabFileWritten

**Description:** Emitted when a process is done writing a Microsoft Cabinet (CAB) file.

**Platforms:** Windows, Linux, macOS

---

### CertificatePinningCompromised

**Description:** An event that indicates that the certificate pinning methods/functions on the device have been tampered with and cannot be trusted. For further details, see the following associated events: ObjCRuntimeAltered or TrampolineDetected.

**Platforms:** iOS

---

### ChannelActive

**Description:** 

**Platforms:** Windows

---

### ChannelDataDownloadComplete

**Description:** Sent by LFODownloadActor when a new channel data file has been downloaded. Platforms: iOS, Kubernetes Platforms: Vmcluster

**Platforms:** Windows, Linux, Falcon Container, Android, macOS

---

### ChannelVersionRequired

**Description:** This event informs the cloud information about the state of a channel on the sensor. The cloud will use this event to decide whether to send the sensor updated channel data. Platforms: Vmcluster, iOS Platforms: Kubernetes

**Platforms:** Windows, macOS, Linux, Falcon Container, Android

---

### CidMigrationComplete

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### CidMigrationConfirmation

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### CidMigrationError

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### CidMigrationManifestDownloadComplete

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### ClassifiedModuleLoad

**Description:** The ClassifiedModuleLoad event provides information about a module which has been loaded into a process's memory space. It is only generated for 'classified' module loads, that is module loads that are interesting enough for us to cloud.

**Platforms:** Windows

---

### ClassifiedProcessStart

**Description:** 

**Platforms:** Windows

---

### ClassifiedSensitiveFileAccess

**Description:** 

**Platforms:** Windows

---

### ClipboardCopy

**Description:** Sent when content is copied to the clipboard.

**Platforms:** Android, iOS

---

### ClipboardPaste

**Description:** Sent when content is pasted from the clipboard.

**Platforms:** Android

---

### CloudAssociateTreeIdWithRoot

**Description:** This event is generated when there is a detection in the CrowdStrike cloud. This event has a data field called PatternId which contains a pattern ID. Pattern IDs are associated with a detection.

**Platforms:** Windows, Linux, Falcon Container, macOS, ChromeOS

---

### CloudScanControl

**Description:** A event to that notifies downstream services of completed tasks.

**Platforms:** Public Cloud

---

### CodeSigningAltered

**Description:** An event that indicates the code signing flags of the current application have unexpected flags or are missing expected ones.

**Platforms:** iOS

---

### CommandHistory

**Description:** This event includes the full command history associated with one of the consoles in a process that has recently terminated (identified by the TargetProcessId). Note that a given UPID may be associated with multiple consoles (identified by ApplicationName).

**Platforms:** Windows

---

### CommsLogReset

**Description:** Sent by Communications indicating that the CommsLog was flushed due to invalid data

**Platforms:** macOS

---

### ConfigDownloadComplete

**Description:** Sent by LFODownloadActor when a new binary configuration has been downloaded as part of a configuration update. Platforms: Vmcluster Platforms: Kubernetes

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ConfigStateUpdate

**Description:** Sent periodically and when dynamic config is updated. Analysts can find out which config was active using this event with ConfigStateHash. You may have to reason about what a particular hash really means for a particular event at a given point in time, particularly if the hash has recently changed. Platforms: Vmcluster, Windows Legacy Platforms: Android, Kubernetes, iOS

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### ConfigurationLoaded

**Description:** Thrown when a new configuration has been successfully loaded but before any Event Sources are started.

**Platforms:** iOS, Android

---

### ConfigurationProfileModified

**Description:** 

**Platforms:** macOS

---

### ConfigurationProvisioningState

**Description:** 

**Platforms:** Linux

---

### ContainerizationUpdate

**Description:** Sent following an LFODownload of a new APK to be installed or updated in the container, containing response information for the operation.

**Platforms:** Android

---

### CrashNotification

**Description:** The sensor sends this to the cloud when the Diagnostics Actor notices that the machine has booted with indication of previous session ending in a crash.

**Platforms:** Windows, macOS

---

### CreateProcessArgs

**Description:** Full command line argument corresponding to a process creation.

**Platforms:** macOS

---

### CreateService

**Description:** Generated when a Windows service is created.

**Platforms:** Windows

---

### CreateSocket

**Description:** This event is created whenever a process creates a socket.

**Platforms:** Forensics, Linux, Falcon Container

---

### CreateThreadKernelNoStartImage

**Description:** Emitted when a new system thread is created outside of a loaded driver.

**Platforms:** Windows

---

### CreateThreadNoStartImage

**Description:** This event is used to indicate the target start address of a CreateThread attempt is not within the limits of a loaded module. This could indicate the presence of shellcode, or other dynamically allocated code regions.

**Platforms:** Windows

---

### CreateThreadReflectiveDll

**Description:** This event is used to indicate the presence of a reflectively loaded dll in the callstack for a CreateThread attempt.

**Platforms:** Windows

---

### CriticalEnvironmentVariableChanged

**Description:** A process set a critical environment variable.

**Platforms:** Linux, Falcon Container

---

### CriticalFileAccessed

**Description:** A critical file was accessed. Platforms: ChromeOS

**Platforms:** Linux, Falcon Container, macOS

---

### CriticalFileModified

**Description:** A critical file was modified. Platforms: ChromeOS

**Platforms:** Linux, Falcon Container, macOS

---

### CrxFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### CSAResultsGenericDetectInfo

**Description:** 

**Platforms:** Windows

---

### CsKmCrashSummaryEvent

**Description:** 

**Platforms:** Windows

---

### CsUmProcessCrashAuxiliaryEvent

**Description:** An event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field, one per thread.

**Platforms:** Windows

---

### CsUmProcessCrashSummaryEvent

**Description:** A event that is emitted when a CrowdStrike process crashes which helps diagnose issues in the field.

**Platforms:** Windows

---

### CurrentSystemTags

**Description:** This event is sent from the sensor to inform the cloud about the system tag state. Platforms: Vmcluster, Windows Legacy

**Platforms:** macOS, Linux, Falcon Container, iOS, Android, Windows, Kubernetes

---

### CustomIOABasicProcessDetectionInfoEvent

**Description:** An event triggered by a Process Creation custom IOA rule.

**Platforms:** Linux, Falcon Container, Windows, macOS

---

### CustomIOADomainNameDetectionInfoEvent

**Description:** Platforms: Windows An event triggered by a Domain Name custom IOA rule.

**Platforms:** Linux, macOS

---

### CustomIOAFileWrittenDetectionInfoEvent

**Description:** An event triggered by a File Creation custom IOA rule.

**Platforms:** Windows, macOS, Linux

---

### CustomIOANetworkConnectionDetectionInfoEvent

**Description:** An event triggered by a Network Connection custom IOA rule. Platforms: Linux

**Platforms:** macOS, Windows

---

### DataEgress

**Description:** Description of a data egress observed on the sensor.

**Platforms:** macOS, Windows

---

### DataProtectionArchiveAssessed

**Description:** Describes an archive processed by Data Protection assessment. Top level event fields are properties of enclosing archive file (e.g. Size)

**Platforms:** Windows, macOS

---

### DataProtectionBrowserConnect

**Description:** 

**Platforms:** Windows, macOS

---

### DataProtectionDataEncryption

**Description:** 

**Platforms:** Windows

---

### DataProtectionPACDiagnostic

**Description:** 

**Platforms:** Windows

---

### DBusMessage

**Description:** An event that generates telemetry that provides visibility into D-Bus messages flowing over local Unix sockets between processes. The sensor will produce events for each message and apply any relevant detections.

**Platforms:** Linux

---

### DcBluetoothAuthorizationStatus

**Description:** 

**Platforms:** macOS

---

### DcBluetoothDeviceBlocked

**Description:** 

**Platforms:** macOS

---

### DcBluetoothDeviceConnected

**Description:** This event represents a connected Bluetooth device. Platforms: macOS

**Platforms:** Windows

---

### DcBluetoothDeviceConnectedDetails

**Description:** 

**Platforms:** macOS, Windows

---

### DcBluetoothDeviceDisconnected

**Description:** Platforms: Windows This event represents a disconnected Bluetooth device.

**Platforms:** macOS

---

### DcBluetoothDevicePolicyViolation

**Description:** 

**Platforms:** macOS

---

### DcBluetoothDeviceProperties

**Description:** This event contains properties for a connected Bluetooth device. Platforms: macOS

**Platforms:** Windows

---

### DcIdentification

**Description:** This event enables monitoring of domain controllers (DCs) and the passing of identifying information to the CrowdStrike Cloud.

**Platforms:** Windows

---

### DcOffline

**Description:** An event that indicates the Device Control plug-and-play driver interface has gone offline. It is sent each time the sensor disconnects from the Device Control interface.

**Platforms:** Windows, macOS, Linux

---

### DcOnline

**Description:** An event that indicates the Device Control plug-and-play driver interface has come online. It is sent each time the sensor connects to the Device Control interface.

**Platforms:** macOS, Linux, Windows

---

### DcRemovableStorageDeviceBlocked

**Description:** 

**Platforms:** Windows, macOS

---

### DcRemovableStorageDeviceConnected

**Description:** 

**Platforms:** Windows, macOS

---

### DcRemovableStorageDeviceDisconnected

**Description:** 

**Platforms:** macOS, Windows

---

### DcRemovableStorageDevicePolicyViolation

**Description:** 

**Platforms:** Windows, macOS

---

### DcStatus

**Description:** An event that contains the status information for the Device Control plug-and-play driver. It is sent once per day after it has successfully connected to the Device Control interface.

**Platforms:** Windows, macOS, Linux

---

### DCSyncAttempted

**Description:** Directory Services changes were replicated. If the source host is not a Domain Controller, this could represent malicious activity.

**Platforms:** Windows

---

### DcUsbConfigurationDescriptor

**Description:** An event that describes a configuration descriptor extracted from the firmware of a USB device. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** macOS, Linux, Windows

---

### DcUsbDeviceBlocked

**Description:** An event that indicates a USB device that was blocked by a policy.

**Platforms:** Linux, macOS, Windows

---

### DcUsbDeviceConnected

**Description:** An event that describes a connected USB device to which Device Control is attached. It is sent each time the system powers on, the associated hub/port is power cycled, or the device is physically inserted into the system.

**Platforms:** Linux, macOS, Windows

---

### DcUsbDeviceDisconnected

**Description:** An event that describes a disconnected USB device to which Device Control has previously attached. It is sent each time the system powers off, the associated hub/port is power cycled, or the device is physically removed from the system.

**Platforms:** Linux, macOS, Windows

---

### DcUsbDevicePolicyViolation

**Description:** An event that indicates a USB device that matched a rule in a policy but was not blocked due to the rule being set to reporting mode only.

**Platforms:** macOS, Linux, Windows

---

### DcUsbDeviceWhitelisted

**Description:** An event that indicates a USB device was added to an allowlist by a Device Control policy. The Device Control plug-and-play driver did not attach to the device as a result of an allowlist policy rule.

**Platforms:** Windows, macOS, Linux

---

### DcUsbEndpointDescriptor

**Description:** An event that describes an endpoint descriptor extracted from the firmware of a USB device. An interface descriptor typically defines 2 or more endpoints that are used for data transfer. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** macOS, Linux, Windows

---

### DcUsbHIDDescriptor

**Description:** This event describes a HID (Human Interface Device) descriptor extracted from the firmware of a USB device. A HID descriptor is a container for a complex set of sub-descriptors that identify the capabilities of a HID device. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** macOS, Linux, Windows

---

### DcUsbInterfaceDescriptor

**Description:** An event that describes an interface descriptor extracted from the firmware of a USB device. There are typically multiple interface descriptors for a given configuration descriptor, with each interface exposing a device capability. This event is sent one time when the first device containing this descriptor is seen and every seven days.

**Platforms:** macOS, Linux, Windows

---

### DeactivateMobileSensorResponse

**Description:** Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. Platforms: Android Sent as confirmation by a Falcon Mobile sensor that it was reset and inactive. On Android, container apps and data have been wiped from the device. Complete deactivation of the sensor, including all current and future cloud connections, will follow shortly after.

**Platforms:** iOS

---

### DebFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### DebuggableFlagTurnedOn

**Description:** An event that indicates a debuggable flag has been turned on for a non-dev build of an app.

**Platforms:** Android

---

### DebuggedState

**Description:** An event that indicates a process is in the state of being debugged (i.e., has a debugger attached to it.)

**Platforms:** iOS

---

### DeliverLocalFXToCloud

**Description:** DeliverLocalFXToCloud conveys feature extraction (FX) data to the cloud from the sensor. Platforms: Linux `DeliverLocalFXToCloud` conveys feature extraction (FX) data to the cloud from the sensor.

**Platforms:** macOS, Windows

---

### DeliverRulesEngineResultsToCloud

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### DetectionExcluded

**Description:** This event indicates that a detection has been excluded, either by customer exclusions or by CrowdStrike.

**Platforms:** macOS, Linux, Falcon Container, Windows, iOS, Android

---

### DeveloperOptionsStatus

**Description:** An event that contains info about developer-related settings on the device. Platforms: iOS

**Platforms:** Android

---

### DexFileWritten

**Description:** Emitted when a file has been written that contains a real Dex image header.

**Platforms:** Android

---

### DirectoryCreate

**Description:** This event is generated when a process creates a new folder. Platforms: Linux

**Platforms:** Windows, macOS

---

### DirectoryTraversalOverSMB

**Description:** This event indicates Directory traversal over an SMB session detected.

**Platforms:** Windows

---

### DiskCapacity

**Description:** An event that contains information about disks, the quantity of disks, and the storage capability of disks that are locally attached to a system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in disk parameters is detected. Platforms: Windows An event that contains information about disks, the quantity of disks, and the storage capability of disks. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in disk parameters is detected.

**Platforms:** Linux

---

### DiskUtilization

**Description:** An event that contains the used and available storage space for each mounted logical drive or volume that has an underlying physical disk locally attached to the system. The event is sent when the sensor connects and every 12 hours thereafter. Platforms: Forensics

**Platforms:** Linux

---

### DllInjection

**Description:** This event indicates that DLL injection occurred in the target process.

**Platforms:** Windows

---

### DmgFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### DmpFileWritten

**Description:** Emitted when a process is done writing a dump file. PidFromCommandLine will be enhanced in some cases to extract out the pid from the commandline of the writing process if possible.

**Platforms:** Windows, Linux, macOS

---

### DnsCache

**Description:** An entry observed within the system's DNS Cache.

**Platforms:** Forensics

---

### DnsRequest

**Description:** When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. Platforms: iOS When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. Platforms: macOS When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. On Mac the data is deduplicated just on DomainName. The sensor clears deduplication entries every 24 hrs after the first DnsRequest for the specific process is received. Platforms: Linux, Windows When a process on a host generates a DNS query, the sensor waits for the response, to generate a DnsRequest that contains the queried domain and information returned in the response such as IP-addresses. On Win/Lin sensor the data is deduplicated based on DomainName, IP4, IP6 and CNAME. Meaning if multiple requests are made that have responses containing different IP addresses for a single domain, they will all be visible. The sensor clears deduplication entries every 24 hrs after the first DnsRequest for the specific process is received.

**Platforms:** Android

---

### DnsRequestBlocked

**Description:** This event is sent whenever a DnsRequest is blocked. Connection to either the IP or the domain in this request has been blocked.

**Platforms:** Android, iOS

---

### DNSRequestDetectInfo

**Description:** This event is sent whenever a malicious DnsRequest is detected. Platforms: Linux

**Platforms:** iOS, Android

---

### DnsRequestResult

**Description:** An event that contains DNS request results after a DNS request.

**Platforms:** Android, iOS

---

### DnsServer

**Description:** DNS server IP addresses.

**Platforms:** Forensics

---

### DnsServerSigRedExploitAttemptEtw

**Description:** 

**Platforms:** Windows

---

### DocumentProgramInjectedThread

**Description:** Indicates a document program process injected a thread into some other process.

**Platforms:** Windows

---

### DotnetModuleLoadDetectInfo

**Description:** 

**Platforms:** Windows

---

### DriverLoad

**Description:** An event to notify of a driver load that will be used for detection.

**Platforms:** Forensics, Windows

---

### DriverLoadBlocked

**Description:** Event which indicates we successfully blocked a driver from loading.

**Platforms:** Windows

---

### DriverLoadedV2DetectInfo

**Description:** 

**Platforms:** Windows

---

### DriverPreventFailed

**Description:** Event which indicates we failed (or timed out) attempting to block a driver load.

**Platforms:** Windows

---

### DriverPreventionStatus

**Description:** 

**Platforms:** Windows

---

### DuplicateInstallFromPlayStore

**Description:** An event that indicates a containerized app is also installed outside the container.

**Platforms:** Android

---

### DwgFileWritten

**Description:** An event that is emitted when a process is done writing to a DWG file.

**Platforms:** Windows

---

### DwmCompositionResourceExploitAttempt

**Description:** 

**Platforms:** Windows

---

### DxfFileWritten

**Description:** 

**Platforms:** Windows

---

### EarlyExploitPivotDetect

**Description:** Telemetry event indicating execution pivoting in an unusual way. Could be indicative of malicious code.

**Platforms:** Windows

---

### ECBDownloadComplete

**Description:** Sent by LFODownloadActor when a new ECB module has been downloaded as part of a configuration update.

**Platforms:** Windows, Linux, macOS

---

### EddScanStart

**Description:** Sent by sensor to indicate the start of a new EDD scan run. Note: This event is currently not supported in macOS. Platforms: Windows Sent by sensor to indicate the start of a new EDD scan run.

**Platforms:** macOS

---

### EddScanStatus

**Description:** Sent by sensor periodically to report the status of an on-going scan. Platforms: macOS Sent by sensor periodically to report the status of an on-going scan. Note: This event is currently not supported in macOS.

**Platforms:** Windows

---

### EksCluster

**Description:** Snapshot of an AWS EKS cluster.

**Platforms:** Public Cloud

---

### EksFargateProfile

**Description:** Snapshot of an AWS EKS Fargate profile.

**Platforms:** Public Cloud

---

### EksNodeGroup

**Description:** Snapshot of an AWS EKS node group.

**Platforms:** Public Cloud

---

### ELFFileWritten

**Description:** Emitted when a file has been written that contains a real ELF image header.

**Platforms:** Android, macOS, Linux, Windows

---

### EmailArchiveFileWritten

**Description:** 

**Platforms:** macOS

---

### EmailFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### EndOfProcess

**Description:** When a process that’s running on a host finishes, the sensor will count all of the events that were generated by that process, bundle the information in an EndOfProcess event, and send it to the cloud. This allows you to determine, for example, how many DNS requests a process made, how many directory creation events occurred, or how many network connections a process made.

**Platforms:** Linux, Falcon Container, macOS, Windows

---

### EntropyScan

**Description:** File contents entropy, useful for identifying potentially malicious files.

**Platforms:** Forensics

---

### ErrorEvent

**Description:** Event indicating a sensor error. Platforms: Kubernetes Platforms: Vmcluster

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### EseFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### EtwComponentResponse

**Description:** Event sent in when EtwComponent has initialized. AttemptNumber is no longer used.

**Platforms:** Windows

---

### EtwErrorEvent

**Description:** An event that indicates that an error occurred which associated is with the ETW consumer.

**Platforms:** Windows

---

### EventLogCleared

**Description:** This event is generated when a Windows event log is cleared.

**Platforms:** Windows

---

### EventTapInfo

**Description:** Describes a macOS Event Tap. Event Taps allow for capturing of keyboard and mouse HID events.

**Platforms:** Forensics

---

### ExcelDocumentOpened

**Description:** 

**Platforms:** Windows

---

### ExecutableDeleted

**Description:** This event indicates that an executable was deleted from the host. Platforms: Linux

**Platforms:** Windows, macOS

---

### ExtendedExploitMitigationViolatedDetectInfo

**Description:** 

**Platforms:** Windows

---

### FalconHostFileTamperingInfo

**Description:** An event that describes the file event that triggered a Falcon sensor tampering indicator.

**Platforms:** Windows

---

### FalconHostRegTamperingInfo

**Description:** An event that describes the registry event that triggered a Falcon sensor tampering indicator.

**Platforms:** Windows

---

### FalconProcessHandleOpDetectInfo

**Description:** 

**Platforms:** Windows

---

### FalconServiceStatus

**Description:** A message from CsFalconService regarding the service and its servlets' lifecycle events.

**Platforms:** Windows

---

### FfcBytePatternScanResult

**Description:** Describes a scanning result performed by the Falcon Forensics Collector.

**Platforms:** Forensics

---

### FileAccessOperationOverSMB

**Description:** File access operations over a SMB user session.

**Platforms:** Windows

---

### FileContentsChanged

**Description:** 

**Platforms:** Linux

---

### FileCreateInfo

**Description:** This event is generated when a file is created by a process.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### FileDeleted

**Description:** This event has been deprecated as of Falcon Sensor for Windows 4.16.7903, and Falcon Sensor for Mac 4.16.7801. Older sensors and existing data for these events will still appear, but new sensors utilize the FileOpenInfo event. This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event. Platforms: Android This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event. Platforms: Forensics File entry from a file observed in the recycle bin.

**Platforms:** Windows

---

### FileDeleteInfo

**Description:** This event is generated when a file deletion for a full file occurs. ADS deletions are not currently tracked with this event.

**Platforms:** Windows, macOS, Linux

---

### FileDescriptorMonitor

**Description:** 

**Platforms:** Forensics

---

### FileDetectInfo

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### FileEntry

**Description:** Some portion of a text file, either a single line or matched regular expression.

**Platforms:** Forensics

---

### FileExtendedAttrOperation

**Description:** 

**Platforms:** macOS

---

### FileHashesEvent

**Description:** 

**Platforms:** Forensics

---

### FileInfo

**Description:** Error event for FileInfo response. Platforms: macOS FileInfo response with information about a file.

**Platforms:** Forensics

---

### FileIntegrityMonitorRuleMatched

**Description:** An event that contains data about a change to a directory, file, or registry key. Used with the FileVantage service. Platforms: macOS

**Platforms:** Windows, Linux

---

### FileOfInterestBasicInfo

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### FileOpenInfo

**Description:** This event is generated when a file is opened by a process.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### FileRenameInfo

**Description:** This event is generated when a file is renamed. Only sent as part of a detection.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### FileSetMode

**Description:** Indicates the file permissions have been modified via chmod/fchmod/fchmodat.

**Platforms:** Linux, Falcon Container

---

### FileSignatureMismatch

**Description:** On-demand scan for files with name extensions and header magic values.

**Platforms:** Forensics

---

### FileSignatureStatistics

**Description:** On-demand scan for files with name extensions and header magic values.

**Platforms:** Forensics

---

### FilesStatisticInfo

**Description:** Files statistic information.

**Platforms:** Forensics

---

### FileStatFsInfo

**Description:** 

**Platforms:** Linux

---

### FileSystemAttributesStatus

**Description:** An event that contains info about the Filesystem attributes of the device.

**Platforms:** iOS

---

### FileSystemContainmentStatus

**Description:** 

**Platforms:** Windows

---

### FileSystemOperationBlocked

**Description:** An event that indicates that a file system operation has been blocked. Platforms: macOS

**Platforms:** Windows

---

### FileSystemOperationDetectInfo

**Description:** Informational event for a file system operation detection.

**Platforms:** Windows

---

### FileTimestampMetadata

**Description:** FileTime event is emitted per timestamp for a given file. This helps analysts build a timeline of file creation, access, and modification.

**Platforms:** Forensics

---

### FileTimestampsModified

**Description:** An event that is emitted when a change occurs to the timestamps of a file.

**Platforms:** Windows

---

### FileVaultStatus

**Description:** Contains information regarding the system FileVault (encrypted) state.

**Platforms:** macOS

---

### FileWrittenAndExecutedInContainer

**Description:** A file was written and later executed in a container.

**Platforms:** Linux, Falcon Container

---

### FileWrittenWithEntropyHigh

**Description:** 

**Platforms:** Windows, Linux

---

### FirewallChangeOption

**Description:** A firewall configuration option has been changed, such as enabling or disabling the firewall. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### FirewallDeleteRule

**Description:** A firewall rule has been deleted, such as removing a rule preventing inbound RDP connections. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### FirewallDeleteRuleIP4

**Description:** An event that notifies that an Ipv4 firewall rule has been deleted. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallDeleteRuleIP6

**Description:** An event that notifies that an Ipv6 firewall rule has been deleted. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallDisabled

**Description:** An event that is sent from the sensor when packet filter is disabled.

**Platforms:** macOS

---

### FirewallEnabled

**Description:** An event that is sent from the sensor when packet filter is enabled.

**Platforms:** macOS

---

### FirewallRuleApplicationFailed

**Description:** An event that indicates that the application of a firewall rule has failed. Platforms: macOS An event that indicates that the application of a firewall rule has failed. Platforms: Linux

**Platforms:** Windows

---

### FirewallRuleInfo

**Description:** 

**Platforms:** Forensics

---

### FirewallRuleIP4

**Description:** 

**Platforms:** Forensics

---

### FirewallRuleIP4Matched

**Description:** An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match. Platforms: Linux Platforms: macOS An event that indicates that a firewall rule has matched an IPv4 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match.

**Platforms:** Windows

---

### FirewallRuleIP6

**Description:** 

**Platforms:** Forensics

---

### FirewallRuleIP6Matched

**Description:** An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match. Platforms: Linux Platforms: Windows An event that indicates that a firewall rule has matched an IPv6 connection attempt. For situations where RuleMatchCountSinceLastReport > 1, the extra data, like process info, will be from only the most recent match.

**Platforms:** macOS

---

### FirewallSetRule

**Description:** A firewall rule has been created or modified, such as a rule allowing inbound RDP connections. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Windows

---

### FirewallSetRuleIP4

**Description:** An event that indicates an IPv4 firewall rule has been created. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirewallSetRuleIP6

**Description:** An event that indicates an IPv6 firewall rule has been created. The field 'IsUnique' will be TRUE if we are sending the rule due to a change which was detected while the sensor was running and will be FALSE if the sensor just started and we are sending all the rules.

**Platforms:** macOS

---

### FirmwareAnalysisErrorEvent

**Description:** Indicates an occurrence of error associated with the Firmware Analysis feature.

**Platforms:** macOS, Windows

---

### FirmwareAnalysisHardwareData

**Description:** This event contains hardware data collected by Firmware Analysis.

**Platforms:** macOS, Windows

---

### FirmwareAnalysisStatus

**Description:** This event contains status of the FPnP filter driver.

**Platforms:** macOS, Windows

---

### FirmwareImageAnalyzed

**Description:** Indicates that analysis of a firmware image was completed.

**Platforms:** macOS, Windows

---

### FirmwareRegionMeasured

**Description:** Indicates that a certain region of a firmware image was measured. Platforms: Windows

**Platforms:** macOS

---

### FlashThreadCreateProcess

**Description:** Thread associated with Flash activity created a process.

**Platforms:** macOS, Windows

---

### ForensicsCollectorLog

**Description:** A log entry emitted by the Falcon Forensics Collector process.

**Platforms:** Forensics

---

### ForensicsCollectorOffline

**Description:** Final event of a Forensics collection.

**Platforms:** Forensics

---

### ForensicsCollectorOnline

**Description:** Marks the beginning of a Forensics collection.

**Platforms:** Forensics

---

### FreeArcFileWritten

**Description:** 

**Platforms:** Windows

---

### FsPostCreate

**Description:** This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing data for these events will still appear, but new sensors utilize the FileCreateInfo event. This event is generated when a file is created by a process.

**Platforms:** Windows

---

### FsPostOpen

**Description:** This event has been deprecated as of Falcon Sensor for Windows 4.16.7903. Older sensors and existing data for these events will still appear, but new sensors utilize the FileOpenInfo event. This event is generated when a file is opened by a process. This event is only sent to the cloud for processes inside of a detection tree.

**Platforms:** Windows

---

### FsPostOpenSnapshotFile

**Description:** Information about a file opened on a snapshot volume.

**Platforms:** Windows

---

### FsPostOpenUpImpersonating

**Description:** A reified FsPostOpen event that occurred in the context of a thread up-impersonating another user, and the context process was not a privileged account.

**Platforms:** Windows

---

### FsVolumeMounted

**Description:** Provides information about a mounted volume. Platforms: Forensics

**Platforms:** Windows, macOS, iOS, Linux, Falcon Container

---

### FsVolumeReadInfo

**Description:** 

**Platforms:** Windows

---

### FsVolumeUnmounted

**Description:** Provides information about an unmounted volume.

**Platforms:** Windows, macOS, iOS, Linux, Falcon Container

---

### FtpCommand

**Description:** 

**Platforms:** Linux

---

### GcpAsset

**Description:** An event that contains GCP (Google Cloud Platform) Organization Metadata.

**Platforms:** Public Cloud

---

### GcpComputeDisk

**Description:** An event that contains GCP (Google Cloud Platform) Compute Disk Configuration details.

**Platforms:** Public Cloud

---

### GcpComputeFirewall

**Description:** An event that contains GCP (Google Cloud Platform) Compute Image configuration details.

**Platforms:** Public Cloud

---

### GcpComputeImage

**Description:** An event that contains GCP (Google Cloud Platform) Compute Image configuration details.

**Platforms:** Public Cloud

---

### GcpComputeInstance

**Description:** An event that contains GCP (Google Cloud Platform) Compute Instance configuration information.

**Platforms:** Public Cloud

---

### GcpComputeNetwork

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network configuration information.

**Platforms:** Public Cloud

---

### GcpComputeNetworkInterface

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network Interface configuration information.

**Platforms:** Public Cloud

---

### GcpComputeNetworkPeering

**Description:** An event that contains GCP (Google Cloud Platform) Compute Network Peering configuration details.

**Platforms:** Public Cloud

---

### GcpComputeSubnetwork

**Description:** An event that contains GCP (Google Cloud Platform) Compute Subnetwork configuration details.

**Platforms:** Public Cloud

---

### GcpIamServiceAccount

**Description:** An event that contains GCP (Google Cloud Platform) IAM Service Account configuration details.

**Platforms:** Public Cloud

---

### GcpProject

**Description:** An event that contains GCP (Google Cloud Platform) Project metadata.

**Platforms:** Public Cloud

---

### GenericFileWritten

**Description:** An event that is emitted when a process is done writing to a file that doesn't match a more specific *FileWritten event. These events are currently generated for removable disks only. Platforms: macOS An event that is emitted when a process is done writing to a file that doesn't match a more specific *FileWritten event. These events are currently generated for removable disks only.

**Platforms:** Windows

---

### GetAsyncKeyStateEtwBatch

**Description:** An event that indicates that an application called the GetAsyncKeyState API multiple times.

**Platforms:** Windows

---

### GifFileWritten

**Description:** Emitted when a process is done writing a GIF image file.

**Platforms:** Linux, Windows, macOS

---

### GroupAccount

**Description:** Describes an observed group account.

**Platforms:** Forensics

---

### GroupIdentity

**Description:** Provides the sensor boot unique mapping between GID, AuthenticationId, UserPrincipal, and UserSid. Platforms: Forensics

**Platforms:** macOS

---

### GzipFileWritten

**Description:** Emitted when a file has been written that contains a real Gzip image header.

**Platforms:** Linux, Windows, macOS

---

### HarmfulAppData

**Description:** An event that contains the name, hash, and category of the harmful app.

**Platforms:** Android

---

### HeapSprayAttempt

**Description:** Emitted when a process that had HeapSpray protections applied detects an invalid execution attempt.

**Platforms:** Windows

---

### HookedAndroidMethodFound

**Description:** An event that indicates that a hooking framework such as Xposed has been found to have been loaded by the FalconMobile application. The FalconMobile application might have been compromised and the device might have been rooted.

**Platforms:** Android

---

### HookedDriverObject

**Description:** This event describes the presence of a hooked pointer in a DRIVER_OBJECT structure.

**Platforms:** Windows

---

### HostedServiceStarted

**Description:** This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is started by the service control manager (SCM). ServiceDisplayName, TargetProcessId, ImageFileName and TargetThreadId are all for the new service. TargetThreadId is the primary thread of the new hosted service. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Also, starting and stopping hosted services multiple times during boot might not always show up in this event due to caching done by the SCM.

**Platforms:** Windows

---

### HostedServiceStatusInfo

**Description:** Status information includes loaded DLL for a hosted service.

**Platforms:** Forensics

---

### HostedServiceStopped

**Description:** This event is emitted when a hosted service (that is, a service inside a SvcHost.exe binary) is stopped by the service control manager (SCM). Unfortunately, the sensor is not currently capable of identifying who requested this operation. However, it can be used to confirm that this is a service stopping vs. a service crashing or being terminated. Also, starting and stopping hosted services multiple times during boot might not always show up in this event due to caching done by the SCM.

**Platforms:** Windows

---

### HostInfo

**Description:** This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This event provides information about the host running the sensor. When searching for information about a specific host, you should use the much faster aid_master search capability instead of searching for HostInfo events Platforms: iOS, macOS This event is generated when: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This event provides information about the host running the sensor. When searching for information about a specific host, you should use the much faster aid_master search capability instead of searching for HostInfo events Platforms: Windows Legacy

**Platforms:** Windows

---

### HostnameChanged

**Description:** Sent by the hostname awareness actor to communicate change in hostname. Platforms: macOS

**Platforms:** Linux, Falcon Container

---

### HostTimeModified

**Description:** 

**Platforms:** Linux, Falcon Container

---

### HttpRequest

**Description:** 

**Platforms:** macOS, Linux

---

### HttpRequestDetect

**Description:** An event that indicates a detection on an HTTP(S) request.

**Platforms:** Windows

---

### HttpRequestV2Detect

**Description:** 

**Platforms:** Windows

---

### HttpResponse

**Description:** 

**Platforms:** Linux, macOS

---

### HttpVisibilityStatus

**Description:** An event that indicates that the status of the HTTP Visibility event source has been updated.

**Platforms:** Windows

---

### IBEBChannelFileEnforcementResponse

**Description:** An event that sent installed browser extension blocking (IBEB) channel file policy enforcement response to cloud.

**Platforms:** macOS, Windows

---

### IdpCloudHealthCheck

**Description:** 

**Platforms:** Windows

---

### IdpCloudHealthConfigurationsGetResponse

**Description:** 

**Platforms:** Windows

---

### IdpCloudHealthConfigurationsSetResponse

**Description:** 

**Platforms:** Windows

---

### IdpCloudHealthStatus

**Description:** 

**Platforms:** Windows

---

### IdpConnectionsOverloadNotification

**Description:** IDP Traffic Inspection detected more than 15,000 concurrent connections in active enforcement mode.

**Platforms:** Windows

---

### IdpContainerRestarted

**Description:** 

**Platforms:** Windows

---

### IdpDcPerfReport

**Description:** This event reports Domain Controller performance counter.

**Platforms:** Windows

---

### IdpDcTiConfiguration

**Description:** 

**Platforms:** Windows

---

### IdpEntityRiskScoreChange

**Description:** 

**Platforms:** Public Cloud

---

### IdpIdaasCorrelate

**Description:** 

**Platforms:** Windows, macOS

---

### IdpPacketDiversionConnectionsOverloadNotification

**Description:** 

**Platforms:** Windows

---

### IdpPacketDiversionLdapsConnectionsOverloadNotification

**Description:** 

**Platforms:** Windows

---

### IdpPolicyAccessRuleMatch

**Description:** 

**Platforms:** Windows

---

### IdpPolicyAccountEventRuleMatch

**Description:** 

**Platforms:** Public Cloud

---

### IdpPolicyAlertRuleMatch

**Description:** 

**Platforms:** Public Cloud

---

### IdpPolicyCloudAccessRuleMatch

**Description:** 

**Platforms:** Public Cloud

---

### IdpPolicyFederatedAccessRuleMatch

**Description:** 

**Platforms:** Public Cloud

---

### IdpTelemetryData

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogConfigurationsGetResponse

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogConfigurationsSetResponse

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogReEnabled

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionRequest

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionTaken

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionTakenForCpu

**Description:** 

**Platforms:** Windows

---

### IdpWatchdogRemediationActionTakenForMemory

**Description:** 

**Platforms:** Windows

---

### IdwFileWritten

**Description:** Emitted when a process is done writing an IDW file.

**Platforms:** Windows

---

### ImageHash

**Description:** This event is generated for each DLL or executable loaded into a process’ memory.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ImapCommand

**Description:** 

**Platforms:** Linux, Windows

---

### ImgExtensionFileWritten

**Description:** 

**Platforms:** Windows

---

### ImpersonationTokenInfo

**Description:** ImpersonationTokenInfo represents a security context for a general impersonation activity. Each ImpersonationTokenInfo can be linked to a corresponding UserIdentity by using the (UserSid, AuthenticationId) tuple.

**Platforms:** Windows

---

### InboundHttpHeader

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### InboundHttpParsingStatus

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### InjectedThread

**Description:** This event is generated when one process injects an execution thread into another process. While often associated with malicious activity, this is also common behavior for certain core operating system processes.

**Platforms:** Windows

---

### InjectedThreadFromUnsignedModule

**Description:** This event contains information about a thread that was injected into a process from an unsigned module. It combines relevant information from the InjectedThread and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### InstallBundleDownloadComplete

**Description:** An install bundle download has completed.

**Platforms:** Windows

---

### InstalledApplication

**Description:** An event that describes a single application. E.g. representing a newly installed application, one just removed, or one discovered during enumeration. Platforms: Forensics This event contains all the information for a single app. Platforms: macOS An event that describes a single application. E.g. representing a newly installed application, one just removed, or one discovered during enumeration. In the macOS version of this event, the UpdateFlag field only sends the value UPDATE_ENUMERATION (1). Platforms: Linux An event that describes a single application. E.g. representing a newly installed application, one just removed, or one discovered during enumeration.

**Platforms:** Windows

---

### InstalledBrowserExtension

**Description:** An event that contains information about installed browser extensions, including updates and removals. The event is sent when the sensor connects and every 48 hours thereafter. If no browser extensions are identified, a default event indicating no-extension-available is sent to the CrowdStrike cloud.

**Platforms:** Windows, macOS

---

### InstalledUpdates

**Description:** An event that describes the updates installed on the system. The Status field will indicate if some error occurred when attempting to find installed updates. PendingUpdateIds will be an empty string if none are pending. The event is emitted once at startup, and then periodically after that.

**Platforms:** Windows

---

### InstallFromUnknownSourcesStatus

**Description:** An event that contains info about third-party app installers on Android.

**Platforms:** Android

---

### InstallServiceDownloadComplete

**Description:** An install service download has completed.

**Platforms:** Windows

---

### InstanceMetadata

**Description:** Metadata information about the instance on which the sensor is running. Platforms: Kubernetes, macOS

**Platforms:** Windows, Linux, Falcon Container

---

### InternetExposureData

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### IntrusivePackageDiscovered

**Description:** 

**Platforms:** Android

---

### IntrusiveProcessDiscovered

**Description:** 

**Platforms:** iOS

---

### IntrusivePropertyDiscovered

**Description:** 

**Platforms:** Android

---

### IOServiceRegister

**Description:** This event describes an IOService being registered with a notification handler.

**Platforms:** macOS

---

### IoSessionConnected

**Description:** An event that is emitted when an IO session has been connected.

**Platforms:** Windows

---

### IoSessionLoggedOn

**Description:** An event that is emitted when an IO session has been logged off.

**Platforms:** Windows

---

### IPCDetectInfo

**Description:** 

**Platforms:** Windows

---

### IsoExtensionFileWritten

**Description:** 

**Platforms:** Windows

---

### JarFileWritten

**Description:** This event is generated when a Java executable archive (.jar) file type is written to disk.

**Platforms:** Windows, macOS, Linux, Android

---

### JavaClassFileWritten

**Description:** Emitted when a process is done writing a Java Class file.

**Platforms:** Windows, macOS, Linux

---

### JavaInjectedThread

**Description:** This event is generated when Java injects a thread into another process.

**Platforms:** Windows

---

### JpegFileWritten

**Description:** Emitted when a process is done writing a Jpeg image file.

**Platforms:** macOS, Linux, Windows

---

### JumpListInfo

**Description:** 

**Platforms:** Forensics

---

### K8SAdmissionReviewResult

**Description:** 

**Platforms:** Kubernetes

---

### K8SAdmissionReviewResultPrime

**Description:** 

**Platforms:** Public Cloud

---

### K8SCluster

**Description:** Snapshot of Kubernetes cluster for mapping Kubernetes cluster id and name.

**Platforms:** Public Cloud

---

### K8SClusterInfo

**Description:** 

**Platforms:** Kubernetes

---

### K8SDaemonSet

**Description:** Snapshot of a Daemon Set object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SDeployment

**Description:** Snapshot of a deployment object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SEphemeralContainer

**Description:** Snapshot of an ephemeral Container belonging to a Pod.

**Platforms:** Public Cloud

---

### K8SInitContainer

**Description:** Snapshot of status for an Initialization(Init) Container inside a Pod.

**Platforms:** Public Cloud

---

### K8SInitContainerStatus

**Description:** Snapshot of an Initialization(Init) Container belonging to a Pod

**Platforms:** Public Cloud

---

### K8SNode

**Description:** Snapshot of a Node object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SPod

**Description:** Snapshot of a Pod object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SProductConfig

**Description:** 

**Platforms:** Kubernetes

---

### K8SReplicaSet

**Description:** Snapshot of a Replica Set object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SResource

**Description:** 

**Platforms:** Kubernetes

---

### K8SRunningContainer

**Description:** Snapshot of a running Container belonging to a Pod.

**Platforms:** Public Cloud

---

### K8SRunningContainerStatus

**Description:** Snapshot of status for a running Container inside a Pod.

**Platforms:** Public Cloud

---

### K8SService

**Description:** Snapshot of a Service object in Kubernetes.

**Platforms:** Public Cloud

---

### K8SSnapshot

**Description:** 

**Platforms:** Kubernetes

---

### K8SWatchStarted

**Description:** 

**Platforms:** Kubernetes

---

### K8SWatchStopped

**Description:** 

**Platforms:** Kubernetes

---

### KernelCallbackTablePatch

**Description:** An event that indicates that the KernelCallbackTable has been altered at the specified index. If present, CallstackModuleNames, Buffer, and MiniContext apply to the thread that modified the index, with Buffer being the bytes at the faulting address. MiniContext, if set, contains Edi, Esi, Ebx, Edx, Ecx, Eax, Ebp for 32-bit processes and Rax, Rcx, Rdx, Rbx, Rbp, Rsi, Rdi, R8-R15 on 64- bit.

**Platforms:** Windows

---

### KernelCallbackTableUpdate

**Description:** An event that indicates that the ProcessEnvironmentBlock KernelCallbackTable field has been changed from its prior value. This might indicate an attempt to alter one of the callback routines.

**Platforms:** Windows

---

### KernelExtension

**Description:** Describes a macOS kernel extension identified by the collector.

**Platforms:** Forensics

---

### KernelModeExecImage

**Description:** Indicates a kernel Image has been loaded into memory.

**Platforms:** Linux, Falcon Container

---

### KernelModeLoadImage

**Description:** Indicates a kernel-mode module has been loaded into memory.

**Platforms:** Windows, Forensics, Linux, Falcon Container, macOS

---

### KernelParameter

**Description:** 

**Platforms:** Forensics

---

### KernelServiceStarted

**Description:** Indicated that a kernel service was started locally or remotely.

**Platforms:** Windows

---

### KextLoad

**Description:** Signals a Kernel Extension (KEXT) Load, triggered via a MAC hook.

**Platforms:** macOS

---

### KextUnload

**Description:** Signals a Kernel Extension (KEXT) Unload, triggered via a MAC hook.

**Platforms:** macOS

---

### KillProcessError

**Description:** If KillProcessActor fails to kill a process due to process being marked as system critical or for any other reason, this event is emitted.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### LFODownloadComplete

**Description:** 

**Platforms:** Android, Vmcluster, Windows, iOS, Kubernetes, macOS, Linux, Falcon Container

---

### LFODownloadConfirmation

**Description:** Thrown when the agent receives an LFODownload event. Platforms: iOS Platforms: Vmcluster, Kubernetes

**Platforms:** Windows, Linux, Falcon Container, macOS, Android

---

### LfoUploadDataComplete

**Description:** Platforms: macOS, Android, Windows, Linux Emitted when the LFOUploadActor has successfully uploaded a file to the cloud.

**Platforms:** Vmcluster, Kubernetes

---

### LfoUploadDataFailed

**Description:** Emitted when the sensor has detected error(s) and has decided not to stop uploading a file to the cloud. LfoUploadExtendedStatus will indicate the detailed failure reason. Platforms: Kubernetes, Vmcluster

**Platforms:** macOS, Android, Linux, Windows

---

### LfoUploadDataUnneeded

**Description:** Emitted when the sensor initiates a file upload, but the cloud has determined the file is not needed. A specific cloud reason will be provided in LfoUploadCloudStatus. Platforms: Kubernetes, Vmcluster

**Platforms:** Windows, Linux, macOS, Android

---

### LfoUploadStart

**Description:** Emitted when the sensor initiates a file upload. Platforms: Vmcluster, Kubernetes

**Platforms:** macOS, Windows, Android, Linux

---

### LhaFileWritten

**Description:** 

**Platforms:** Windows

---

### LightningUnresponsiveStatus

**Description:** 

**Platforms:** Windows, macOS

---

### LinkFileInfo

**Description:** Link file information.

**Platforms:** Forensics

---

### LnkFileWritten

**Description:** 

**Platforms:** Windows, Linux, macOS

---

### LoadImage

**Description:** Indicates a module has been loaded into memory.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### LocalGroupIdentity

**Description:** Group identity information includes user group name, GID, and names, UIDs and sid of user members.

**Platforms:** Forensics

---

### LocalIpAddressIP4

**Description:** This event is generated when a host uses a new IPv4 network address. Platforms: Forensics

**Platforms:** macOS, iOS, Linux, Falcon Container, Windows, Android

---

### LocalIpAddressIP6

**Description:** This event is generated when a host uses a new IPv6 network address. Platforms: Forensics

**Platforms:** macOS, Linux, Falcon Container, iOS, Windows, Android

---

### LocalIpAddressRemovedIP4

**Description:** This event is generated when a host loses its IPv4 network address.

**Platforms:** Linux, Falcon Container, iOS, Windows, Android, macOS

---

### LocalIpAddressRemovedIP6

**Description:** This event is generated when a host loses its IPv6 network address.

**Platforms:** macOS, iOS, Android, Linux, Falcon Container, Windows

---

### LocalWindowsUserUpdate

**Description:** 

**Platforms:** Windows

---

### LockdownModeStatus

**Description:** 

**Platforms:** iOS

---

### LockScreenStatus

**Description:** An event that contains info about the device lock screen mechanism.

**Platforms:** Android, iOS

---

### LogCollectorDeploymentStatus

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### LogEntry

**Description:** A log entry observed on an endpoint.

**Platforms:** Forensics

---

### LoginItemAdded

**Description:** 

**Platforms:** macOS

---

### LogonBehaviorCompositionDetectInfo

**Description:** 

**Platforms:** Windows

---

### LowILModuleLoadAttempt

**Description:** An event that indicates that a non-LowIL process attempted to load an untrusted LowIL module.

**Platforms:** Windows

---

### LRZipFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### LsassHandleFromUnsignedModule

**Description:** This event contains information about a handle that was created to LSASS from an unsigned module.

**Platforms:** Windows

---

### LSQuarantineEvent

**Description:** 

**Platforms:** Forensics

---

### LZ4FileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### LzfseFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### LZipFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### LzmaFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### LZOFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### MacFsEventRecord

**Description:** Mac fsevents record, forensically interesting filesystem logging/information.

**Platforms:** Forensics

---

### MachOFileWritten

**Description:** Emitted when a process is done writing a MachO file.

**Platforms:** macOS, Linux, Windows

---

### MachOHeaderParsed

**Description:** A MachO file was read into memory from disk and its header was parsed.

**Platforms:** macOS

---

### MacKnowledgeActivityEnd

**Description:** An entry from a knowledgeC database indicating the end of some user activity on a MacOs system.

**Platforms:** Forensics

---

### MacKnowledgeActivityStart

**Description:** An entry from a knowledgeC database indicating the start of some user activity on a MacOs system.

**Platforms:** Forensics

---

### MacMRU

**Description:** A digital forensics record derived from Apple SharedFileList (.sfl/.sfl2) files. This event helps identify most recently used resources (applications, documents, volumes, etc.).

**Platforms:** Forensics

---

### MacroContentInfo

**Description:** Description: Provides information about a macro extracted when an Office file is written or opened ContextTimeStamp System time of event creation ContextProcessId UPID of the process originating this event ImageFileName Full path to an executable (PE) fileThe context of this field provides more information as to its meaning. For ProcessRollup2 events, this is the full path to the main executable for the created process. CommandLine Command line used to create this process Might be empty in some circumstances, visit http://msdn.microsoft.com/en- us/library/windows/desktop/ms682425(v=vs.85).aspx for more information. ScriptContent Script contents; non null-terminated wide-characters OriginalContentLength Size of ScriptContent (before truncation) in bytes ScriptModuleName The name of the VBA module or other module type that contains the script contents TargetFileName Multiple usesAgentOnline - Config file name. If using internal config, field is 0FileOperations - Entire path to the file including name and extension TargetSHA256HashData SHA256HashData for the target context, doesn’t imply a relationship with the ContextProcessId primary image itself MacroSHA256HashData SHA256 hash of an Office macro SHA256HashData SHA256 hash of a file; in most cases, the hash of the file that is referred to by the ImageFileName fieldValuesSTATIC_SHA256_DOPPELGANGING (0x56f3097c4d5bf4c7cffef168ee732e1c78f2ee62bc1c1ba61c219226bef619f8)STATIC_SHA256_SYSTEM (0x03312a19baa7ab137c09127c6feb58c05216a7880d3c9e6ae54a8bcda460f92a) MacroExtractorVersion Version of the macro extractor on the sensor KnownFileType Known file type constantValues (from type KnownFileType)UNKNOWN (0) - Unknown file typePE (1) - PE file (Windows executable)PDF (2) - PDF file (Adobe Acrobat / Reader)OLE (3) - OLE file (Office -le 2003; eg .doc)RTF (4) - RTF file (Rich Text Format; can be .doc)ZIP (5) - ZIP file, not detected as JAR or OOXMLJAR (6) - JAR file, Java archive (very simple detection)OOXML (7) - OOXML file (Office -ge 2007; eg .docx)DMP (8) - DMP file (Windows memory dump file)RAR (9) - RAR file, archiveSZIP (10) - 7zip file, archiveDWG (11) - DWG file, CAD relatedIDW (12) - IDW file, CAD relatedDXF (13) - DXF file, CAD relatedSLD (14) - SLDPRT/SLDDRW/SLDASM file, CAD relatedCAB (15) - CAB file (Microsoft Cabinet)MACHO (16) - MachO file (macOS executable)TAR (17) - TAR file, archiveXAR (18) - XAR file, archiveBZ2 (19) - BZip2 file, archiveSCRIPT (20) - Script file. Used only on macESE (21) - Extensible Storage Engine (ESE) Database File (EDB) format. Formerly JET databaseCLASS (22) - JavaClass File, Java byte codeELF (23) - ELF file (linux executable)GZIP (24) - Gzip file, archiveARC (27) - ARC archive fileARJ (28) - ARJ archive fileTIFF (29) - TIFF image fileGIF (30) - GIF image fileJPEG (31) - JPEG image filePNG (32) - PNG image fileBMP (33) - BMP image fileBLF (34) - BLF log fileMSDOCX (35) - MS Office Docx fileMSXLSX (36) - MS Office Xlsx fileMSPPTX (37) - MS Office Pptx fileMSVSDX (38) - MS Office Vsdx fileVMDK (39) - VMDK VMWare virtual machine fileVDI (40) - VDI VMWare virtual machine fileDMG (41) - Disk image fileMSI (42) - MSI fileEMAIL (43) - Email message fileLNK (44) - LNK fileEMAILARC (45) - Email archive fileRPM (46) - Linux RPM packageDEB (47) - Linux DEB packageWEBSCRIPT (48) - Web script (ASPX, PHP, etc.)PYTHON (49) - Python source fileBATCH (50) - Windows batch script fileHIVE (51) - Windows registry hive fileADEXPLORER (52) - ADExplorer snapshot fileCRX (53) - CRX Chrome Extension file ScriptContentBytes Script Contents Binary buffer ScriptContentCodePage Script contents binary buffer is reported to be encoded with this code page identifier ControlTemplateMatched Indicates if an office macro matched a OfficeFileMacroMLExclusions template instance ControlTemplateInstanceId The instance ID from a template OfficeFileMacroMLExclusions match; used for debugging ConfigBuild Config that caused this event CloudRequestId CloudRequestId is an identifier provided by the cloud whenrequesting action from the sensor; the sensor acknowledges the request with a CloudRequestReceived event. ConfigStateHash Murmur3-32 Hash of ConfigStateUpdate table csv from ConfigState; comparable between sensors only within a CID as channel versions are not unique or portable across CIDs. ConfigStateIndex Deprecated Non-cloudable static field that is SMEnhanced to contain the number 1; prior to SMEnhancer understanding immediate values needed to index into the appropriate RuntimeSystemTable entry SensorRequestId Identifier provided by the sensor when requesting action from the cloud The cloud echos back the SensorRequestId where appropriate Entitlements Bitfield of Cloud relevant Entitlements for the SKU that this sensor is currently licensed for; Sensor relevant entitlements are stored in SystemTable Tags. The value is set by the cloud and only has meaning to the cloud.The value is totally opaque to the sensor. There won’t be any #define or similar info relating to this field in sensor code. It is sent to the cloud by the sensor for efficiency, because the cloud can’t afford to look up sensor(aid) specific entitlements for every arriving event. EffectiveTransmissionClass Field representing the effective transmission class BoundingState Indicates the bounding decision for a cloudable eventValuesUNBOUNDED (0)BOUNDED (1) BoundingLimitCount Aggregate threshold for a given event type; thisfield is present on an event only after a bounding threshold has been exceeded. It signals an imminent end to transmission of this type of event.For events containing a UPID field, this threshold count is usually applied per-process. Transmission might restart under various conditions. Some events have their threshold count raised, if they are, or become, a Detect-Tree (TreeId field is set). Rate limited events might restart after the time interval indicated by BoundingLimitDuration expires. There are also SystemTags that might change bounding behavior for some event types. EventOrigin If set, this field should be non-zero, to indicate whether it is aBaseline (bit-0), Detect (bit-1), or Experiment (bit-7-34).bits 2-6/35-63 are spare.If this field doesn’t exist on an event, it is equivalent to having the value 1, indicating a pure Baseline event.An event can be both Baseline and Detect at the same time, if a process is part of a detect, but hasn’t exceeded the baseline limits for the event. It could also be Baseline and in one or more experiments simultaneously.ValuesBASELINE (0x1) - Sent while within ordinary baseline bounding limitsDETECT (0x2) - Sent while UPID was in a DetectCROWDSCORE (0x4) - Relevant to CrowdScore analysisTRIGGER (0x8) - OverwatchTrigger/CrowdscoreTrigger Incident eventsUNBOUNDED (0x10) - SysPolicy tag directed unboundingEXPERIMENT1 (0x100) - sent due to experiment-1EXPERIMENT2 (0x200) - sent due to experiment-2EXPERIMENT3 (0x400) - sent due to experiment-3EXPERIMENT4 (0x800) - sent due to experiment-4EXPERIMENT5 (0x1000) - sent due to experiment-5EXPERIMENT6 (0x2000) - sent due to experiment-6 BoundingLimitDuration The duration window in milliseconds during which an aggregate threshold applies for a given event type. Thisfield appears in conjunction with BoundingLimitCount.The duration represented by the value of this field goes intoeffect at a point determined by the respective bounding algorithm.Some 24h timers are tied to sensor load-time, other algorithms start timing from the first instance of the event. AnnotationData Arbitrary data attached to those events that are associated or interesting to an Integration(Annotation) Vendor Tactic Field representing the MITRE Tactic name or identifier and used to label events related to a MITRE classified activityCurrently this universal field isn’t used or referenced in the Sensor. It is only of use to the Cloud. Technique Field representing the MITRE Technique name or identifier and used to label events related to a MITRE classified activityCurrently this universal field isn’t used or referenced in the Sensor. It is only of use to the Cloud. FieldReference Universal field for representing field references within events

**Platforms:** Windows

---

### MacroDetectInfo

**Description:** Event description: Provides more context around the macro content that was detected. ContextProcessId UPID of the process generating this event FileAnalysisContext The context for the macro’s detection, such as File Open or File Written ValuesUNKNOWN (0)FILE_WRITE (1)FILE_OPEN (2) TargetFileName Multiple uses:AgentOnline - Config file name. If using internal config, field is 0 FileOperations - Entire path to the file including name and extension FileIdentifier UFID definition IsOnNetwork Set to true if the relevant file listed in the eventis on a network drive IsOnRemovableDisk Set to true if this file was located on a removable disk ParentImageFileName The ImageFileName of the parent process GrandparentImageFileName The ImageFileName of the parent-of-parent process CommandLine The command line used to create this process; may be empty in some circumstancesFor more information, visit http://msdn.microsoft.com/en- us/library/windows/desktop/ms682425(v=vs.85).aspx MacroSHA256HashData The SHA256 hash of an Office macro TargetSHA256HashData SHA256HashData for the target context; doesn’t imply relationship with the ContextProcessIdprimary image itself ImageFileName Full path to an executable (PE) file The context of this field provides more information as to its meaning. For ProcessRollup2 events, this is the full path to the main executable for the created process. SHA256HashData The SHA256 hash of a fileIn most cases, the hash of the file that is referred to by the ImageFileName fieldValuesSTATIC_SHA256_DOPPELGANGING (0x56f3097c4d5bf4c7cffef168ee732e1c78f2ee62bc1c1ba61c219226bef619f8)STATIC_SHA256_SYSTEM (0x03312a19baa7ab137c09127c6feb58c05216a7880d3c9e6ae54a8bcda460f92a) TemplateInstanceId The instance ID from a template match, used for debugging TemplateDisposition The requested disposition of a template hitValuesTEMPLATE_DISPOSITION_NOACTION (0)TEMPLATE_DISPOSITION_ANALYSIS (3)TEMPLATE_DISPOSITION_SENSOR_ONLY (4)TEMPLATE_DISPOSITION_INDICATOR (10)TEMPLATE_DISPOSITION_DETECT (20)TEMPLATE_DISPOSITION_OPERATION_BLOCK (25)TEMPLATE_DISPOSITION_PREVENT (30)TEMPLATE_DISPOSITION_PREVENT_KILLPARENT (60)TEMPLATE_DISPOSITION_PREVENT_KILLSOURCE (61) PatternId PatternIdList Comma separated list of pattern IDs ParentProcessPatternIdList Comma separated list of pattern IDs for parent process GrandparentProcessPatternIdList Comma separated list of pattern IDs for grandparent process ScriptModuleName Name of the VBA module or other module type that contains the script contents ScriptContent Script contents; non null-terminated wide-characters ConfigBuild Field present implicitly on every event to carry the config that caused this event CloudRequestId Identifier provided by the cloud when requesting action from the sensor The sensor acknowledges the request with a CloudRequestReceived event. ConfigStateHash Murmur3-32 Hash of ConfigStateUpdate table csv from ConfigState Comparable between sensors only within a CID; channel versions aren’t unique or portable across CIDs ConfigStateIndex Deprecated Non-cloudable static field that is SMEnhanced to contain the number 1; prior to SMEnhancer understanding immediate values needed to index into the appropriate RuntimeSystemTable entry SensorRequestId Identifier provided by the sensor when requesting action from the cloud The cloud echos back the SensorRequestId where appropriate Entitlements Bitfield of Cloud relevant Entitlements for the SKU that this sensor is currently licensed for; Sensor relevant entitlements are stored in SystemTable Tags. The value is set by the cloud and only has meaning to the cloud.The value is totally opaque to the sensor. There won’t be any #define or similar info relating to this field in sensor code. It is sent to the cloud by the sensor for efficiency, because the cloud can’t afford to look up sensor(aid) specific entitlements for every arriving event. EffectiveTransmissionClass Field representing the effective transmission class BoundingState Indicates the bounding decision for a cloudable eventValuesUNBOUNDED (0)BOUNDED (1) BoundingLimitCount Aggregate threshold for a given event type; thisfield is present on an event only after a bounding threshold has been exceeded. It signals an imminent end to transmission of this type of event.For events containing a UPID field, this threshold count is usually applied per-process. Transmission might restart under various conditions. Some events have their threshold count raised, if they are, or become, a Detect-Tree (TreeId field is set). Rate limited events might restart after the time interval indicated by BoundingLimitDuration expires. There are also SystemTags that might change bounding behavior for some event types. EventOrigin If set, this field should be non-zero, to indicate whether it is aBaseline (bit-0), Detect (bit-1), or Experiment (bit-7-34).bits 2-6/35-63 are spare.If this field doesn’t exist on an event, it is equivalent to having the value 1, indicating a pure Baseline event.An event can be both Baseline and Detect at the same time, if a process is part of a detect, but hasn’t exceeded the baseline limits for the event. It could also be Baseline and in one or more experiments simultaneously.ValuesBASELINE (0x1) - Sent while within ordinary baseline bounding limitsDETECT (0x2) - Sent while UPID was in a DetectCROWDSCORE (0x4) - Relevant to CrowdScore analysisTRIGGER (0x8) - OverwatchTrigger/CrowdscoreTrigger Incident eventsUNBOUNDED (0x10) - SysPolicy tag directed unboundingEXPERIMENT1 (0x100) - sent due to experiment-1EXPERIMENT2 (0x200) - sent due to experiment- 2EXPERIMENT3 (0x400) - sent due to experiment-3EXPERIMENT4 (0x800) - sent due to experiment-4EXPERIMENT5 (0x1000) - sent due to experiment-5EXPERIMENT6 (0x2000) - sent due to experiment-6 BoundingLimitDuration The duration window in milliseconds during which an aggregate threshold applies for a given event type. Thisfield appears in conjunction with BoundingLimitCount.The duration represented by the value of this field goes intoeffect at a point determined by the respective bounding algorithm.Some 24h timers are tied to sensor load-time, other algorithms start timing from the first instance of the event. AnnotationData Arbitrary data attached to those events that are associated or interesting to an Integration(Annotation) Vendor Tactic Field representing the MITRE Tactic name or identifier and used to label events related to a MITRE classified activityCurrently this universal field isn’t used or referenced in the Sensor. It is only of use to the Cloud. Technique Field representing the MITRE Technique name or identifier and used to label events related to a MITRE classified activityCurrently this universal field isn’t used or referenced in the Sensor. It is only of use to the Cloud. FieldReference Universal field for representing field references within events

**Platforms:** Windows

---

### MalPaths

**Description:** Malicious DLL or executable image name conflicts found in different or unexpected folders.

**Platforms:** Forensics

---

### ManifestDownloadComplete

**Description:** Sent by LFODownloadActor when a new configuration manifest has been downloaded. Platforms: Kubernetes Platforms: Vmcluster

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### MbrOverwriteRawDetectInfo

**Description:** 

**Platforms:** Windows

---

### MemoryAdvise

**Description:** 

**Platforms:** Linux

---

### MemoryLocked

**Description:** 

**Platforms:** Linux

---

### MemoryMapped

**Description:** Triggers when an executable memory region is mapped.

**Platforms:** Linux, Falcon Container

---

### MemoryProtectionChanged

**Description:** 

**Platforms:** Linux

---

### MemoryProtectionUpdated

**Description:** Triggers if a new executable memory region is mapped which is writable or mapped from a file.

**Platforms:** Linux, Falcon Container

---

### MemoryScanEnabled

**Description:** 

**Platforms:** Windows

---

### MemoryScanErrorEvent

**Description:** 

**Platforms:** Windows

---

### MftBootSector

**Description:** Windows Master File Table (MFT) Boot sector.

**Platforms:** Forensics

---

### MftRecord

**Description:** Windows Master File Table (MFT) record.

**Platforms:** Forensics

---

### MobileAppIdentifiers

**Description:** An event that describes details about a mobile application package.

**Platforms:** Android

---

### MobileAppsManifest

**Description:** Delivers information about apps.

**Platforms:** Android

---

### MobileDetection

**Description:** An event that's sent by the sensor when a sensor-level detection occurs.

**Platforms:** iOS, Android

---

### MobileOsForensicsReport

**Description:** 

**Platforms:** iOS, Android

---

### MobileOsIntegrityStatus

**Description:** Describes the integrity of the mobile OS (eg. jailbroken/rooted)

**Platforms:** Android, iOS

---

### MobilePowerStats

**Description:** Sent when power level in a mobile device changes, also contains duration when the sensor is in foreground/background during IntervalStartTime to IntervalEndTime.

**Platforms:** Android, iOS

---

### ModifyServiceBinary

**Description:** Indicates a Windows service's binary was changed.

**Platforms:** Windows

---

### ModuleBlockedEvent

**Description:** This event is sent to inform cloud about the fact that given module (identified by hash) was blocked.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ModuleBlockedEventWithPatternId

**Description:** This event adds a potential reason for blocking (as a PatternId) to module blocking information.

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ModuleCertificateInfo2

**Description:** 

**Platforms:** Windows

---

### ModuleDetectInfo

**Description:** This event identifies a scenario that would be a blocking prevention if more rigorous settings were active.

**Platforms:** Linux, Falcon Container, Windows, macOS

---

### ModuleDownloadComplete

**Description:** Sent by LFODownloadActor when a new module has been downloaded as part of a configuration update.

**Platforms:** Windows, Linux, macOS

---

### ModuleLoadV3DetectInfo

**Description:** Additional information for detections from the Module Load V3 template.

**Platforms:** Windows

---

### MotwWritten

**Description:** 

**Platforms:** Windows

---

### MountedVolume

**Description:** 

**Platforms:** Windows

---

### MpThreat

**Description:** Microsoft protection threat.

**Platforms:** Forensics

---

### MpThreatAction

**Description:** Report when a particular threat action type has occurred.

**Platforms:** Forensics

---

### MpThreatDetection

**Description:** Microsoft protection threat detection.

**Platforms:** Forensics

---

### MpThreatDetectionWMI

**Description:** 

**Platforms:** Forensics

---

### MpThreatWMI

**Description:** 

**Platforms:** Forensics

---

### MSDocxFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### MsiFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### MsiTransactionExecuted

**Description:** 

**Platforms:** Windows

---

### MSPptxFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### MSVsdxFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### MSXlsxFileWritten

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### NamedMutantHandleClosedTelemetry

**Description:** An event that indicates that a process closed a handle to a known bad named mutex.

**Platforms:** Windows

---

### NamedPipe

**Description:** Named pipe information.

**Platforms:** Forensics

---

### NamedPipeDetectInfo

**Description:** Named pipe detect telemetry event

**Platforms:** Windows

---

### NamedSemaphoreHandleClosedTelemetry

**Description:** An event that indicates that a process closed a handle to a known bad named semaphore.

**Platforms:** Windows

---

### NamespaceChanged

**Description:** 

**Platforms:** Linux, Falcon Container

---

### NeighborListIP4

**Description:** This event shows the IPv4 network addresses and MAC addresses of other devices on the host's network, gathered using ARP on the host. The first time a device sends this event to the CrowdStrike Cloud, its entire ARP table is sent. For later events, only the changes to the ARP table are sent. This event returns data as a MAC address, an IPv4 address, and a delimiter character (0 or 1). Each item is separated by a pipe character (|). If the delimiter character is a 0, the preceding MAC and IP addresses belong to a device. If the delimiter character is 1, the preceding IP and MAC addresses belong to the host's gateway.

**Platforms:** macOS, Linux, Falcon Container, Forensics, Windows

---

### NeighborListIP6

**Description:** This event shows the MAC addresses and IPv6 network addresses of other devices on the host's network, gathered using ARP on the host. The first time a device sends this event to the CrowdStrike Cloud, its entire ARP table is sent. For later events, only the changes to the ARP table are sent. This event returns data as a MAC address, an IPv6 address, and a delimiter character (0 or 1). Each item is separated by a pipe character (|). If the delimiter character is a 0, the preceding MAC and IP addresses belong to a device. If the delimiter character is 1, the preceding IP and MAC addresses belong to the host's gateway. Platforms: Forensics

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### NetShareAdd

**Description:** This event is generated when a network share is added or modified on a host.

**Platforms:** Windows

---

### NetShareDelete

**Description:** This event is generated when a network share is removed from a host.

**Platforms:** Windows

---

### NetShareInfo

**Description:** Shared resource information.

**Platforms:** Forensics

---

### NetShareSecurityModify

**Description:** This event is generated when the security descriptor of a network share is changed.

**Platforms:** Windows

---

### NetworkCloseIP4

**Description:** An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. Platforms: macOS An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 5 minutes using UDP. IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. Platforms: Linux, Falcon Container An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 2 minutes using UDP.IPv4 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state.

**Platforms:** Windows, Android, Forensics

---

### NetworkCloseIP6

**Description:** An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. Platforms: Linux, Falcon Container An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 2 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. Platforms: Android An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 10 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state. Platforms: macOS An event that is generated by an application using a connection-oriented or connectionless protocol attempts to set the socket to the closed state. This event is also generated when a session is inactive for 5 minutes using UDP. IPv6 is the source of the connection/connectionless protocol in this event. Note: this event does not guarantee the communication between the two endpoints has ceased, but that a single socket has entered the closed state.

**Platforms:** Windows, Forensics

---

### NetworkConnectIP4

**Description:** This event is generated when an application attempts a remote connection. Platforms: Forensics, ChromeOS

**Platforms:** Windows, iOS, Linux, Falcon Container, macOS, Android

---

### NetworkConnectIP4Blocked

**Description:** This event is created whenever a NetworkConnectIP4 event is blocked. Platforms: iOS This event is created whenever a NetworkConnectIP4 event is blocked because of the IP or the domain/URL being accessed.

**Platforms:** Android, Windows, macOS

---

### NetworkConnectIP4DetectInfo

**Description:** This event is sent whenever a connection to malicious IP4 address is detected.

**Platforms:** iOS, Android

---

### NetworkConnectIP6

**Description:** This event is created whenever an application using a connection-oriented protocol attempts a remote connection (e.g., via a call to the connect() function) or a connectionless protocol first attempts to transmit a message (e.g., via a call to the sendto() function). Platforms: Linux, Falcon Container This event is generated when an application attempts a remote connection. Platforms: Forensics, ChromeOS

**Platforms:** Windows, iOS, Android, macOS

---

### NetworkConnectIP6Blocked

**Description:** This event is created whenever a NetworkConnectIP6 event is blocked because of the IP or the domain/URL being accessed. Platforms: Windows, macOS, Android This event is created whenever a NetworkConnectIP6 event is blocked.

**Platforms:** iOS

---

### NetworkConnectIP6DetectInfo

**Description:** This event is sent whenever a connection to malicious IP6 address is detected.

**Platforms:** iOS, Android

---

### NetworkContainmentCompleted

**Description:** This event is sent by the sensor after processing a NetworkContainmentRequest event from the cloud. The Status field indicates the success or failure of the containment operation. Platforms: iOS, Android

**Platforms:** macOS, Linux, Windows

---

### NetworkDnsSuffix

**Description:** A network suffix name in the configured DNS suffix list.

**Platforms:** Forensics

---

### NetworkEndPointDataUsage

**Description:** This event has total counts of sent/received octets/packets to/from the network-attached end point during active connection. The counting window is the life of the end point.

**Platforms:** Forensics

---

### NetworkHostsFileEntry

**Description:** A host name entry in the network hosts file.

**Platforms:** Forensics

---

### NetworkIcmpDataIP4

**Description:** 

**Platforms:** Linux

---

### NetworkIcmpDataIP6

**Description:** 

**Platforms:** Linux

---

### NetworkInterfaceStatistics

**Description:** 

**Platforms:** Forensics

---

### NetworkLinkConfigGetAddress

**Description:** 

**Platforms:** Linux

---

### NetworkLinkConfigGetLink

**Description:** 

**Platforms:** Linux

---

### NetworkListenIP4

**Description:** This event is generated when an application establishes a socket in listening mode Platforms: Forensics, ChromeOS Platforms: Linux, Falcon Container This event is generated when an application establishes a socket in listening mode.

**Platforms:** Windows, macOS, Android

---

### NetworkListenIP6

**Description:** This event is created whenever an application using a connection-oriented protocol establishes a socket in listening mode (e.g., via a call to the listen() function). Platforms: Forensics, ChromeOS

**Platforms:** Windows, Android, Linux, Falcon Container, macOS

---

### NetworkModuleLoadAttempt

**Description:** An event that indicates that a process whose primary image was not on a network attempted to load a module from that network.

**Platforms:** Windows

---

### NetworkOutboundPortScanDetectInfo

**Description:** 

**Platforms:** Windows

---

### NetworkReceiveAcceptIP4

**Description:** This event is generated when an application using a connection-oriented protocol attempts to accept a remote connection request (e.g., via a call to the accept() function) or a connectionless protocol attempts to process the first datagram received. Platforms: Forensics

**Platforms:** Windows, Android, Linux, Falcon Container, macOS

---

### NetworkReceiveAcceptIP6

**Description:** This event is created whenever an application using a connection-oriented protocol attempts to accept a remote connection request (e.g., via a call to the accept() function) or a connectionless protocol attempts to process the first datagram received. Platforms: Forensics

**Platforms:** Windows, Android, Linux, Falcon Container, macOS

---

### NetworkStatisticsIP4

**Description:** 

**Platforms:** Forensics

---

### NetworkStatisticsIP6

**Description:** 

**Platforms:** Forensics

---

### NetworkStatisticsTCP4

**Description:** 

**Platforms:** Forensics

---

### NetworkStatisticsTCP6

**Description:** 

**Platforms:** Forensics

---

### NetworkStatisticsUDP4

**Description:** 

**Platforms:** Forensics

---

### NetworkStatisticsUDP6

**Description:** 

**Platforms:** Forensics

---

### NetworkSummary

**Description:** 

**Platforms:** Windows

---

### NetworkUncontainmentCompleted

**Description:** Platforms: Linux, Windows, macOS This event is sent by the sensor after processing a NetworkUncontainmentRequest event from the cloud. The Status field indicates the success or failure of the uncontainment operation.

**Platforms:** Android, iOS

---

### NewExecutableRenamed

**Description:** This event is generated when an executable is renamed.

**Platforms:** Windows, macOS

---

### NewExecutableWritten

**Description:** This event is generated when an executable file extension is written, whether or not it is truly an executable file type. Any file that ends with a known executable file extension (e.g. .exe, .bat, .scr) will generate this event. The difference between a NewExecutableWritten event and PeFileWritten is that NewExecutableWritten looks for the extension of a file written, while PEFileWritten looks for the PE header in a file that was written.

**Platforms:** Windows, Linux, macOS

---

### NewScriptWritten

**Description:** This event is generated when a new script is written (e.g. .js, .aspx, .bat, .ps1, .vbs, .lua). Platforms: Linux, Falcon Container, macOS The NewScriptWritten template can be triggered by file writes in following scenarios: 1. a file is created with a two character shebang (!#) as the first two bytes of the file with the script extension, 2. a file is created with a two character shebang (!#) as the first two bytes of the file without the extension, or 3. a file is created without the shebang and has a known script extension. These extensions are listed in the following table. Script Type Example Extensions Bash Shell .sh Script Type Example Extensions JavaScript .js, .jsp, .jspx, .jsw, .jsv, .jsv, .jspf Perl .pl Python .py Ruby .rb Powershell .psl Lua .lua Batch .bat Groovy .groovy AWK .awk PHP .php, .phpNs, .inc, .ctp, .pht, .phar Apache distributed config .htaccess Modulefile .module Config file .config ASP.NET .ashx, .asmx, .aspq, .asa, .axd, .aspx, .aspq REM .rem SOAP .soap Cretificate .cer WSS .wss Do .do Database Manager .dbm SWF .swf CGI .cgi Action .action Yaws .yaws HTML .html, .shtml, .vbhtml, .phtml, .cshtml Script Type Example Extensions ColdFusion .cfm, .cfc, .cfml

**Platforms:** Windows

---

### NtfsLinkCreatedDetectInfo

**Description:** 

**Platforms:** Windows

---

### NtfsQueryEaExploitAttempt

**Description:** 

**Platforms:** Windows

---

### NullPageProtectionModificationAttempt

**Description:** An event that indicates that an attempt was made to modify the protection of the NULL page.

**Platforms:** Windows

---

### NullPageUnmapAttempt

**Description:** An event that indicates that an attempt was made to unmap the NULL page.

**Platforms:** Windows

---

### ObjCRuntimeAltered

**Description:** An event that indicates an Obj-C method has been tampered with. MethodSignature indicates which Obj-C method has been tampered with. ImageFileName contains the path to the image containing the new, swizzled, implementation of the method. ExpectedImageFileName contains the path where it was expected. SuspectAddress contains the load address of ImageFileName. ExpectedAddress contains the load address of ExpectedImageFileName.

**Platforms:** iOS

---

### OciContainerComplianceInfo

**Description:** 

**Platforms:** Linux, Falcon Container

---

### OciContainerEngineInfo

**Description:** An event that contains information about this container engine.

**Platforms:** Linux, Falcon Container

---

### OciContainerHeartbeat

**Description:** An event that is sent by the sensor to indicate this container engine is still being used. This event is sent every 24 hours.

**Platforms:** Linux, Falcon Container

---

### OciContainerInfo

**Description:** An event that contains information about this container on creation of the container.

**Platforms:** Linux, Falcon Container

---

### OciContainerPlumbingSummary

**Description:** 

**Platforms:** Linux

---

### OciContainerStarted

**Description:** An event that is sent by the sensor to indicate a container has started when the container is created.

**Platforms:** Linux, Falcon Container

---

### OciContainerStopped

**Description:** An event sent to indicate a container has stopped when the container is deleted.

**Platforms:** Linux, Falcon Container

---

### OciContainerTelemetry

**Description:** An event that contains telemetry information on a container.

**Platforms:** Linux, Falcon Container

---

### OciImageHeartbeat

**Description:** An event that is sent by the sensor to indicate this image is still being used.

**Platforms:** Linux, Falcon Container

---

### OciImageInfo

**Description:** An event that contains information about this image used in a container.

**Platforms:** Linux, Falcon Container

---

### OdsActionStatus

**Description:** Platforms: Windows

**Platforms:** macOS

---

### OdsCancelRequestReceived

**Description:** Platforms: macOS

**Platforms:** Windows

---

### OdsMaliciousFileFound

**Description:** Platforms: Windows

**Platforms:** macOS

---

### OdsProfileReceived

**Description:** Platforms: Windows

**Platforms:** macOS

---

### OdsScanComplete

**Description:** On-demand scan for files with name extensions and header magic values.

**Platforms:** Forensics

---

### OdsScheduleCanceled

**Description:** Platforms: macOS

**Platforms:** Windows

---

### OdsScheduleCancelRequestReceived

**Description:** Platforms: macOS

**Platforms:** Windows

---

### OdsScheduleRequestReceived

**Description:** Platforms: macOS

**Platforms:** Windows

---

### OdsStarted

**Description:** Platforms: Windows

**Platforms:** macOS

---

### OdsStartRequestReceived

**Description:** Platforms: macOS

**Platforms:** Windows

---

### OdsStatus

**Description:** Platforms: Windows

**Platforms:** macOS

---

### OleFileWritten

**Description:** This event is generated when a file a Microsoft Office (Pre-Office 2007) file type is written to disk.

**Platforms:** Windows, macOS, Linux

---

### OoxmlFileWritten

**Description:** This event is generated when a Microsoft Office (Post-Office 2007) file type is written to disk.

**Platforms:** Windows, macOS, Linux

---

### OpenDirectoryAttributeAdd

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryAttributeRemove

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryAttributeSet

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryCreateUser

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryDeleteUser

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryGroupAdd

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryGroupRemove

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryGroupSet

**Description:** 

**Platforms:** macOS

---

### OpenDirectoryPasswordModification

**Description:** 

**Platforms:** macOS

---

### OsfmDownloadComplete

**Description:** Sent by LFODownloadActor when new OSFM data is downloaded.

**Platforms:** Windows

---

### OsUpdateTimestamp

**Description:** Operating system update timestamp.

**Platforms:** Forensics

---

### OsVersionInfo

**Description:** This event is generated during any one of the following scenarios: A host is turned on or rebooted A new Falcon sensor is installed on a host An existing Falcon sensor is updated This provides details about the operating system on which the sensor is running. Servers do not get rebooted often. Hence, you might not see some servers in this sample query. Platforms: Forensics, Vmcluster, Windows Legacy Platforms: Kubernetes

**Platforms:** Windows, Linux, Falcon Container, Android, iOS, macOS

---

### PackageManagerDownloadComplete

**Description:** 

**Platforms:** Kubernetes, Vmcluster, Windows, macOS, Linux, Falcon Container

---

### PackedExecutableWritten

**Description:** An event that indicates that a packed executable was written to disk. The packer type is indicated by the FileSubType field.

**Platforms:** Windows

---

### PacketDiversionConnectionsOverloadConfigurationResponse

**Description:** 

**Platforms:** Windows

---

### PacketFilterAttached

**Description:** 

**Platforms:** Linux

---

### PathUnexpectedlyReadable

**Description:** An event that indicates a system file or directory can be opened for reading. On a non-jailbroken system, this should not be possible.

**Platforms:** iOS

---

### PatternHandlingError

**Description:** This event is emitted when an error occurs in processing a behavior.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### PcaAppLaunchEntry

**Description:** An application launch entry in windows Program Compatibility Assistant (PCA) file PcaAppLaunchDic.txt.

**Platforms:** Forensics

---

### PcaGeneralDbEntry

**Description:** An application launch entry in windows Program Compatibility Assistant (PCA) database PcaGeneralDb[0-9]+.txt.

**Platforms:** Forensics

---

### PdfFileWritten

**Description:** This event is generated when a PDF file type (.pdf) is written to disk.

**Platforms:** Windows, Linux, macOS

---

### PeaFileWritten

**Description:** 

**Platforms:** Windows

---

### PeCodePageInfo

**Description:** A code page that is used to decode code point values within a windows Portable Executable resource.

**Platforms:** Forensics

---

### PeFileWritten

**Description:** This event is generated when a Windows Portable Executable file type is written to disk. The difference between a NewExecutableWritten event and PeFileWritten is that NewExecutableWritten looks for the extension of a file written, while PEFileWritten looks for the PE header in a file that was written.

**Platforms:** Windows, macOS, Linux

---

### PeFileWrittenDetectInfo

**Description:** 

**Platforms:** Windows

---

### PeHeaderInfo

**Description:** Portable Executable header information from a Windows executable.

**Platforms:** Forensics

---

### PeHeaderOptionalInfo

**Description:** Portable Executable optional header information from a Windows executable.

**Platforms:** Forensics

---

### PeLanguageId

**Description:** A language on which a windows Portable Executable resource depends.

**Platforms:** Forensics

---

### PemFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### PeSectionInfo

**Description:** Windows Portable Executable (PE) section information.

**Platforms:** Forensics

---

### PeVersionInfo

**Description:** An event that describes file version information from a Portable Executable file resource location, as seen in the file properties dialog on Windows. The data is in the form of a binary blob that requires further parsing.

**Platforms:** Windows

---

### PhpBase64Decode

**Description:** 

**Platforms:** Linux

---

### PhpEvalString

**Description:** 

**Platforms:** Linux

---

### PhpExecuteScript

**Description:** 

**Platforms:** Linux

---

### PngFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### PodInfo

**Description:** Metadata associated with a Kubernetes pod.

**Platforms:** Linux, Falcon Container

---

### PodProductConfig

**Description:** 

**Platforms:** Linux, Falcon Container

---

### Pop3Command

**Description:** 

**Platforms:** Windows, Linux

---

### PrefetchFile

**Description:** Prefetch or Layout file records 8 most recent execution times of a Windows application.

**Platforms:** Forensics

---

### PrivilegedProcessHandle

**Description:** Indicates a process has opened a handle to a privileged process with special access rights.

**Platforms:** Windows

---

### PrivilegedProcessHandleFromUnsignedModule

**Description:** This event contains information about a privileged process handle created from an unsigned module.

**Platforms:** Windows

---

### ProcessActivitySummary

**Description:** A rollup event created when a process terminates. Includes statistical information about what a process did during its lifetime.

**Platforms:** Windows, macOS

---

### ProcessAncestryInformation

**Description:** The ProcessAncestryInformation event captures unique process lineage chains (process, parent, grandparent, and great-grandparent) that haven't been observed recently on the host, and won't be generated for repetitious executions. This experimental event helps identify anomalous process execution patterns that may indicate suspicious activity or novel attack techniques, and is subject to change in future releases.

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### ProcessBlocked

**Description:** This event is generated when a process is blocked based on a prevention policy. Platforms: Windows Legacy

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ProcessControl

**Description:** 

**Platforms:** Linux, Falcon Container

---

### ProcessDataUsage

**Description:** Measurements and statistics of data traffic sent and received to/from the target process.

**Platforms:** Forensics

---

### ProcessEnvironmentEmpty

**Description:** 

**Platforms:** Linux

---

### ProcessExecOnPackedExecutable

**Description:** An event that contains telemetry data emitted on execution of a PE file which is known to be packed. The packer type is indicated by the FileSubType field.

**Platforms:** Windows

---

### ProcessExecOnRDPFile

**Description:** A PE file was written and executed from an RDP session.

**Platforms:** Windows

---

### ProcessExecOnSMBFile

**Description:** An event that contains telemetry data emitted on execution of a PE file which was written by SMB.

**Platforms:** Windows

---

### ProcessExecOnWinRMFile

**Description:** 

**Platforms:** Windows

---

### ProcessHandleOpDetectInfo

**Description:** An event that describes the operation on a Process handle that triggered a detection.

**Platforms:** Windows

---

### ProcessHandleOpDowngraded

**Description:** An event that describes the operation on a Process handle where the AccessMask was downgraded.

**Platforms:** Windows

---

### ProcessHandleTableEntry

**Description:** An entry in a process handle table referencing a kernel object.

**Platforms:** Forensics

---

### ProcessInjection

**Description:** An event that indicates that a remote process wrote and executed code.

**Platforms:** Windows

---

### ProcessOpenedFileDescriptor

**Description:** 

**Platforms:** Forensics

---

### ProcessPatternTelemetry

**Description:** Platforms: Windows

**Platforms:** Linux, macOS

---

### ProcessRollup

**Description:** An event that contains information from several sources and combines it into one event. The event describes a process which is running or has previously run on the host. The functionality of this event has been replaced by ProcessRollup2.

**Platforms:** Windows

---

### ProcessRollup2

**Description:** This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats. Every ProcessRollup2 event contains a field called TargetProcessId. This ID is generated internally by the sensor, and will be unique for every instance of a process. For example, if you run cmd.exe twice, you will see two different ProcessRollup2 events with two unique values for TargetProcessId. This ID should not be confused with the host operating system PID for the process, which will be a different value. Processes often generate multiple, if not dozens of related events. For example, opening a browser or running an executable can generate network connectivity events, temporary file write events, DNS request events. We therefore need a way to understand the parent-child relationship between processes and the events they generate. Every event that is generated by a ProcessRollup2 contains a data field called ContextProcessId. The ContextProcessId will match the TargetProcessId of its parent ProcessRollup2 event. In the example below, the ContextProcessId values indicate that each of the events are children of the parent ProcessRollup2events. By searching for events that have matching values for ContextProcessId and TargetProcessId, you can see a list of all events that were generated as a result of a ProcessRollup2 event. As previously mentioned, every process that executes on a host has a corresponding ProcessRollup2 event. This means that when a process spawns another process, a brand new ProcessRollup2 event will be generated for that new ProcessRollup2event. This new event will contain a field called ParentProcessId. The ParentProcessId of the child PR2 will match the TargetProcessId of the parent PR2, as shown below : By searching for events that have matching values for ParentProcessId and TargetProcessId, you can determine the parent-child relationship of multiple ProcessRollup2 events. Platforms: macOS This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats. Every ProcessRollup2 event contains a field called TargetProcessId. This ID is generated internally by the sensor, and will be unique for every instance of a process. For example, if you run cmd.exe twice, you will see two different ProcessRollup2 events with two unique values for TargetProcessId. This ID should not be confused with the host operating system PID for the process, which will be a different value. Processes often generate multiple, if not dozens of related events. For example, opening a browser or running an executable can generate network connectivity events, temporary file write events, DNS request events, etc. We therefore need a way to understand the parent-child relationship between processes and the events they generate. Every event that is generated by a ProcessRollup2 contains a data field called ContextProcessId. The ContextProcessId will match the TargetProcessId of its parent ProcessRollup2 event. In the example below, the ContextProcessId values indicate that each of the events are children of the parent ProcessRollup2events. By searching for events that have matching values for ContextProcessId and TargetProcessId, you can see a list of all events that were generated as a result of a ProcessRollup2 event. As previously mentioned, every process that executes on a host has a corresponding ProcessRollup2 event. This means that when a process spawns another process, a brand new ProcessRollup2 event will be generated for that new ProcessRollup2event. This new event will contain a field called ParentProcessId. The ParentProcessId of the child PR2 will match the TargetProcessId of the parent PR2, as shown below : By searching for events that have matching values for ParentProcessId and TargetProcessId, you can determine the parent-child relationship of multiple ProcessRollup2 events. Platforms: Forensics, Windows Legacy, ChromeOS Platforms: Linux, Falcon Container, Android This event (often called "PR2" for short) is generated for a process that is running or has finished running on a host and contains information about that process. For every ProcessRollup2 event, there is a corresponding event that is generated when a process completes. The name of this event is EndOfProcess for Windows and Mac and TerminateProcess for Linux. Important: This event is generated on Windows, Mac, and Linux sensors. However, because of the way Mac and Linux manage processes at the kernel level, the Falcon sensors for these platforms are configured to send ProcessRollup2information in a second event called ProcessRollup2Stats. For more information, see ProcessRollup2Stats.

**Platforms:** Windows

---

### ProcessRollup2Stats

**Description:** Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only generates ProcessRollup2 events. When a process finishes running, the sensor generates and sends a ProcessRollup2 event. Mac sensors send far more ProcessRollup2 events than Windows (roughly 20x as many), so rather than send events for every process on those hosts, the sensor sends an initial ProcessRollup2 event, followed 10 minutes later by a ProcessRollup2Stats event with a SHA256 hash and the count of how many times the hash executed in the last 10 minutes. Platforms: Linux, Falcon Container Important: This event is generated on Mac and Linux Sensors only. The Falcon sensor for Windows only generates ProcessRollup2 events. When a process finishes running, the sensor generates and sends a ProcessRollup2 event. Linux sensors send far more ProcessRollup2 events than Windows (roughly 20x as many), so rather than send events for every process on those hosts, the sensor sends an initial ProcessRollup2 event, followed 60 minutes later by a ProcessRollup2Stats event with a SHA256 hash and the count of how many times the hash executed in the last 60 minutes.

**Platforms:** macOS

---

### ProcessSelfDeleted

**Description:** This event indicates when a process self-delete situation is detected. It will be thrown when a process deletes a file that was previously loaded as the primary module in an ancestor process. If the self-delete was accomplished via injecting into an already running process, ContextProcessId will be the injector as well.

**Platforms:** macOS, Windows, Linux

---

### ProcessSessionCreated

**Description:** 

**Platforms:** Linux, Falcon Container

---

### ProcessSignal

**Description:** 

**Platforms:** Linux

---

### ProcessState

**Description:** Running process observed at collection time.

**Platforms:** Forensics

---

### ProcessSubstituteUser

**Description:** 

**Platforms:** macOS

---

### ProcessTokenPrivilegesEdited

**Description:** 

**Platforms:** Windows

---

### ProcessTokenStolen

**Description:** An event that describes a process token stealing detection. ContextProcessId has been detected stealing the token of TargetProcessId.

**Platforms:** Windows

---

### ProcessTrace

**Description:** 

**Platforms:** Linux, Falcon Container

---

### ProcessTreeCompositionPatternTelemetry

**Description:** 

**Platforms:** Windows

---

### ProcessWitness

**Description:** Emitted when the sensor witnesses a process is running. This event is not an indication that a process just started, only that the process was first seen running when the event was sent. It is used for iOS where there is no way to be notified of processes start or running, or to query about running processes, and the sensor only knows a process exists when it makes a network connection. This event is therefore different from PR2s or SynPR2s.

**Platforms:** iOS

---

### PromiscuousBindIP4

**Description:** This is a reified NetworkBindIP4 indicating a socket is in promiscuous mode.

**Platforms:** Windows

---

### PromiscuousBindIP6

**Description:** 

**Platforms:** Windows

---

### ProtectVmEtw

**Description:** A virtual memory protect event generated from ETW data.

**Platforms:** Windows

---

### ProvisioningChannelVersionRequired

**Description:** This event informs the cloud about the state of a channel on the sensor during provisioning. It is only sent when the sensor is in an unprovisioned state. Platforms: Android, iOS

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ProvisioningEnded

**Description:** Sent when provisioning is completed.

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

### PtActivationStatus

**Description:** Reports host's compatibility with the Processor Trace feature.

**Platforms:** Windows

---

### PtTelemetry

**Description:** 

**Platforms:** Windows

---

### PtyAttached

**Description:** 

**Platforms:** Linux

---

### PtyCreated

**Description:** An event that notifies that a pty has been created.

**Platforms:** macOS

---

### PtyDetached

**Description:** 

**Platforms:** Linux

---

### PythonFileWritten

**Description:** 

**Platforms:** Windows

---

### QuarantineActionResult

**Description:** This event reports the result of a file quarantine triggered by Falcon Prevent.

**Platforms:** Linux, macOS, Windows

---

### QuarantinedFile

**Description:** This event is generated when a file is quarantined by Falcon Prevent.

**Platforms:** macOS, Linux, Windows

---

### QuarantinedFileState

**Description:** This event reports the state of a file quarantined by Falcon Prevent.

**Platforms:** macOS, Linux, Windows

---

### QuarantineXattribute

**Description:** 

**Platforms:** Forensics

---

### QueueApcEtw

**Description:** 

**Platforms:** Windows

---

### QuickAssistCookieInfo

**Description:** 

**Platforms:** Forensics

---

### QuickAssistDownloadEnded

**Description:** 

**Platforms:** Forensics

---

### QuickAssistDownloadStarted

**Description:** 

**Platforms:** Forensics

---

### QuickAssistHistoryVisit

**Description:** 

**Platforms:** Forensics

---

### RansomwareCreateFile

**Description:** A reified LocalFsPostCreate event so the cloud can route these events for ransomware support.

**Platforms:** Windows

---

### RansomwareFileAccessPattern

**Description:** Helper event for ransomware file access patterns.

**Platforms:** Windows

---

### RansomwareOpenFile

**Description:** A reified LocalFsPostCreate event so the cloud can route these events for ransomware support.

**Platforms:** Windows

---

### RansomwareRenameFile

**Description:** A reified LocalFsPostRename event so the cloud can route these events for ransomware support.

**Platforms:** Windows

---

### RarFileWritten

**Description:** Emitted when a process is done writing a RAR file.

**Platforms:** Windows, Linux, macOS

---

### RawBindIP4

**Description:** An event that is created when an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). It is a more specific version of the event NetworkBindIP4 indicating a socket is in raw mode. IPv4 is the source of the connection/connectionless protocol in this event. A NetworkBindIP4 event is created whenever an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). The event's ConnectionFlags field describes the parameters of that bind operation. A socket that is bound has not performed any network activity per se. Only a subsequent call to listen() or connect() generates network activity through the bound socket. The attributes of the bind, such as promiscuous mode or raw socket, are available in the ConnectionFlags field. Platforms: Forensics IPv4 network binding event. Terminating socket is in raw mode.

**Platforms:** Windows, Android, Linux, Falcon Container, macOS

---

### RawBindIP6

**Description:** An event that is created when an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). It is a more specific version of the event NetworkBindIP6 indicating a socket is in raw mode. IPv6 is the source of the connection/connectionless protocol in this event. A NetworkBindIP6 event is created whenever an application using a connection-oriented or connectionless protocol causes a port resource assignment to a socket through a call to bind(). The event's ConnectionFlags field describes the parameters of that bind operation. A socket that is bound has not performed any network activity per se. Only a subsequent call to listen() or connect() generates network activity through the bound socket. The attributes of the bind, such as promiscuous mode or raw socket, are available in the ConnectionFlags field. Platforms: Forensics IPv6 network binding event. Terminating socket is in raw mode.

**Platforms:** Linux, Falcon Container, Android, macOS, Windows

---

### RecentExecutionTimestamp

**Description:** Recent execution timestamp from a Forensics artifact.

**Platforms:** Forensics

---

### RecentlyModifiedFileExecutedInContainer

**Description:** Emitted by the Falcon sensor for Linux when: A new or modified binary executable is run in a container. A new or modified script is run in a container. Emitted by the Falcon Container sensor for Linux when: A new or modified binary executable is run in a container.

**Platforms:** Linux, Falcon Container

---

### RecoveryActionDeleteFilesComplete

**Description:** 

**Platforms:** Linux, Falcon Container, Kubernetes, macOS, Windows

---

### RecoveryActionDeleteFilesReply

**Description:** 

**Platforms:** macOS, Linux, Falcon Container, Kubernetes, Windows

---

### RecoveryActionGetModuleTableRecordComplete

**Description:** 

**Platforms:** macOS, Windows, Linux, Falcon Container

---

### RecoveryActionGetRuntimeSystemTagsComplete

**Description:** 

**Platforms:** macOS, Windows, Linux, Falcon Container

---

### RecoveryActionGetSystemTagsComplete

**Description:** 

**Platforms:** macOS, Linux, Falcon Container, Windows, Kubernetes

---

### RecoveryActionKillProcessesComplete

**Description:** 

**Platforms:** macOS, Linux, Falcon Container, Kubernetes, Windows

---

### RecoveryActionKillProcessesReply

**Description:** 

**Platforms:** Kubernetes, Linux, Falcon Container, macOS, Windows

---

### RecoveryActionManipulateModuleTableComplete

**Description:** 

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### RecoveryActionRegistryCreateKeyComplete

**Description:** 

**Platforms:** Windows

---

### RecoveryActionRegistryCreateKeyReply

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

### RecoveryActionRegistryDeleteValueKeyComplete

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

### RecoveryActionRegistrySetValueKeyReply

**Description:** 

**Platforms:** Windows

---

### RecoveryActionSetRuntimeSystemTagsComplete

**Description:** 

**Platforms:** macOS, Linux, Falcon Container, Windows

---

### RecoveryActionSetSystemTagsComplete

**Description:** 

**Platforms:** Linux, Falcon Container, macOS, Kubernetes, Windows

---

### ReflectiveDllLoaded

**Description:** An event that indicates that a user space thread reflectively loaded DLL.

**Platforms:** Windows

---

### ReflectiveDllOpenProcess

**Description:** A userspace thread attempted to open a process which appeared to originate from a reflectively loaded DLL.

**Platforms:** Windows

---

### ReflectiveDotnetModuleLoad

**Description:** Event generated when .NET module is reflectively (e.g. from a byte array) loaded in a process.

**Platforms:** Windows

---

### RegCredAccessDetectInfo

**Description:** 

**Platforms:** Windows

---

### RegCrowdstrikeKeyUpdate

**Description:** 

**Platforms:** Windows

---

### RegCrowdstrikeValueUpdate

**Description:** 

**Platforms:** Windows

---

### RegFeatureUsageInfo

**Description:** 

**Platforms:** Forensics

---

### RegGenericInfo

**Description:** Registry entry generic information.

**Platforms:** Forensics

---

### RegGenericKeyUpdate

**Description:** 

**Platforms:** Windows

---

### RegGenericValueUpdate

**Description:** An event that indicates that a registry value has been updated.

**Platforms:** Windows

---

### RegisterRawInputDevicesEtw

**Description:** An event that indicates that an application called the RegisterRawInputDevices API. Captured using the ETW consumer.

**Platforms:** Windows

---

### RegistryHiveFileWritten

**Description:** 

**Platforms:** Windows

---

### RegistryOperationBlocked

**Description:** An event that indicates that a registry operation has been blocked using a callback filter.

**Platforms:** Windows

---

### RegistryOperationDetectInfo

**Description:** An event that describes a registry operation blocked using a callback filter.

**Platforms:** Windows

---

### RegKeySecurityDecreasedFromUnsignedModule

**Description:** This event contains information about a protected registry security object whose security was decreased. It combines relevant information from the RegKeySecurityDecreased and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### RegNtPostOpenKeyEx

**Description:** Registry post open key operation event.

**Platforms:** Windows

---

### RegNtPostOpenKeyExUpImpersonating

**Description:** A reified RegNtPostOpenKeyEx event that occurred in the context of a thread up-impersonating another user, and the context process was not a privileged account.

**Platforms:** Windows

---

### RegShimCache

**Description:** Shim cache registry entry.

**Platforms:** Forensics

---

### RegSystemConfigKeyUpdate

**Description:** 

**Platforms:** Windows

---

### RegSystemConfigValueUpdate

**Description:** An event that indicates that a registry value related to system configuration or security has been updated.

**Platforms:** Windows

---

### RegValueQueryDetectInfo

**Description:** 

**Platforms:** Windows

---

### RemediationActionKillIP4Connection

**Description:** Sensor attempted to kill a connection to a malicious IPv4 address. No further data will be sent or received on the connection.

**Platforms:** iOS, Android

---

### RemediationActionKillIP6Connection

**Description:** Sensor attempted to kill a connection to a malicious IPv6 address. No further data will be sent or received on the connection.

**Platforms:** iOS, Android

---

### RemediationActionKillProcess

**Description:** Notification of a kill process remediation action attempted by the sensor. Platforms: macOS, Windows Legacy, Linux

**Platforms:** Windows

---

### RemediationActionQuarantineFile

**Description:** Notification of a quarantine file remediation action attempted by the sensor.

**Platforms:** Windows

---

### RemediationActionQuarantineMacroFile

**Description:** 

**Platforms:** Windows

---

### RemediationActionQuarantineOfficeMacroFile

**Description:** 

**Platforms:** Windows

---

### RemediationActionRegistryRemoval

**Description:** Notification of a registry persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### RemediationActionScheduledTaskRemoval

**Description:** Notification of a scheduled task persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### RemediationActionServiceRemoval

**Description:** Notification of a service persistence removal remediation action attempted by the sensor.

**Platforms:** Windows

---

### RemediationMonitorKillProcess

**Description:** Platforms: Windows Notification of a kill process remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Linux, macOS

---

### RemediationMonitorQuarantineFile

**Description:** Notification of a quarantine file remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### RemediationMonitorRegistryRemoval

**Description:** Notification of a registry persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### RemediationMonitorScheduledTaskRemoval

**Description:** Notification of a scheduled task persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### RemediationMonitorServiceRemoval

**Description:** Notification of a service persistence removal remediation action that would have been attempted by the sensor but wasn't because the remediation was in monitor mode.

**Platforms:** Windows

---

### RemoteBruteForceDetectInfo

**Description:** An event that describes a remote brute force detection.

**Platforms:** Windows

---

### RemoteCommandResponse

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### RemoteProcessMemoryRead

**Description:** 

**Platforms:** Linux

---

### RemoteProcessMemoryWrite

**Description:** 

**Platforms:** Linux

---

### RemoteThreadCreate

**Description:** 

**Platforms:** macOS

---

### RemovableDiskModuleLoadAttempt

**Description:** An event that indicates that a process with a primary image that is not on a removable disk attempted to load a module from a removable disk.

**Platforms:** Windows

---

### RemovableMediaFileWritten

**Description:** An event that is emitted for files written to removable media on Android devices.

**Platforms:** Android

---

### RemovableMediaVolumeMounted

**Description:** This event provides information about a removable media volume that was just mounted.

**Platforms:** Windows, Android

---

### RemovableMediaVolumeUnmounted

**Description:** An event that contains information about a removable media volume that was just unmounted.

**Platforms:** Android

---

### ResourceLimit

**Description:** 

**Platforms:** Linux

---

### ResourceUtilization

**Description:** Platforms: Linux, Falcon Container An event that contains CPU and RAM utilization data for a system. The event is sent when the sensor connects and every 15 minutes thereafter. Platforms: Windows An event that contains CPU and RAM utilization data for a system. The event is sent when the sensor connects, every 15 minutes thereafter, and in case any change in capacity is detected.

**Platforms:** macOS, Kubernetes

---

### RootkitDetectionResponse

**Description:** 

**Platforms:** Windows

---

### RouteIP4

**Description:** IPv4 Route entry.

**Platforms:** Forensics

---

### RouteIP6

**Description:** IPv6 Route entry.

**Platforms:** Forensics

---

### RpmFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

---

### RtfFileWritten

**Description:** Emitted when a process is done writing an RTF file.

**Platforms:** Windows, macOS, Linux

---

### RuntimeEnvironmentVariable

**Description:** Environment Variable provided to a process; In the context of falcon forensics, this is an environment variable provided to the collector process itself.

**Platforms:** Forensics

---

### SafetyNetCheckFailed

**Description:** An event that indicates the SafetyNet check could not be completed.

**Platforms:** Android

---

### SafetyNetCompatibilityStatus

**Description:** An event that contains the SafetyNet compatibility status obtained via the Google SafetyNet API.

**Platforms:** Android

---

### SafetyNetVerifyAppsStatus

**Description:** An event that contains information about the status of SafetyNet Verify Apps (Google Play Protect) on the device.

**Platforms:** Android

---

### SAMHashDumpFromUnsignedModule

**Description:** This event contains information about an unsigned module that accessed protected SAM account registry keys. It combines relevant information from the RegNtPostOpenKeyEx and SignInfoWithCertAndContext events

**Platforms:** Windows

---

### ScheduledTaskDeleted

**Description:** This event is sent when Falcon has detected that a scheduled task has been removed from the machine. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Note that the context here is not sufficient to determine full details on the task being removed (that is captured in ScheduledTaskRegistered), but does show the task name and originator info.

**Platforms:** Windows

---

### ScheduledTaskInfo

**Description:** Scheduled windows tasks.

**Platforms:** Forensics

---

### ScheduledTaskModified

**Description:** Event sent when EAEP has determined a new scheduled task was modified to the local machine. The RPC data will be for the furthest 'hop' away in an RPC connection. For instance, the 'at' command is 2 levels away from the schdsvc service. RegPostObjectName is used for DFA enhancing other fields, and isn't part of this events cloudable definition.

**Platforms:** Windows

---

### ScheduledTaskRegistered

**Description:** This event is sent when Falcon detects that a scheduled task has been added to the machine, either locally or remotely. This includes things added via the at command (at.exe) or scheduled tasks (schtasks.exe). The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. This service has multiple versions over time from Windows 7 to Windows 10, so some fields may not be available in all versions. The raw TaskXml will always be available, which should be a superset of the other ‘Task’ fields.

**Platforms:** Windows

---

### ScheduledTaskTamperingRegistryOperation

**Description:** 

**Platforms:** Windows

---

### ScheduledTaskTemplateDetectInfo

**Description:** 

**Platforms:** Windows

---

### ScreenshotTakenEtw

**Description:** An event that indicates that partial or full screenshot has been taken. Captured using the ETW consumer.

**Platforms:** Windows

---

### ScriptControlBlocked

**Description:** This event is sent when Falcon Host has blocked malicious script content from being executed on the machine. This event provides the details of exactly what content was blocked.

**Platforms:** Windows

---

### ScriptControlDetectInfo

**Description:** This event is sent when Falcon has detected malicious script content being executed on the host. This event provides the details of exactly what content was detected.

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### ScriptControlDetectInvalidInfo

**Description:** 

**Platforms:** macOS, Linux, Falcon Container

---

### ScriptControlDotNetMetadata

**Description:** Contains the last 56kb of ScriptContent from a .NET AMSI scan.

**Platforms:** Windows

---

### ScriptControlErrorEvent

**Description:** An event that contains telemetry data containing up to 56 KB ScriptContent field data from AMSI (AntiMalware Scan Interface) that has been deobfuscated.

**Platforms:** Windows

---

### ScriptControlScanInfo

**Description:** 

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### ScriptControlScanTelemetry

**Description:** 

**Platforms:** Windows

---

### ScriptFileContentsDetectInfo

**Description:** 

**Platforms:** Windows

---

### ScriptFileWrittenInfo

**Description:** 

**Platforms:** Windows

---

### SecureTrafficDecrypted

**Description:** An event that contains certificate info for the compromised network connection.

**Platforms:** Android, iOS

---

### SEHOverWriteAttempt

**Description:** An event that is emitted when a UserException event has failed a SEH (Structured Exception Handler) validation. The nature of the failure is described by the bitmask SEHValidationFailureFlags. Depending on the type of failure, ExceptionHandlerAddress field or ExceptionFrameAddress field may not be present.

**Platforms:** Windows

---

### SELinuxStatus

**Description:** An event that contains info about the SELinus status.

**Platforms:** Android

---

### SensitiveWmiQuery

**Description:** An event that indicates that a client process executed a sensitive WMI query.

**Platforms:** Windows

---

### SensorAntiTamperState

**Description:** 

**Platforms:** Windows

---

### SensorEnteredSafemode

**Description:** 

**Platforms:** Linux, Falcon Container, macOS, Windows

---

### SensorGroupingTagsUpdate

**Description:** 

**Platforms:** Windows, Android

---

### SensorHeartbeat

**Description:** Sent periodically to inform the cloud that the sensor is active. Platforms: Linux, Falcon Container Sent periodically to inform the cloud that the sensor is active. Platforms: ChromeOS, Windows Legacy, Vmcluster Platforms: Kubernetes

**Platforms:** Windows, macOS, Android, iOS

---

### SensorMetadataUpdate

**Description:** 

**Platforms:** Linux

---

### SensorSelfDiagnosticAlert

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### SensorSelfDiagnosticTelemetry

**Description:** 

**Platforms:** Windows, macOS, Linux

---

### SensorSettingsUpdate

**Description:** 

**Platforms:** Linux, Falcon Container, Windows, macOS, Kubernetes, Vmcluster

---

### SensorTampering

**Description:** Thrown when a tampering event occurs on the sensor.

**Platforms:** Linux

---

### ServicesStatusInfo

**Description:** Detailed information and status of a windows service. Platforms: Windows

**Platforms:** Forensics

---

### ServiceStarted

**Description:** This event is generated when a standalone service is started by the service control manager (SCM). ServiceDisplayName, TargetProcessId, ImageFileName and CommandLine are all for the new service. The data will indicate the initial process (command- line tool, custom utility, or GUI application) or remote address/host name that resulted in this action.

**Platforms:** Windows

---

### ServiceStopped

**Description:** This event is emitted when a standalone service is stopped by the service control manager (SCM). Unfortunately, the sensor is not currently capable of identifying who requested this operation. However, it can be used to confirm that this is a service stopping vs. a service crashing or being terminated.

**Platforms:** Windows

---

### SessionPatternTelemetry

**Description:** 

**Platforms:** macOS, Linux

---

### SetThreadCtxEtw

**Description:** 

**Platforms:** Windows

---

### SetWindowsHook

**Description:** An event that is sent from the sensor when a user mode program attempts to set a windows hook.

**Platforms:** Windows

---

### SetWindowsHookExEtw

**Description:** An event that indicates that an application called SetWinEventHookEx API. Captured using the ETW consumer.

**Platforms:** Windows

---

### SetWinEventHookEtw

**Description:** An event that indicates that an application called the SetWinEventHook API. Captured using the ETW consumer.

**Platforms:** Windows

---

### SevenZipFileWritten

**Description:** This event is generated when a 7ZIP file type (.7zip) is written to disk.

**Platforms:** macOS, Linux, Windows

---

### SharedObjectLoaded

**Description:** 

**Platforms:** Linux

---

### ShellBagFileTimeStampMetadata

**Description:** One event is emitted per timestamp from a ShellBag registry entry.

**Platforms:** Forensics

---

### ShellBagInfo

**Description:** Windows ShellBag MRU registry entry.

**Platforms:** Forensics

---

### ShellCommandLineInfo

**Description:** 

**Platforms:** Linux

---

### ShimDbTag

**Description:** A tag entry in the Shim database.

**Platforms:** Forensics

---

### SignInfo

**Description:** Sent by FalconForensicsCollector containing information about the signing-state of an image. Platforms: macOS, Windows

**Platforms:** Forensics

---

### SignInfoWithCertAndContext

**Description:** Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains information about the signing-state of an image.

**Platforms:** Windows, macOS

---

### SignInfoWithContext

**Description:** Sent by SignInfoActor as a response to the SignInfoRequestWithContext sent by the cloud. It contains information about the signing-state of an image.

**Platforms:** macOS, Windows

---

### SigningIdentity

**Description:** 

**Platforms:** iOS

---

### SigningPublicKey

**Description:** 

**Platforms:** Android, iOS

---

### SldFileWritten

**Description:** 

**Platforms:** Windows

---

### SmbClientNamedPipeConnectEtw

**Description:** An event that indicates when a machine connects to a remote SMB (Server Message Block) named pipe. The event contains the pattern id of the associated indicator and is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmbClientShareClosedEtw

**Description:** An event that indicates when a machine disconnects from a remote share. This event is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmbClientShareLogonBruteForceLowThreshold

**Description:** 

**Platforms:** Windows

---

### SmbClientShareLogonBruteForceSuspected

**Description:** 

**Platforms:** Windows

---

### SmbClientShareOpenedEtw

**Description:** An event that indicates when a machine connects to a remote share. This event is supported on all Windows platform except 8.1 and Server 2012 R2. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmbServerLocalNamedPipeOpenedEtw

**Description:** 

**Platforms:** Windows

---

### SmbServerShareOpenedEtw

**Description:** An event that indicates a remote machine opening a local share. This event is supported on all Windows platform except 8.1 and Server 2012 R2.

**Platforms:** Windows

---

### SmbServerV1AuditEtw

**Description:** An event that indicates that a client attempted to connect to this machine using the Server Message Block protocol, SMBv1. Captured using the ETW consumer.

**Platforms:** Windows

---

### SmtpAttachment

**Description:** 

**Platforms:** Linux

---

### SmtpCommand

**Description:** 

**Platforms:** Linux

---

### SmtpEmailMessage

**Description:** 

**Platforms:** Windows

---

### SnapshotVolumeMounted

**Description:** Information about a snapshot volume that was just mounted.

**Platforms:** Windows

---

### SourceCodeFileWritten

**Description:** 

**Platforms:** Windows, macOS

---

### SpotlightEntityBatch

**Description:** Single Event consisting of a list of Spotlight Entity State data packaged for optimal size and part of a larger set of batch events that will be processed in Cloud. Platforms: Linux

**Platforms:** Windows, macOS

---

### SpotlightEntityBatchHeader

**Description:** Spotlight Batch header to indicate all required metadata of incoming batch along with information to deal with possibilities of dropped subsequent events. Platforms: Linux

**Platforms:** Windows, macOS

---

### SpotlightEntitySystemState

**Description:** Spotlight Entity heart-beat event to notify cloud of current state with last synced batch and Channel file version information. Platforms: Linux

**Platforms:** Windows, macOS

---

### SpotlightSearchEntry

**Description:** Per-user spotlight search information.

**Platforms:** Forensics

---

### SruApplicationResourceUsage

**Description:** System Resource Utilization Monitor: application resource usage per user.

**Platforms:** Forensics

---

### SruApplicationTimelineProvider

**Description:** System Resource Utilization Monitor: application resource usage timeline.

**Platforms:** Forensics

---

### SruNetworkConnectivityUsage

**Description:** System Resource Utilization Monitor: connection time per local network interface, application and user tuple.

**Platforms:** Forensics

---

### SruNetworkDataUsage

**Description:** System Resource Utilization Monitor: bytes sent/received per local network interface, application and user tuple.

**Platforms:** Forensics

---

### SSHClientAuthenticated

**Description:** 

**Platforms:** Linux

---

### SsoApplicationAccess

**Description:** Indicates successful access to an application through an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS.

**Platforms:** Public Cloud

---

### SsoApplicationAccessFailure

**Description:** Indicates failed access to an application through an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS.

**Platforms:** Public Cloud

---

### SsoUserLogon

**Description:** Indicates an initial, successful sign-in to an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS.

**Platforms:** Public Cloud

---

### SsoUserLogonFailure

**Description:** Indicates an initial, failed sign-in to an SSO facilitator, which could be either an IDaaS directory, a federation portal, or a combination of both, such as Azure with AD-FS.

**Platforms:** Public Cloud

---

### StaticAnalysisContainerTelemetry

**Description:** Cloudable event in response to a telemetry query for the static analysis containers.

**Platforms:** Windows

---

### StaticConfigurationError

**Description:** 

**Platforms:** Linux

---

### StorageEncryptionStatus

**Description:** An event that contains information about the Device Storage encryption.

**Platforms:** Android

---

### SudoCommandAttempt

**Description:** 

**Platforms:** macOS

---

### SuperfetchAppInfo

**Description:** Application entry from Windows Superfetch AgForegroundAppHistory.db.

**Platforms:** Forensics

---

### SuperfetchAppSchedule

**Description:** Application running schedule/period recently updated from Windows Superfetch AgGlobalHistory.db.

**Platforms:** Forensics

---

### SuspectCreateThreadStack

**Description:** This event is used to indicate that suspicious data has been discovered in the context of a CreateThread attempt.

**Platforms:** Windows

---

### SuspendProcessError

**Description:** This event is emitted if KillProcessActor fails to suspend a process.

**Platforms:** macOS, Windows, Linux, Falcon Container

---

### SuspiciousAndroidActivityFound

**Description:** An event that indicates that a currently installed application on the device has been found providing a suspicious Android Activity.

**Platforms:** Android

---

### SuspiciousAndroidLogcatMessageFound

**Description:** An event that indicates that an application log message originating from a suspicious source has been found indicating the FalconMobile application might have been compromised and the device might have been rooted.

**Platforms:** Android

---

### SuspiciousAndroidStackTraceElementFound

**Description:** An event that indicates that a hooking framework has been found via stacktrace analysis and that the FalconMobile application might have been compromised.

**Platforms:** Android

---

### SuspiciousAndroidSystemPropertyFound

**Description:** An event that indicates that a suspicious system property has been found. This might indicate the OS Integrity has been tampered with which might mean the device has been rooted.

**Platforms:** Android

---

### SuspiciousAppFound

**Description:** An event that indicates that a suspicious application has been found to be installed on the device.

**Platforms:** Android

---

### SuspiciousCreateSymbolicLink

**Description:** An event that indicates the creation of a suspicious symbolic link.

**Platforms:** Windows

---

### SuspiciousCredentialModuleLoad

**Description:** An indicator event fired when suspicious credential module activity is detected, which means the process opened a handle to the LSASS process and loaded one of its DLLs for symbolic resolution of protected LSASS resources. The name of the DLL that was loaded is in the ImageFileName field This event also contains data from the offending application, whose name is stored in TargetFileName

**Platforms:** Windows

---

### SuspiciousDnsRequest

**Description:** This event is generated when the sensor detects a suspicious DNS request. A request is suspicious if it is attempting to send a request to a domain found on the sensor’s list of suspicious domains.

**Platforms:** Windows, Linux, macOS

---

### SuspiciousEseFileWritten

**Description:** This event indicates that a possible domain credential file (NTDS.dit) was copied from a volume snapshot.

**Platforms:** Windows

---

### SuspiciousLackOfProcessRollupEvents

**Description:** This event is emitted if we don't see any ProcessRollup2 events for a long time.

**Platforms:** Windows

---

### SuspiciousPeFileWritten

**Description:** A suspicious PE image file was written to disk.

**Platforms:** Windows

---

### SuspiciousPrivilegedProcessHandle

**Description:** Indicates a process has opened a handle to a privileged process with special access rights.

**Platforms:** Windows

---

### SuspiciousRawDiskRead

**Description:** This event indicates a process successfully read a target file using raw disk access.

**Platforms:** Windows

---

### SuspiciousRawDiskReadFromUnsignedModule

**Description:** This event contains information about an unsigned module reading a target file using raw disk access. It combines relevant information from the SuspiciousRawDiskRead and SignInfoWithCertAndContext events.

**Platforms:** Windows

---

### SuspiciousRegAsepUpdate

**Description:** An event that describes the registry activity that triggered a suspicious registry ASEP (Autostart Extension Point) detect.

**Platforms:** Windows

---

### SuspiciousUserFontLoad

**Description:** Sent when a UserFontLoad event has been blocked by the sensor.

**Platforms:** Windows

---

### SuspiciousUserRemoteAPCAttempt

**Description:** An event that indicates that a remote APC (Asynchronous Procedure Call) that is classified as potentially suspicious was queued on the target process by the context process.

**Platforms:** Windows

---

### SyntheticPR2Stats

**Description:** 

**Platforms:** macOS

---

### SyntheticProcessRollup2

**Description:** This event provides data similar to what is available in a ProcessRollup2. SyntheticProcessRollup2 events are generated for processes that started before the sensor does, such as during installation. Platforms: ChromeOS

**Platforms:** Windows, Linux, Falcon Container, macOS

---

### SyntheticProcessTrace

**Description:** 

**Platforms:** Linux

---

### SyntheticSharedObjectLoaded

**Description:** 

**Platforms:** Linux

---

### SyntheticSystemdServiceCreated

**Description:** 

**Platforms:** Linux

---

### SyntheticSystemdTimerCreated

**Description:** 

**Platforms:** Linux

---

### SyntheticVirtualMemoryArea

**Description:** 

**Platforms:** Linux

---

### SyscacheEntry

**Description:** An entry in windows syscache hive.

**Platforms:** Forensics

---

### SysConfigInfo

**Description:** 

**Platforms:** Linux, Falcon Container

---

### SystemCapacity

**Description:** An event that describes the CPU and RAM capacity of the system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in capacity is detected. Platforms: Linux An event that describes the CPU and RAM capacity data for a system. The event is sent when the sensor connects, every 24 hours thereafter, and in case any change in capacity is detected.

**Platforms:** Windows, macOS

---

### SystemdServiceCreated

**Description:** 

**Platforms:** Linux

---

### SystemdServiceDeleted

**Description:** 

**Platforms:** Linux

---

### SystemdServicePropertiesChanged

**Description:** 

**Platforms:** Linux

---

### SystemdTimerCreated

**Description:** 

**Platforms:** Linux

---

### SystemdTimerDeleted

**Description:** 

**Platforms:** Linux

---

### SystemdTimerPropertiesChanged

**Description:** 

**Platforms:** Linux

---

### SystemExtension

**Description:** Describes a macOS system extension identified by the collector.

**Platforms:** Forensics

---

### SystemPartitionAltered

**Description:** An event that indicates a system partition has been altered and is in an unexpected state.

**Platforms:** iOS

---

### SystemPartitionStatus

**Description:** An event that contains information about the device system partition. This event is deprecated as of Android sensor version 2021.09.3060002.

**Platforms:** Android

---

### SystemTokenStolen

**Description:** An event that indicates that system token stealing was detected.

**Platforms:** Windows

---

### SystemUpdatesBlockedByDNS

**Description:** Indicates that OS updates have been blocked via DNS.

**Platforms:** iOS

---

### SystemUpdatesBlockedByFilesystem

**Description:** Indicates that OS updates have been blocked via the filesystem.

**Platforms:** iOS

---

### SystemUpdatesBlockedByHTTP

**Description:** Indicates that OS updates have been blocked via HTTP.

**Platforms:** iOS

---

### TarFileWritten

**Description:** Emitted when a process is done writing a Tar file.

**Platforms:** macOS, Linux, Windows

---

### TccModification

**Description:** 

**Platforms:** macOS

---

### TcgPcrInfo

**Description:** An event that contains the Platform Configuration Register (PCR) values.

**Platforms:** Windows

---

### TerminalSavedStateInfo

**Description:** MacOS terminal saved state information.

**Platforms:** Forensics

---

### TerminateProcess

**Description:** This event is thrown when a process exits normally or is forcibly terminated. Platforms: ChromeOS

**Platforms:** Windows, macOS, Linux, Falcon Container

---

### TerminateRemoteProcessEtw

**Description:** 

**Platforms:** Windows

---

### ThreadBlocked

**Description:** Reports the status of a block thread attempt.

**Platforms:** Windows

---

### ThreadPreviousModeMismatch

**Description:** 

**Platforms:** Windows

---

### TiffFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

### TlsClientHello

**Description:** Platforms: macOS

**Platforms:** Linux, Windows

---

### TokenImpersonated

**Description:** An event that contains detailed before and after impersonation information for detection telemetry.

**Platforms:** Windows

---

### TrampolineDetected

**Description:** An event that indicates a C function has been tampered with. In iOS jailbreak, functions are modified by adding an unconditional trampoline in the first 4 words. FunctionName contains the function that has been determined to have been tampered with, ImageFileName contains the path to the image where the trampoline jumps to, and ExecutableBytes contains the first 4 words of the tampered-with function where the trampoline was detected.

**Platforms:** iOS

---

### TriggeredMemoryDumpResponse

**Description:** 

**Platforms:** Windows

---

### UACAxisElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target ActiveX Installation Service (AXIS).

**Platforms:** Windows

---

### UACCOMElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target COM object.

**Platforms:** Windows

---

### UACCredentialCaptureElevation

**Description:** This UAC event indicates the UAC consent.exe application was used by Windows to refresh the smart card credentials after a configurable timeout has expired.

**Platforms:** Windows

---

### UACExeElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target executable.

**Platforms:** Windows

---

### UACMSIElevation

**Description:** This UAC event indicates an attempt has been made to elevate the security privileges of a target MSI.

**Platforms:** Windows

---

### UmppaErrorEvent

**Description:** 

**Platforms:** Windows

---

### UmppcDetectInfo

**Description:** An event that describes a UMPPC-based detection.

**Platforms:** Windows

---

### UmppcEntryAnomaly

**Description:** 

**Platforms:** Windows

---

### UnclassifiedRegValueUpdate

**Description:** 

**Platforms:** Windows

---

### UncontainerizeAppResponse

**Description:** Sent in response to UncontainerizeApp, containing response information for the operation.

**Platforms:** Android

---

### UnexpectedDynamicLibraryLoaded

**Description:** An event that indicates that an unexpected dynamic library was loaded at runtime.

**Platforms:** iOS

---

### UnexpectedEnvironmentVariable

**Description:** An event that indicates some dangerous environment variables have made it to the app at runtime.

**Platforms:** iOS

---

### UnexpectedFileFound

**Description:** An event that indicates a file that should not exist on the device has been found. Platforms: Android An event that indicates a file that should not exist on the device has been found.

**Platforms:** iOS

---

### UnixFileWritten

**Description:** 

**Platforms:** Android

---

### UnixName

**Description:** 

**Platforms:** Linux

---

### UnsignedModuleLoad

**Description:** This event contains information about an unsigned module that was loaded into a target process. It combines relevant information from the ImageHash and SignInfoWithCertAndContext events for the unsigned module.

**Platforms:** Windows

---

### UpdateManifestDownloadComplete

**Description:** An update manifest download has completed.

**Platforms:** Windows

---

### UsbDeviceInfo

**Description:** Information on each USB device attachment.

**Platforms:** Forensics

---

### UserAccessLogEntry

**Description:** Per-user access log information for the year for a service role and IP address pair on Windows servers.

**Platforms:** Forensics

---

### UserAccount

**Description:** Describes an observed user account.

**Platforms:** Forensics

---

### UserAccountAddedToGroup

**Description:** This event is generated when an existing user account is added to an existing group. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. The group RID will indicate which group this user was added to. Of interest, for example, is a user being added to the “Administrators” group. Platforms: Linux

**Platforms:** Windows

---

### UserAccountCreated

**Description:** Platforms: Windows This event is generated when a new user account is created. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action.

**Platforms:** Linux

---

### UserAccountDeleted

**Description:** This event is generated when a user account is deleted. The data will indicate the initial process (command-line tool, custom utility, or GUI application) or remote address/hostname that resulted in this action. Platforms: Forensics User account deleted. Platforms: Linux

**Platforms:** Windows

---

### UserAccountRemovedFromGroup

**Description:** 

**Platforms:** Windows, Linux

---

### UserAssistAppLaunchInfo

**Description:** Application launched via user-assisted GUI menu.

**Platforms:** Forensics

---

### UserEatAccessMonitoring

**Description:** 

**Platforms:** Windows

---

### UserExceptionDEP

**Description:** This event is emitted when a userspace process is detected as having has a DEP or NX-related exception.

**Platforms:** Windows

---

### UserFontLoad

**Description:** An event that is sent when a user mode program attempts to add a font.

**Platforms:** Windows

---

### UserGroupCreated

**Description:** 

**Platforms:** Linux

---

### UserGroupDeleted

**Description:** 

**Platforms:** Linux

---

### UserIdentity

**Description:** The UserIdentity event is generated when a user logs in to a host. It conveys important security-related characteristics associated with a user to the CrowdStrike cloud, such as the user name. Platforms: Forensics, Linux

**Platforms:** Windows, macOS

---

### UserInformationEtw

**Description:** An event that indicates the password of a user was changed or set and other user information taken from UserLogonEtw.

**Platforms:** Windows

---

### UserLogoff

**Description:** This event is generated when a user logs off from a host. Platforms: ChromeOS, Linux

**Platforms:** macOS, Windows

---

### UserLogon

**Description:** This event is generated when a user logs on to a host. Platforms: ChromeOS

**Platforms:** Linux, macOS, Windows

---

### UserLogonFailed

**Description:** This event is generated when a user logon fails.

**Platforms:** Windows

---

### UserLogonFailed2

**Description:** An event that indicates that a local user attempted to logon, but failed due to bad password. LogonTime is the last successful logon time. The remote information will be present only if the logon originated over the network. RawProcessId will attribute a pid if relevant. Platforms: ChromeOS, macOS, Linux

**Platforms:** Windows

---

### UserSetProcessBreakOnTermination

**Description:** 

**Platforms:** Windows

---

### USNRecord

**Description:** 

**Platforms:** Forensics

---

### VdiFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### VerifyAppsDisabled

**Description:** This event has been deprecated.

**Platforms:** Android

---

### VirtualMemoryArea

**Description:** 

**Platforms:** Linux

---

### VMClusterInfo

**Description:** Event sent periodically to let the cloud know that the sensor is running with the following VM cluster data.

**Platforms:** Vmcluster

---

### VmcSensorStatus

**Description:** This event is sent to provide VMC sensor operational status.

**Platforms:** Vmcluster

---

### VmcVmAsset

**Description:** This event is sent to provide VMware vCenter VM information.

**Platforms:** Vmcluster

---

### VmdkFileWritten

**Description:** 

**Platforms:** macOS, Windows, Linux

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

**Platforms:** Windows

---

### VulnerableDriverDetectInfo

**Description:** 

**Platforms:** Windows

---

### WebScriptFileWritten

**Description:** 

**Platforms:** Linux, Windows, macOS

---

### WebShellDetected

**Description:** To identify webshell script files in a target folder, the content of each text file is matched against a large built-in list of regular expressions.

**Platforms:** Forensics

---

### WfpFilterTamperingFilterAdded

**Description:** This event is created whenever WFP indicates to our callout driver that a new filter that references one of our callout functions has been added to the Base Filtering Engine.

**Platforms:** Windows

---

### WfpFilterTamperingFilterDeleted

**Description:** This event is created whenever WFP indicates to our callout driver that a filter that references one of our callout functions has been deleted from the Base Filtering Engine.

**Platforms:** Windows

---

### WiFiConnect

**Description:** Sent when a device connects to a WiFi network. This event is only sent if the Connected Wi-Fi networks setting is enabled in Mobile Policies.

**Platforms:** Android, iOS

---

### WiFiDisconnect

**Description:** Sent when a device disconnects from a WiFi network. This event is only sent if the Connected Wi-Fi networks setting is enabled in Mobile Policies.

**Platforms:** Android, iOS

---

### WindowsTimelineEntry

**Description:** 

**Platforms:** Forensics

---

### WindowsTimelineEntryTimestamp

**Description:** 

**Platforms:** Forensics

---

### WlanInterfaceInfo

**Description:** 

**Platforms:** Forensics

---

### WmiCreateProcess

**Description:** Windows Management Instrumentation (WMI) is a default service installed on machines with Windows XP and newer. WMI is the infrastructure for management data and operations which allows a user to remotely manage machines and automate administrative tasks. WMI also supports scripting languages such as PowerShell and VBScript. Adversaries have utilized the WMI service to install implants, tools and perform credential theft via scripting in an effort to maneuver throughout customer environments. The Enhanced Attacker Execution Profiling (EAEP) event “WmiCreateProcess” will be useful in tracking the adversary’s lateral activity and/or origin of an attack during an intrusion. The Enhanced Attacker Execution Profiling (EAEP) event category focuses on gathering additional endpoint data on things like service creation, scheduled tasks, firewall rule modification, etc. This event is emitted when it is determined WMI was used to start a new process. ProcessRollup2 may also be updated to include RPC client information if available. There may be some known inconsistencies with attribution of the real RPC client data here, due to worker thread indirection that occurs within the WMI service process. If so, a later update will resolve those inconsistencies.

**Platforms:** Windows

---

### WmiFilterConsumerBindingEtw

**Description:** An event that is emitted when a WMI (Windows Management Instrumentation) consumer instance gets bound to a filter instance. Captured using the ETW consumer.

**Platforms:** Windows

---

### WmiProviderRegistrationEtw

**Description:** An event that is emitted when a WMI (Windows Management Instrumentation) provider gets registered. Captured using the ETW consumer.

**Platforms:** Windows

---

### WmiQuery

**Description:** Windows Management Instrumentation (WMI) query status.

**Platforms:** Forensics

---

### WmiQueryDetectInfo

**Description:** 

**Platforms:** Windows

---

### WroteExeAndGeneratedServiceEvent

**Description:** Indicates a process both wrote an executable and generated a service event.

**Platforms:** Windows

---

### WSLDistributionRegistered

**Description:** A user registers a Linux distribution but hasn’t started it yet.

**Platforms:** Windows

---

### WSLDistributionStarted

**Description:** The Linux distribution starts.

**Platforms:** Windows

---

### WSLDistributionStopping

**Description:** The Linux distribution is stopping.

**Platforms:** Windows

---

### WSLDistributionUnregistered

**Description:** A user unregisters a Linux distribution.

**Platforms:** Windows

---

### WSLMetadata

**Description:** 

**Platforms:** Linux

---

### WSLVMStarted

**Description:** The Linux Virtual Machine Root Namespace starts.

**Platforms:** Windows

---

### WSLVMStopping

**Description:** The Linux Virtual Machine Root Namespace is stopping.

**Platforms:** Windows

---

### XarFileWritten

**Description:** Emitted when a process is done writing a Xar file. macOS installer files are of this type.

**Platforms:** macOS, Linux, Windows

---

### XProtectAction

**Description:** 

**Platforms:** macOS

---

### XumdHookEvent

**Description:** 

**Platforms:** Windows

---

### XumdStatus

**Description:** 

**Platforms:** Windows

---

### XzFileWritten

**Description:** 

**Platforms:** macOS, Linux, Windows

---

### Yz1FileWritten

**Description:** 

**Platforms:** Windows

---

### ZerologonExploitAttempt

**Description:** 

**Platforms:** Windows

---

### ZipFileWritten

**Description:** This event is generated when a ZIP file type (.zip) is written to disk.

**Platforms:** Windows, macOS, Linux

---

### ZpaqFileWritten

**Description:** 

**Platforms:** Windows

---

### ZstdFileWritten

**Description:** 

**Platforms:** Linux, macOS, Windows

---

