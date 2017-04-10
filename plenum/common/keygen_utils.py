import os

from plenum.common.stacks import nodeStackClass
from stp_zmq.util import createCertsFromKeys

from plenum.common.constants import CLIENT_STACK_SUFFIX


def initLocalKeys(name, baseDir, sigseed, override=False, config=None):
    pubkey, verkey = nodeStackClass.initLocalKeys(name, baseDir, sigseed,
                                            override=override)
    print("Public key is", pubkey)
    print("Verification key is", verkey)
    return pubkey, verkey


def initRemoteKeys(name, baseDir, sigseed, verkey, override=False, config=None):
    nodeStackClass.initRemoteKeys(name, baseDir, sigseed, verkey,
                                            override=override)


def initNodeKeysForBothStacks(name, baseDir, sigseed, override=False, config=None):
    nodeStackClass.initLocalKeys(name, baseDir, sigseed, override=override)
    nodeStackClass.initLocalKeys(name + CLIENT_STACK_SUFFIX, baseDir, sigseed,
                       override=override)


def areKeysSetup(name, baseDir, config=None):
    return nodeStackClass.areKeysSetup(name, baseDir)


def learnKeysFromOthers(baseDir, nodeName, otherNodes):
    otherNodeStacks = []
    for otherNode in otherNodes:
        if otherNode.name != nodeName:
            otherNodeStacks.append(otherNode.nodestack)
            otherNodeStacks.append(otherNode.clientstack)
    nodeStackClass.learnKeysFromOthers(baseDir, nodeName, otherNodeStacks)


def tellKeysToOthers(node, otherNodes):
    otherNodeStacks = []
    for otherNode in otherNodes:
        if otherNode != node:
            otherNodeStacks.append(otherNode.nodestack)
            otherNodeStacks.append(otherNode.clientstack)

    node.nodestack.tellKeysToOthers(otherNodeStacks)
    node.clientstack.tellKeysToOthers(otherNodeStacks)
