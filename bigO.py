# Example to show data shape only.
domains = {
   "one.com": dict(policy="block"),
   "two.com": dict(policy="none"),
   "three.com": dict(policy="none"),
   "four.com": dict(policy="block")
}

def getBlockPolicyState(domains):
  policyArr = []
  numDomains = len(domains.keys())
  for x in range(numDomains):
    policy = domains.values()[x]["policy"]
    policyArr.append(policy)
  oneDomain = [True for policy in policyArr if policy == "block"]
  allDomains = all(policy == "block" for policy in policyArr)
  

def getBlockPolicyState(domains):
    policyArr = []
    numDomains = len(domains.keys())

    # This part could be simplified to have general 0(n)
    for x in range(numDomains): 
        policy = domains.values()[x]["policy"] 
        policyArr.append(policy) 

    oneDomain = [True for policy in policyArr if policy == "block"]
    allDomains = all(policy == "block" for policy in policyArr)
    return dict(oneDomain=oneDomain, allDomains=allDomains)

def getBlockPolicyState(domains):
    domains_values = domains.values() # O(n)
    # This way we avoid to perform a linear time operation for each value in the input data and we keep it 0(n)
    oneDomain = [True for domain in domains_values if domain.get("policy") == "block"] # O(n)
    allDomains = len(domains_values) == len(oneDomain) # O(1)
    return dict(oneDomain=oneDomain, allDomains=allDomains) # O(n)
