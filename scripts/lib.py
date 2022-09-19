from datetime import date
import logging
import os
import subprocess

from scripts.import_test_functions import *


def setup_logging(verbose):
    """Setup the root logger.

    Args:
      verbose: Verbose logging
    """
    if verbose:
        logging.basicConfig(
            format="%(asctime)s %(filename)s:%(lineno)-5s %(levelname)-8s %(message)s",
            datefmt='%a, %d %b %Y %H:%M:%S',
            level=logging.DEBUG)
    else:
        logging.basicConfig(format="%(asctime)s %(levelname)-8s %(message)s",
                            datefmt='%a, %d %b %Y %H:%M:%S',
                            level=logging.INFO)


def create_output(instr, output):
    """ Create output directory

    Args:
      instr: Name of instruction
      output : Name of specified output directory

    Returns:
      Output directory
    """
    # Create output directory
    if output is None:
        output = str(date.today()) + "-" + instr
    os.system("rm -rf {}".format(output))

    logging.info("Creating output directory: {}".format(output))
    subprocess.run(["mkdir", "-p", output])

    return output


def create_cgf_path(instr, type, rvv_atg_root, output_dir):
    """ Create CGF path among exsiting CGF Files, and copy it to `output_dir`

    Args:
      instr : Name of instruction

    Returns:
      CGF path
    """
    p = str(rvv_atg_root) + "/cgfs/" + str(type) + "/" + str(instr) + ".yaml"
    os.system("cp %s %s" % (p, output_dir))
    logging.info("Finding CGF for: {} in {}.".format(instr, p))

    return p


def create_empty_test(instr, xlen, vlen, vsew, lmul, vta, vma, output_dir):
    """Create an empty test file to generate coverage report, and put empty test into `output_dir`

    Args:
      instr     : Instruction name
      xlen      : XLEN
      vlen      : Length of each vector registers, decide elements of one vector
      vsew      : Selected element width, decide width of operands and elements of one vector
      lmul      : Vector register group multiplier, decide vector registers
      vta       : Vector tail agnostic policy, decide expect results
      vma       : Vector mask elements agnostic policy, decide expect results
      output_dir: Output dir of this execution

    Return:
    Test file path
    """
    func_str = "create_empty_test_{}(xlen, vlen, vsew, lmul, vta, vma, output_dir)".format(
        instr)
    return eval(func_str)


def create_first_test(instr, xlen, vlen, vsew, lmul, vta, vma, output_dir, rpt_path):
    """Create an test file with all operands needing to be tested in the coverage report, but the expected answer is using 0x5201314, and put empty test into `output_dir`

    Args:
      instr     : Instruction name
      xlen      : XLEN
      vlen      : Length of each vector registers, decide elements of one vector
      vsew      : Selected element width, decide width of operands and elements of one vector
      lmul      : Vector register group multiplier, decide vector registers
      vta       : Vector tail agnostic policy, decide expect results
      vma       : Vector mask elements agnostic policy, decide expect results
      output_dir: Output dir of this execution
      rpt_path  : Path of coverate report
    Return:
    Test file path
    """
    func_str = "create_first_test_{}(xlen, vlen, vsew, lmul, vta, vma, output_dir, rpt_path)".format(
        instr)
    return eval(func_str)

def check_type(ins, type):
  return True