# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from nipype.testing import assert_equal
from nipype.interfaces.freesurfer.utils import MRIsConvert

def test_MRIsConvert_inputs():
    input_map = dict(annot_file=dict(argstr='--annot %s',
    ),
    args=dict(argstr='%s',
    ),
    dataarray_num=dict(argstr='--da_num %d',
    ),
    environ=dict(nohash=True,
    usedefault=True,
    ),
    functional_file=dict(argstr='-f %s',
    ),
    ignore_exception=dict(nohash=True,
    usedefault=True,
    ),
    in_file=dict(argstr='%s',
    mandatory=True,
    position=-2,
    ),
    label_file=dict(argstr='--label %s',
    ),
    labelstats_outfile=dict(argstr='--labelstats %s',
    ),
    normal=dict(argstr='-n',
    ),
    origname=dict(argstr='-o %s',
    ),
    out_datatype=dict(mandatory=True,
    ),
    out_file=dict(argstr='./%s',
    genfile=True,
    position=-1,
    ),
    parcstats_file=dict(argstr='--parcstats %s',
    ),
    patch=dict(argstr='-p',
    ),
    rescale=dict(argstr='-r',
    ),
    scalarcurv_file=dict(argstr='-c %s',
    ),
    scale=dict(argstr='-s %.3f',
    ),
    subjects_dir=dict(),
    talairachxfm_subjid=dict(argstr='-t %s',
    ),
    terminal_output=dict(mandatory=True,
    nohash=True,
    ),
    vertex=dict(argstr='-v',
    ),
    xyz_ascii=dict(argstr='-a',
    ),
    )
    inputs = MRIsConvert.input_spec()

    for key, metadata in input_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(inputs.traits()[key], metakey), value

def test_MRIsConvert_outputs():
    output_map = dict(converted=dict(),
    )
    outputs = MRIsConvert.output_spec()

    for key, metadata in output_map.items():
        for metakey, value in metadata.items():
            yield assert_equal, getattr(outputs.traits()[key], metakey), value

