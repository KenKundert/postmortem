PostMortem: Generates Packets of Useful Information for Partners and Dependents to be Opened Upon Death
=======================================================================================================

| Version: 0.2.0
| Released: 2019-03-23
|

*PostMortem* works with `Avendesora <https://avendesora.readthedocs.io>`_ to 
produce packets of information for partners and dependents to help them carry on 
after your death or incapacitation.  Primarily *PostMortem* queries *Avendesora* 
to produce an encrypted document that contains information about all of your 
essential accounts including security credentials such as usernames and 
passcodes. It also can include related pre-prepared documents such as the legal 
documents that establish and control your estate.

Your partners and dependents do not need *PostMortem* to access their documents, 
however they must be capable of using *GPG* and have a GPG encryption key.

Please report all bugs and suggestions to postmortem@nurdletech.com

Getting Started
---------------

You download and install *PostMortem* with::

    pip3 install --user postmortem

Once installed, you will need a configuration file. The file is: 
~/.config/postmortem/config and should contain the following fields.

my_gpg_ids:

    A string that contains an identifier for your GPG key. This could be your 
    email address or a GPG ID. The output files will be encrypted with this key 
    as well as the keys of the intended recipients.

name_template:

    A python format string that specifies how the packet directory should be 
    named. It can include two named parameters, *name* and *now*. *name* is the 
    name of a recipient and now is and Arrow time object.

recipients:

    A dictionary of dictionary that contains preferences for each of the 
    recipients.

Here is an example config file::

    my_gpg_ids = 'odin@norse-gods.com'
    name_template = '{name}-{now:YYMMDD}'

    recipients = dict(
        frigg = dict(
            email = 'frigg@norse-gods.com',
            category = 'wife',
            extras = [
                '~/home/finances/estate
            ],
            networth = True,
        ),
        thor = dict(
            email = 'thor@norse-gods.com',
            category = 'kids',
            extras = [
                '~/home/finances/estate
            ],
        ),
        loki = dict(
            email = 'loki@norse-gods.com',
            category = 'kids',
            extras = [
                '~/home/finances/estate
            ],
        ),
    )

An encrypted file is created for each recipient. Each recipient should have an 
*email* or *gpg_id* that is associated with a known GPG key. Each recipient 
should all have a category. Your Avendesora accounts will be searched for 
a field named *postmortem_recipients*, which is a string or list. The account is 
included in the packet if the recipients category is contained in 
*postmortem_recipients*.  *extras* is a list of files or directories that are 
also included in the packet. Finally, if *networth* is specified and is True, 
then a networth summary is also included. *networth* may also be a profile name 
for the networth command, in which case that profile is used. The networth 
command is available from `Cryptocurrency 
<https://github.com/KenKundert/cryptocurrency>`_.


Running PostMortem
==================

You can generate a packet for a particular recipient using::

    postmortem thor

This creates the encrypted file that contains the packet. The packet can be 
extracted with::

    gpg -d thor-190101.tgz.gpg > thor-190101.tgz
    tar xf thor-190101.tgz

You can have *PostMortem* send the packet directly using email if *email* is 
given in the configuration file using::

    postmortem -s thor

Finally, if you do not specify a recipient, packets are created for all known 
recipients.
