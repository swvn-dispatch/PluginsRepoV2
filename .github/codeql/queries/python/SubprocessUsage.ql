/**
 * @name Plugin subprocess capability use
 * @description Calling a subprocess API requires Dispatcharr's subprocess capability in enforcing manifests.
 * @kind problem
 * @problem.severity warning
 * @precision high
 * @id plugin/capability-contract/subprocess
 * @tags security external/cwe/cwe-269
 */

import python

from Call call, Attribute function, Name module
where
  call.getFunc() = function and
  function.getObject() = module and
  module.getId() = "subprocess" and
  function.getName() in ["Popen", "run", "call", "check_call", "check_output"]
select call, "This subprocess call requires the `subprocess` capability in a runtime-enforcing plugin manifest."
