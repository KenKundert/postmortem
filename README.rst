PostMortem: Generates Packets of Useful Information for Partners and Dependents to be Opened Upon Death
=======================================================================================================


.. image:: https://img.shields.io/pypi/v/postmortem.svg
    :target: https://pypi.python.org/pypi/postmortem

.. image:: https://img.shields.io/pypi/pyversions/postmortem.svg
    :target: https://pypi.python.org/pypi/postmortem


| Author: Ken Kundert
| Version: 0.5.2
| Released: 2020-10-13
| Please post all questions, suggestions, and bug reports to
  `Github Issues <https://github.com/KenKundert/postmortem/issues>`_.
|

*PostMortem* works with `Avendesora <https://avendesora.readthedocs.io>`_ to 
produce packets of information for partners and dependents to help them carry on 
after your death or incapacitation.  Primarily *PostMortem* queries *Avendesora* 
to produce an encrypted document that contains information about all of your 
essential accounts including security credentials such as usernames and 
passcodes. It also can include related pre-prepared documents such as the legal 
documents that establish and control your estate.

Your partners and dependents do not need *PostMortem* or *Avendesora* to access 
their documents, however they must be capable of using *GPG* and have a GPG 
encryption key.  However, if they do use happen to use *Avendesora*, they can 
import the accounts you shared with them directly into *Avendesora*.

Please report all bugs and suggestions to postmortem@nurdletech.com

Getting Started
---------------

You download and install *PostMortem* with::

    pip3 install --user postmortem

Once installed, you will need a configuration file. The file is: 
~/.config/postmortem/config.nt and should contain the following fields.

my gpg ids
    A string that contains an identifier for your GPG key. This could be your 
    email address or a GPG ID. The output files will be encrypted with this key 
    as well as the keys of the intended recipients.

sign with
    A string that contains an identifier of the GPG key you wish to use when 
    signing the generated archives.  If not given, your archives are not signed.  
    You will also need to specify *avendesora gpg passphrase account* so that 
    your key can be unlocked.

avendesora gpg passphrase account
    The name of the account that holds the passphrase of the GPG signing key.

avendesora gpg passphrase field
    The name of the account field that holds the passphrase of the GPG signing 
    key.  If not given, it is assumed to be a passcode field.

name template
    A python format string that specifies how the packet directory should be 
    named. It can include two named parameters, *name* and *now*. *name* is the 
    name of a recipient and now is and Arrow time object.

recipients
    A dictionary of dictionary that contains preferences for each of the 
    recipients.

The configuration is a `NestedText <https://nestedtext.org>`_ file.
Here is an example config file::

    my gpg ids: odin@norse-gods.com
    sign with: @ my gpg ids
    name template: {name}-{now:YYMMDD}
    estate docs:
        - ~/home/estate/trust.pdf
        - ~/home/estate/will.pdf
        - ~/home/estate/deed-valhalla.pdf

    recipients:
        frigg:
            email: frigg@norse-gods.com
            category: wife
            attach: @ estate docs
            networth: odin
        thor:
            email: thor@norse-gods.com
            category: kids
            attach: @ estate docs
        loki:
            email: loki@norse-gods.com
            category: kids
            attach: @ estate docs

Notice that *estate docs* was defined at the top level, but it is not 
a *PostMortem* setting. It simply defines a value that will be interpolated into 
a setting later. The interpolation is done by adding ``@`` to the name of the 
value. So for example, in the recipients *attach* is specified as ``@estate 
docs``.  This causes the list of estate documents to be used as attachments.  
The same thing is done in *sign with*, which interpolates *my gpg ids*.

Two encrypted files are created for each recipient, one is an encrypted text 
file that contains your account information, the other is an encrypted 
Avendesora account file. Both of these files contain the same information.  Each 
recipient should have an *email* or *gpg_id* that is associated with a known GPG 
key. Each recipient should also belong to a category.  Your Avendesora accounts 
are searched for a field named *postmortem_recipients*, which is a string or 
list.  The account is included in the packet if the recipients category is 
contained in *postmortem_recipients*.  *attach* is a list of files or 
directories that are also included in the packet.  Finally, if *networth* is 
specified and is True, then a networth summary is also included.  *networth* may 
also be a profile name for the networth command, in which case that profile is 
used. The networth command is available from `GitHub 
<https://github.com/KenKundert/networth>`_.


Running PostMortem
------------------

You can generate a packet for a particular recipient using::

    postmortem thor

This creates the encrypted file that contains the packet. The packet can be 
extracted with::

    gpg -d -o thor-190101.tgz thor-190101.tgz.gpg
    tar zxf thor-190101.tgz

or, in a single step using::

    gpg -d -o - thor-190101.tgz.gpg | tar zxf -

You can have *PostMortem* send the packet directly using email if *email* is 
given in the configuration file using::

    postmortem -s thor

Finally, if you do not specify a recipient, packets are created for all known 
recipients.


Importing Accounts into Avendesora
----------------------------------

Once you have extracted the files from a packet you will see a file named 
*avendesora_acounts.gpg*.  This is an *Avendesora* accounts file. If you use 
*Avendesora* you can import the accounts using these two steps:

1. Copy the file into your *Avendesora* accounts directory. You may rename the 
   file, but keep the extension the same.  For example::

       mv avendesora_acounts.gpg ~/.config/avendesora/parents.gpg

2. Edit the *Avendesora* accounts file and add your new file to the 
   *accounts_files* list::

       vi ~/.config/avendesora/accounts_files

Once you have done this you may find that there are conflicting names or aliases 
for your *Avendesora* accounts. For example, if both you and your parents use 
*Nordea* bank, the name *nordea* might conflict. In this case you should adjust 
the names and aliases used in your newly imported accounts file. None of the 
secrets in the imported file are generated, and so changing the account names in 
this file will change the underlying secrets.


Releases
--------

Latest Development Version
    | Version: 0.5.2
    | Released: 2020-10-13

0.6 (2020-10-14)
    - Improve sanity checking on settings.
    - Rename extras setting to attach.

0.5 (2020-10-12)
    - Switch to using NestedText for config file.

0.4 (2020-03-06)
    - Add README to repository.
    - Sign the archives, generate the unpack script.

0.3 (2019-04-28)
    - Add generation of avendesora_accounts.gpg file.

0.2 (2019-03-23)
    - Bug fixes.

0.0 (2019-01-31)
    - Initial version
