from ansible.module_utils.basic import AnsibleModule

def add(firstNumber, secondNumber):
    return firstNumber + secondNumber 

def main():
    
    module = AnsibleModule (
                argument_spec=dict(
                   firstInput=dict(type='float', required='yes'),
                   secondInput=dict(type='float', required='yes')
                )
             )
             
    firstNumber = module.params['firstInput']
    secondNumber = module.params['secondInput']

    response = add( firstNumber, secondNumber )

    module.exit_json(meta=response, changed=False)
    #module.fail_json(msg="Fatal error occurred.")

main()
