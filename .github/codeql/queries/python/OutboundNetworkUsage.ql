/**
 * @name Plugin outbound network capability use
 * @description Selected HTTP and socket connection APIs require Dispatcharr's outbound_network capability in enforcing manifests.
 * @kind problem
 * @problem.severity warning
 * @precision medium
 * @id plugin/capability-contract/outbound-network
 * @tags security external/cwe/cwe-269
 */

import python

from Call call, Attribute function, Name module
where
  call.getFunc() = function and
  (
    function.getName() = "connect" or
    (
      function.getObject() = module and
      module.getId() = "requests" and
      function.getName() in ["get", "post", "put", "patch", "delete", "request"]
    )
  )
select call, "This outbound network operation requires the `outbound_network` capability in a runtime-enforcing plugin manifest."
