import os
import ctypes
import random
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
def out_red(text):
    print("\033[31m{}" .format(text))
def out_green(text):
    print("\033[32m{}" .format(text))
def out_white(text):
    print("\033[37m{}" .format(text))
print('This test consists of 31 questions.'+'\n'+'You need to answer questions in the following format e.g.: abc or ABC(without spaces).'+'\n'+'GOOD LUCK!')
print()
input('Press ENTER to start ')
sump = 0
l = list(range(0,31))
random.shuffle(l)
while True:
    qs = []
    qs.append('Which two componets are built into the vCenter Server Appliance 6.x?(Choose two.)'+'\n'+'A. vSphere Auto Deploy'+'\n'+'B. vCenter Converter'+'\n'+'C. vRealize Orchestrator'+'\n'+'D. VMware vSphere Update Manager')
    qs.append('VMware vRealize Log Insight can be configured to send notification events to which endpoint?'+'\n'+'A. vRealize Configuration Manager'+'\n'+'B. vRealize Operations Manager'+'\n'+'C. vRealize Infastructure Navigator'+'\n'+'D. vCenter Server')
    qs.append('Which two scenarios can cause a VM to appear orphaned in the vSphere Web Client? (Choose two.)'+'\n'+'A. The VM was removed from the vCenter Server.'+'\n'+'B. The VM had an unsuccessful migration within a vSphere DRS cluster.'+'\n'+'C. The ESXi host had an unsuccessful failover event in vSphere HA.'+'\n'+'D. The VM was unregistered from the ESXi host directly.')
    qs.append('What are two requirements needed to enable a 4 vCPU virtual machine with Fault Tolerance? (Choose two.)'+'\n'+'A. vSphere Enterprise Plus license'+'\n'+'B. 1 GbE uplink for FT logging network'+'\n'+'C. vSphere Standard license'+'\n'+'D. 10 GbE uplink for FT logging network')
    qs.append('A vSphere administrator has been tasked with ensuring that 500 virtual desktops are unable to communicate with one another, but can communicate with required services.'+'\n'+'Which two solutions does VMware recommend? (Choose two.)'+'\n'+'A. vSphere Host Firewall'+'\n'+'B. Private VLAN'+'\n'+'C. VMware NSX Distributed Firewall'+'\n'+'D. Port Filtering')
    qs.append('One of your virtual machines (VM) has performance issues and sometimes is unresponsive.'+'\n'+'Which VM file must be checked in order to find the root cause?'+'\n'+'A. vpxd.log'+'\n'+'B. ds.log'+'\n'+'C. vminst.log'+'\n'+'D. vmware.log')
    qs.append('Which two choices are valid ways to patch an ESXi host? (Choose two.)'+'\n'+'A. vRealize Operations Manager'+'\n'+'B. vSphere Update Manager'+'\n'+'C. configuring a Host Profile'+'\n'+'D. utilizing the esxcli Command Line Interface')
    qs.append('Which three installation methods are supported for a guest operating system within a virtual machine? (Choose three.)'+'\n'+'A. ISO image from the datastore'+'\n'+'B. CD-ROM'+'\n'+'C. ISO image from a Content Library'+'\n'+'D. ISO image from an external FTP Server'+'\n'+'E. ISO image from Update Manager repository')
    qs.append('When using vSAN, all the storage characteristics are specified by Storage Policies.'+'\n'+'Which parameter in vSAN Storage Policies can increase performance in a cache miss situation?'+'\n'+'A. Number of failures to tolerate'+'\n'+'B. Number of disk stripes per object'+'\n'+'C. Force provisioning'+'\n'+'D. Object space reservation (%)')
    qs.append('A vSphere administrator uses vMotion to migrate a virtual machine between two ESXi hosts and notices that they can no longer ping the VM.'+'\n'+'What is the cause?'+'\n'+'A. The destination host has an incorrect VLAN tag on the virtual machine port group for the VM.'+'\n'+'B. The destination host has two port groups with the same VLAN tag.'+'\n'+'C. There is an MTU mismatch.'+'\n'+'D. The virtual machine has RDMs attached.')
    qs.append('A vSphere administrator notices that sometimes they receive poor network throughput for multiple port groups that reside on a vSwitch with multiple physical'+'\n'+'uplinks (vmnics). The configuration on the ESXi host is identical to other hosts that are working properly in the same cluster.'+'\n'+'What should be done next?'+'\n'+'A. Add additional port groups the v Switch.'+'\n'+'B. Add additional resources to the virtual machines that are powered on.'+'\n'+'C. Restart Management agents in ESXi Direct Console User Interface (DCUI).'+'\n'+'D. Alter the failover order of the vmnics until a bad vmnic is found.')
    qs.append('A vSphere administrator sees the alarm:'+'\n'+'vSphere HA virtual machine failed to failover'+'\n'+'This occurred for a number of virtual machines on a particular ESXi host in a cluster with vSphere High Availability (HA) enabled. The virtual machines guest'+'\n'+'operating systems never reported a power event.'+'\n'+'What occurred?'+'\n'+'A. The virtual machines were vMotioned off of the ESXi host.'+'\n'+'B. The ESXi host failed and vSphere HA successfully failed over the virtual machines.'+'\n'+'C. The previous virtual machine cloning operations failed to complete.'+'\n'+'D. The ESXi host is still running but has disconnected from the network.')
    qs.append('What three steps are necessary to enable Jumbo Frames for use with an iSCSI storage array? (Choose three.)'+'\n'+'A. Configure the MTU on the VMKernel port.'+'\n'+'B. Configure the MTU on the virtual switch.'+'\n'+'C. Configure the MTU on the physical switch.'+'\n'+'D. Configure the MTU on the LAG group.'+'\n'+'E. Configure the MTU on the VTEP.')
    qs.append('A vSphere Administrator is tasked with implementing a production VMware vSAN cluster and has followed the design and sizing guide to correctly size the environment.'+'\n'+'Which two requirements represent valid VMware recommendations? (Choose two.)'+'\n'+'A. A disk group must be composed of more than one cache disk and at least one capacity disk.'+'\n'+'B. All-Flash configurations do not require a caching tier.'+'\n'+'C. A disk group must be composed of one cache disc and at least one capacity disk.'+'\n'+'D. The cache tier should be sized to no less than 10% of the capacity tier.')
    qs.append('What is required to create a vSphere Distributed Switch? (Choose two.)'+'\n'+'A. vSphere Enterprise Plus licensing is required.'+'\n'+'B. Login to the ESXi Host with the Root account.'+'\n'+'C. A minimum of two physical uplinks is required.'+'\n'+'D. The host is added to a vCenter Server.')
    qs.append('Which three steps deploy a virtual machine from a VM Template in the Content Library? (Choose three.)'+'\n'+'A. Right-click a VM Template and select New VM from This Template'+'\n'+'B. In the vSphere Web Client navigator, select vCenter Inventory Lists > VM templates in Folders.'+'\n'+'C. Using vSphere Host client, select vCenter Inventory Lists > Content Libraries.'+'\n'+'D. In the vSphere Web Client navigator, select vCenter Inventory Lists > Content Libraries.'+'\n'+'E. Select a Content Library, click Related Objects tab and click Templates.')
    qs.append('When trying to export the vApp to the OVF, the option is grayed out. What solution allows for the export of a vApp?'+'\n'+'A. The vApp is marked as Non-Exportable.'+'\n'+'B. Logout of the vSphere Client and use the vSphere WebClient.'+'\n'+'C. Change the portgroup where the VMs are connected to.'+'\n'+'D. PowerOff the vApp.')
    qs.append('Which two formats are supported for exporting a VM to a storage media? (Choose two.)'+'\n'+'A. EXE'+'\n'+'B. OVF'+'\n'+'C. OVA'+'\n'+'D. ISO')
    qs.append('Which two statements are true using Resource Pools? (Choose two.)'+'\n'+'A. Resource Pools require vSphere DRS to be enabled.'+'\n'+'B. Resource Pools compartmentalize all resource in a cluster.'+'\n'+'C. Resource Pools compartmentalize all resources in a datacenter.'+'\n'+'D. Resource Pools require vSphere HA to be enabled.')
    qs.append('Which two resource types can be limited on the vApp level? (Choose two.)'+'\n'+'A. Network'+'\n'+'B. CPU'+'\n'+'C. Storage'+'\n'+'D. Memory')
    qs.append('Which three virtual hardware configurations will allow snapshots? (Choose three.)'+'\n'+'A. 16+ vCPU'+'\n'+'B. full memory reservation'+'\n'+'C. Physical Mode RDMs'+'\n'+'D. Virtual Mode RDMs'+'\n'+'E. bus sharing')
    qs.append('A vSphere administrator is required to apply security hardening policies following the VMware vSphere Hardening Guide recommendations.'+'\n'+'Which tool enables native compliance reporting for these guidelines?'+'\n'+'A. VMware vCenter Server'+'\n'+'B. VMware vRealize Operations Manager'+'\n'+'C. VMware vSphere Update Manager'+'\n'+'D. VMware AirWatch')
    qs.append('A vSphere administrator takes a snapshot before logging into a VM to preserve the current state in case of a problem.'+'\n'+'Assumping this process is repeated every day for over 30 days, what two results will happen? (Choose two.)'+'\n'+'A. The virtual machine’s performance will decrease.'+'\n'+'B. The virtual machine can end up consumping more space on the datastore than assigned.'+'\n'+'C. The administrator will have backups for the entire month.'+'\n'+'D. The administrator has successfully cloned the VM 30 times.')
    qs.append('Which three options are available when applying a customization Specification to an existing virtual machine? (Choose three.)'+'\n'+'A. Create a specification'+'\n'+'B. Import a specification'+'\n'+'C. Modify a specification'+'\n'+'D. Select an existing specification.'+'\n'+'E. Create a specification from an existing specification.')
    qs.append('Which state does VMware recommend an ESXi host be in before removing the ESXi host from a DRS cluster?'+'\n'+'A. Powered off'+'\n'+'B. Quarantine mode'+'\n'+'C. Disconnected'+'\n'+'D. Maintenance mode')
    qs.append('Which three actions allow a VMware vSphere 6.x administrator to view vSphere log files? (Choose three.)'+'\n'+'A. Analyze the vSphere logs from the vRealize Log Insight user interface.'+'\n'+'B. Download the vSphere log bundles from the Direct Console User Interface (DCUI).'+'\n'+'C. Download the vSphere log bundles from vSphere Web Client connected to a vCenter Server system.'+'\n'+'D. View the vSphere log files from the vSphere Web Client Log Browser.'+'\n'+'E. Analyze the vSphere logs from the vRealize Operations user interface.')
    qs.append('A vSphere administrator wants to migrate a virtual machine with vMotion from one node to another in the same cluster, but when the destination server is specified,'+'\n'+'an error message is displayed.'+'\n'+'What might be wrong? (Choose two.)'+'\n'+'A. The destination host does not have access to the shared datastore.'+'\n'+'B. The hosts are licensed for vSphere Essentials Plus.'+'\n'+'C. The cluster is configured for EVC and the hosts are of the same processor family.'+'\n'+'D. The hosts have a dedicated vMotion VMKernel interface configured.'+'\n'+'E. The source host is not licensed for vMotion.')
    qs.append('Which two options are available when migrating a powered off VM and relocating the attached disks? (Choose two.)'+'\n'+'A. Raw Device Mapping Virtual compatibility'+'\n'+'B. Same format as source'+'\n'+'C. Thick Provision Eager Zeroed'+'\n'+'D. Raw Device Mapping Physical compatibility')
    qs.append('A VMware vSphere 6.x administrator is implementing a new eight-node cluster for business critical applications. Each server will be configured with two 10 GbE'+'\n'+'network adapters and will utilize iSCSI for storage on one subnet.'+'\n'+'Which feature is required to implement this solution?'+'\n'+'A. Storage DRS'+'\n'+'B. Network I/O Control'+'\n'+'C. VMKernel Port Binding'+'\n'+'D. LACP')
    qs.append('Which two options are valid to create vApp in the vSphere Environment? (Choose two.)'+'\n'+'A. Login using vSphere C# Client to the ESXi host, right click on the host and select Create new vApp.'+'\n'+'B. Login using vSphere Host Client to the ESXi host, right click on the host and select Create new vApp.'+'\n'+'C. Login using vSphere WebClient to the vCenter Server, right click on the Cluster and select Create new vApp.'+'\n'+'D. Login using vSphere WebClient to the vCenter Server, right click on the standalone ESXi host and select Create new vApp.')
    qs.append('Which function key command will allow a vSphere administrator to access ESXi shell?'+'\n'+'A. Alt + F12'+'\n'+'B. Alt + F1'+'\n'+'C. Alt + F2'+'\n'+'D. Alt + F11')
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in l:
        print(qs[i])
        if i == 0:
            a = input('Your answer: ')
            if a == 'ad' or a == 'AD' or a == 'da' or a == 'DA':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AD')
        elif i == 1:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 2:
            a = input('Your answer: ')
            if a == 'cd' or a == 'CD' or a == 'DC' or a == 'dc':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is CD')
        elif i == 3:
            a = input('Your answer: ')
            if a == 'ad' or a == 'AD' or a == 'DA' or a =='da':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AD')
        elif i == 4:
            a = input('Your answer: ')
            if a == 'bc' or a == 'BC' or a == 'cb' or a == 'CB':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BC')
        elif i == 5:
            a = input('Your answer: ')
            if a == 'd' or a == 'D':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is D')
        elif i == 6:
            a = input('Your answer: ')
            if a == 'bd' or a == 'BD' or a == 'DB' or a == 'db':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BD')
        elif i == 7:
            a = input('Your answer: ')
            if a == 'abd' or a == 'ABD' or a == 'adb' or a == 'ADB' or a == 'bad' or a == 'dab' or a == 'DAB' or a == 'bda' or a == 'BDA' or a == 'dba' or a == 'DBA':
                out_green('Correct')
                sump += 1
            elif a == 'BAD':
                out_green('Not really:) All fine! And that was correct answer')
            else:
                out_red('Wrong! Correct answer is ABD')
        elif i == 8:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 9:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 10:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 11:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 12:
            a = input('Your answer: ')
            if a == 'abc' or a == 'ABC' or a == 'acb' or a == 'ACB' or a == 'bac' or a == 'BAC' or a == 'bca' or a == 'BCA' or a == 'cba' or a == 'CBA' or a == 'cab' or a == 'CAB':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is ABC')
        elif i == 13:
            a = input('Your answer: ')
            if a == 'cd' or a == 'CD' or a == 'dc' or a == 'DC':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is CD')
        elif i == 14:
            a = input('Your answer: ')
            if a == 'ad' or a == 'AD' or a == 'da' or a == 'DA':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AD')
        elif i == 15:
            a = input('Your answer: ')
            if a == 'acd' or a == 'ACD' or a == 'adc' or a == 'ADC' or a == 'cad' or a == 'CAD' or a == 'cda' or a == 'CDA' or a == 'dac' or a == 'DAC' or a == 'dca' or a == 'DCA':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is ACD')
        elif i == 16:
            a = input('Your answer: ')
            if a == 'd' or a == 'D':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is D')
        elif i == 17:
            a = input('Your answer: ')
            if a == 'bc' or a == 'BC' or a == 'cb' or a == 'CB':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BC')
        elif i == 18:
            a = input('Your answer: ')
            if a == 'ab' or a == 'AB' or a == 'ba' or a == 'BA':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AB')
        elif i == 19:
            a = input('Your answer: ')
            if a == 'bd' or a == 'BD' or a == 'db' or a == 'DB':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BD')
        elif i == 20:
            a = input('Your answer: ')
            if a == 'abd' or a == 'ABD' or a == 'adb' or a == 'ADB' or a == 'bad' or a == 'dab' or a == 'DAB' or a == 'bda' or a == 'BDA' or a == 'dba' or a == 'DBA':
                out_green('Correct')
                sump += 1
            elif a == 'BAD':
                out_green('Not really:) All fine! And that was correct answer')
            else:
                out_red('Wrong! Correct answer is ABD')
        elif i == 21:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        elif i == 22:
            a = input('Your answer: ')
            if a == 'ab' or a == 'AB' or a == 'BA' or a == 'ba':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AB')    
        elif i == 23:
            a = input('Your answer: ')
            if a == 'abd' or a == 'ABD' or a == 'adb' or a == 'ADB' or a == 'bad' or a == 'dab' or a == 'DAB' or a == 'bda' or a == 'BDA' or a == 'dba' or a == 'DBA':
                out_green('Correct')
                sump += 1
            elif a == 'BAD':
                out_green('Not really:) All fine! And that was correct answer')
            else:
                out_red('Wrong! Correct answer is ABD')
        elif i == 24:
            a = input('Your answer: ')
            if a == 'd' or a == 'D':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is D')
        elif i == 25:
            a = input('Your answer: ')
            if a == 'acd' or a == 'ACD' or a == 'adc' or a == 'ADC' or a == 'cad' or a == 'CAD' or a == 'cda' or a == 'CDA' or a == 'dac' or a == 'DAC' or a == 'dca' or a == 'DCA':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is ACD')
        elif i == 26:
            a = input('Your answer: ')
            if a == 'ad' or a == 'AD' or a == 'DA' or a == 'da':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is AD')
        elif i == 27:
            a = input('Your answer: ')
            if a == 'bc' or a == 'BC' or a == 'CB' or a == 'cb':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BC')
        elif i == 28:
            a = input('Your answer: ')
            if a == 'c' or a == 'C':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is C')
        elif i == 29:
            a = input('Your answer: ')
            if a == 'bc' or a == 'BC'or a == 'CB' or a == 'cb':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is BC')
        elif i == 30:
            a = input('Your answer: ')
            if a == 'b' or a == 'B':
                out_green('Correct')
                sump += 1
            else:
                out_red('Wrong! Correct answer is B')
        out_white('')
        input('Press ENTER to continue')
        os.system('cls' if os.name == 'nt' else 'clear')
    print("Your result is ", end = '')
    if int((100/31)*sump) >= 80:
        out_green('')
        print(int((100/31)*sump),end = '')
    else: 
        out_red('')
        print(int((100/31)*sump),end = '')
    out_white('%')
    print()
    r = input("Press 'r' to restart or any other key to end the test"+'\n')
    if r == 'r':
        os.system('cls' if os.name == 'nt' else 'clear')
        continue
    else:
        break





















