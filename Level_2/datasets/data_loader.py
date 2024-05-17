#import pandas as pd
import numpy as np
import os
PATH = os.getcwd()
PATH+="\Level_2"
print(PATH)
import ast
def call_graph_loop_of(benchmark):
    if benchmark=='Raytrace':
        return  {'magnitude': [('dot', 1)], 'normalized': [('scale', 1), ('magnitude', 1)], 'scene': [('vector', 1)],
     'bench_raytrace': [('scene', 100), ('addLight', 100), ('vector', 100), ('addLight', 100), ('vector', 100),
                        ('lookAt', 100), ('vector', 100), ('addObject', 100), ('sphere', 100), ('vector', 100),
                        ('simpleSurface', 100), ('addObject', 600), ('sphere', 600), ('vector', 600),
                        ('simpleSurface', 600), ('scale', 600), ('normalized', 600), ('vector', 600)],
     'main': [('bench_raytrace', 1)]}
    elif benchmark=='Pascal':
        return  {'pascal_upp': [], 'pascal_low': [('pascal_upp', 1)], 'pascal_sym': [],
     'printMatrixes': [('printMatrix', 1), ('pascal_upp', 1), ('printMatrix', 1), ('pascal_low', 1), ('printMatrix', 1),
                       ('pascal_sym', 1)], 'nextperm': [], 'perm3': [('nextperm', 1)],
     'main': [('perm3', 1), ('printMatrixes', 1000)]}
    elif benchmark=='Nbody':
        return  {'combinations': [], 'advance': [], 'bench_nbody': [('offset_momentum', 1), ('report_energy', 1), ('advance', 1), ('report_energy', 1)], 'main': [('bench_nbody', 1)]}
    elif benchmark=='Sieve':
        return  {'make_stream': [], 'stream_unfold': [('stream_first', 1), ('stream_rest', 1)], 'stream_get': [('stream_unfold', 1), ('stream_get', 1)], 'count_from': [('make_stream', 1), ('count_from', 1)], 'sift': [('stream_unfold', 1), ('sift', 1), ('make_stream', 1), ('sift', 1)], 'sieve': [('stream_unfold', 1), ('make_stream', 1), ('sieve', 1), ('sift', 1)], 'primes': [('sieve', 1), ('count_from', 1)], 'main': [('stream_get', 1), ('primes', 1)]}
    elif benchmark=='Meteor':
        return  {'permute': [('rotate', 50), ('flip', 880)], 'convert': [], 'get_footprints': [], 'get_senh': [], 'get_puzzle': [('permute', 1), ('convert', 1)], 'solve': [('solve', 120)], 'bench_meteor_contest': [('solve', 4)], 'main': [('get_puzzle', 1), ('get_footprints', 1), ('get_senh', 1), ('bench_meteor_contest', 1)]}
    elif benchmark=='Scimark':
        return  {'array2d': 30.009999999999998, 'idx': 0.43, 'getitem': 23.200000000000003, 'setitem': 0, 'SOR_execute': 22175.82, 'bench_SOR': 34.068, 'main': 1.29, 'array2dpar0': 0, 'array2dpar1': 0, 'idxpar0': 0, 'idxpar1': 0, 'idxpar2': 0, 'getitempar0': 0, 'getitempar1': 1, 'setitempar0': 0, 'setitempar1': 0, 'setitempar2': 0, 'SOR_executepar0': 0, 'SOR_executepar1': 0, 'SOR_executepar2': 0, 'bench_SORpar0': 0, 'bench_SORpar1': 0, 'bench_SORpar2': 0}
    elif benchmark=='Monte':
        return {'initialize': 92.39000000000003, 'rand': 17.73, 'nextDouble': 75.96, 'MonteCarlo': 4641.290000000001, 'main': 32.348, 'initializepar0': 1, 'initializeparReturnStatement': 0, 'initializepar1': 0, 'randpar0': 0, 'randparReturnStatement': 0, 'nextDoublepar0': 1, 'nextDoubleparReturnStatement': 200, 'MonteCarlopar0': 0, 'MonteCarloparReturnStatement': 0}

    elif benchmark=="Chaos":
        return {'GVector__init__': 3.1620000000000004, 'GVectorMag': 49.36100000000001, 'GVectordist': 14.448, 'GVector__add__': 224.41999999999993, 'GVector__sub__': 29.65, 'GVector__mul__': 67.75, 'GVectorlinear_combination': 33.824, 'GVector__str__': 38.53000000000001, 'GetKnots': 0.86, 'Spline__init__': 24.375999999999994, 'SplineGetDomain': 20.42, 'Spline__call__': 245881.68000000005, 'SplineGetIndex': 1261.006, 'Spline__len__': 11.350000000000001, 'Spline__repr__': 34.480000000000004, 'write_ppm': 0.86, 'Chaosgame__init__': 20988.644000000004, 'Chaosgameget_random_trafo': 152.13200000000003, 'Chaosgametransform_point': 139.54999999999995, 'Chaosgametruncate': 92.19200000000002, 'Chaosgamecreate_image_chaos': 157.28900000000002, 'main': 368.85750000000036, 'add_cmdline_args': 68.76400000000001}
    elif benchmark=="Richard":
        return {'Packet__init__': 51.0235, 'Packetappend_to': 2.926, 'DeviceTaskRec__init__': 1.054, 'IdleTaskRec__init__': 2.108, 'HandlerTaskRec__init__': 2.108, 'HandlerTaskRecworkInAdd': 12.576, 'HandlerTaskRecdeviceInAdd': 12.576, 'WorkerTaskRec__init__': 2.108, 'TaskState__init__': 3.1620000000000004, 'TaskStatepacketPending': 3.1620000000000004, 'TaskStatewaiting': 3.1620000000000004, 'TaskStaterunning': 3.1620000000000004, 'TaskStatewaitingWithPacket': 3.1620000000000004, 'TaskStateisPacketPending': 0.624, 'TaskStateisTaskWaiting': 0.624, 'TaskStateisTaskHolding': 0.624, 'TaskStateisTaskHoldingOrWaiting': 1.8719999999999999, 'TaskStateisWaitingWithPacket': 1.8719999999999999, 'trace': 19.68, 'TaskWorkArea__init__': 50.28600000000001, 'Task__init__': 66.00800000000001, 'Taskfn': 0, 'TaskaddPacket': 14.878, 'TaskrunTask': 46.36600000000001, 'TaskwaitTask': 1.054, 'Taskhold': 10.778000000000002, 'Taskrelease': 13.006000000000002, 'Taskqpkt': 33.434, 'Taskfindtcb': 46.480000000000004, 'DeviceTask__init__': 0, 'DeviceTaskfn': 55.818000000000005, 'HandlerTask__init__': 0, 'HandlerTaskfn': 96.26799999999997, 'IdleTask__init__': 0.86, 'IdleTaskfn': 58.74400000000001, 'WorkTask__init__': 0, 'WorkTaskfn': 50.148000000000025, 'schedule': 63.480000000000004, 'Richardsrun': 1011.3719999999993, 'pascal_upp': 79.902, 'pascal_low': 136.28, 'pascal_sym': 7.642000000000001, 'printMatrix': 0, 'printMatrixes': 145.33100000000002, 'nextperm': 1.72, 'perm3': 287.72, 'main': 1.417} 
    elif benchmark=="Pdf":
        return {'__init____Class': 0.624, 'data_bytes__Class': 40.894, 'poly__Class': 52.364, '_get_crc16_ccitt__Class': 20.552999999999997, 'get_crc_hex_string__Class': 11.261000000000001, 'pil_image__Class': 11.134, 'compression_type__Class': 61.434, '_get_binary_byte_count__Class': 10.704, '_get_bytes_per_row__Class': 1.248, '_get_graphic_field_count__Class': 11.952000000000002, '_get_data_string__Class': 76.203, 'get_graphic_field__Class': 10.157, 'image__Class': 51.598, 'invert__Class': 41.754, 'dither__Class': 41.754, 'threshold__Class': 72.044, 'width__Class': 52.364, 'height__Class': 52.364, 'pos_x__Class': 52.364, 'pos_y__Class': 52.364, 'complete_zpl__Class': 41.754, 'to_zpl__Class': 2475128.5999999996, 'pdf_bytes__Class': 40.894, 'zpl_data__Class': 41.754, '_match_dimensions__Class': 18.16, 'to_images__Class': 243.758, 'to_pdf__Class': 559413.5199999998, 'TestZebrafy_read_static_file__Class': 66.56799999999998, 'TestZebrafytest_version__Class': 11.564, 'TestZebrafytest_crc_data_bytes__Class': 42.428, 'TestZebrafytest_crc_poly__Class': 34.025999999999996, 'TestZebrafytest_graphic_field_image__Class': 42.428, 'TestZebrafytest_graphic_field_compression_type__Class': 55.578, 'TestZebrafytest_zebrafy_image_image__Class': 42.428, 'TestZebrafytest_zebrafy_image_compression_type__Class': 55.578, 'TestZebrafytest_zebrafy_image_invert__Class': 43.82, 'TestZebrafytest_zebrafy_image_dither__Class': 43.82, 'TestZebrafytest_zebrafy_image_threshold__Class': 67.33600000000001, 'TestZebrafytest_zebrafy_image_height__Class': 43.82, 'TestZebrafytest_zebrafy_image_pos_x__Class': 43.82, 'TestZebrafytest_zebrafy_image_complete_zpl__Class': 43.82, 'TestZebrafytest_image_to_default_zpl__Class': 53.756, 'TestZebrafytest_image_to_gfa_zpl__Class': 53.276, 'TestZebrafytest_image_to_zpl_invert__Class': 53.276, 'TestZebrafytest_image_to_zpl_invert_no_dither__Class': 53.276, 'TestZebrafytest_image_to_zpl_no_dither__Class': 53.276, 'TestZebrafytest_image_to_zpl_threshold_high__Class': 53.276, 'TestZebrafytest_image_to_zpl_width_height__Class': 53.276, 'TestZebrafytest_image_to_zpl_pos_x_pos_y__Class': 53.276, 'TestZebrafytest_multiple_image_to_zpl__Class': 53.276, 'TestZebrafytest_zebrafy_pdf_pdf_bytes__Class': 42.428, 'TestZebrafytest_zebrafy_pdf_compression_type__Class': 56.488, 'TestZebrafytest_zebrafy_pdf_invert__Class': 44.73, 'TestZebrafytest_zebrafy_pdf_dither__Class': 44.73, 'TestZebrafytest_zebrafy_pdf_threshold__Class': 68.24600000000001, 'TestZebrafytest_zebrafy_pdf_width__Class': 44.73, 'TestZebrafytest_zebrafy_pdf_pos_x__Class': 44.73, 'TestZebrafytest_zebrafy_pdf_complete_zpl__Class': 44.73, 'TestZebrafytest_pdf_to_default_zpl__Class': 53.756, 'TestZebrafytest_pdf_to_gfc_zpl__Class': 53.276, 'TestZebrafytest_pdf_to_zpl_no_dither__Class': 53.276, 'TestZebrafytest_pdf_to_zpl_threshold_low__Class': 53.276, 'TestZebrafytest_pdf_to_zpl_threshold_high__Class': 53.276, 'TestZebrafytest_pdf_to_zpl_width_height__Class': 53.276, 'TestZebrafytest_zebrafy_zpl_zpl_data__Class': 42.428, 'TestZebrafytest_gfa_zpl_to_image__Class': 85.388, 'TestZebrafytest_broken_zpl_gf_to_image__Class': 42.622, 'TestZebrafytest_broken_zpl_gfc_crc_to_image__Class': 42.622, 'TestZebrafytest_broken_zpl_gfc_compression_to_image__Class': 42.622, 'TestZebrafytest_gfb_zpl_to_pdf__Class': 74.06}
    elif benchmark=="Benchfirst":
        return {'GVector__init____Class': 3.1620000000000004, 'GVectorMag__Class': 49.36100000000001, 'GVectordist__Class': 14.448, 'GVector__add____Class': 126.61399999999995, 'GVector__sub____Class': 0, 'GVector__mul____Class': 67.75, 'GVectorlinear_combination__Class': 33.824, 'GVector__str____Class': 38.53000000000001, 'Spline__init____Class': 55.282000000000004, 'SplineGetDomain__Class': 77.75, 'Spline__call____Class': 817821.075, 'SplineGetIndex__Class': 57.73700000000001, 'Spline__len____Class': 11.350000000000001, 'Spline__repr____Class': 34.480000000000004, 'write_ppm': 3440.86, 'Chaosgame__init____Class': 152322.93000000002, 'Chaosgameget_random_trafo__Class': 162.42800000000003, 'Chaosgametransform_point__Class': 169.19999999999996, 'Chaosgametruncate__Class': 55.792000000000016, 'Chaosgamecreate_image_chaos__Class': 373.83500000000004, 'main_2_to_3': 102.37400000000001, 'main_bm_chameleon': 152.62299999999996, 'f': 0, 'bench_mp_pool': 33.671, 'bench_thread_pool': 33.671, 'main_concurrent': 48.54999999999999, 'fibonacci': 0, 'bench_coverage': 54.38, 'main_bm_coverage': 21.871, 'bench_pyaes': 44138.778000000006, 'main_bm_crypto_pyaes': 21.313999999999997, 'main_call_chaos': 1019.9444999999993, 'add_cmdline_args': 68.76400000000001, 'main_chaos': 72.67200000000001, 'write_ppmpar0': 0, 'write_ppmparReturnStatement': 0, 'write_ppmpar1': 0, 'fpar0': 0, 'fparReturnStatement': 0, 'bench_mp_poolpar0': 0, 'bench_mp_poolparReturnStatement': 0, 'bench_mp_poolpar1': 0, 'bench_mp_poolpar2': 0, 'bench_thread_poolpar0': 0, 'bench_thread_poolparReturnStatement': 0, 'bench_thread_poolpar1': 0, 'bench_thread_poolpar2': 0, 'fibonaccipar0': 0, 'fibonacciparReturnStatement': 0, 'bench_coveragepar0': 0, 'bench_coverageparReturnStatement': 0, 'bench_pyaespar0': 0, 'bench_pyaesparReturnStatement': 0, 'main_call_chaospar0': 0, 'main_call_chaosparReturnStatement': 0, 'main_call_chaospar1': 0, 'add_cmdline_argspar0': 0, 'add_cmdline_argsparReturnStatement': 0, 'add_cmdline_argspar1': 0}
    elif benchmark=="Cpu":
        return {'Trace__init____Class': 77.466, 'Traceheader__Class': 43.870000000000005, 'Tracesuccess__Class': 43.440000000000005, 'Tracefail__Class': 221.803, 'Tracecommand_header__Class': 43.870000000000005, 'Tracecommand_output__Class': 95.28799999999998, 'Tracekeys__Class': 592.6160000000002, 'Tracewrite__Class': 23.71, 'Traceto_dict__Class': 84.10999999999999, 'DataSourcehas_proc_cpuinfo__Class': 11.758, 'DataSourcehas_dmesg__Class': 0.43, 'DataSourcehas_var_run_dmesg_boot__Class': 76.842, 'DataSourcehas_cpufreq_info__Class': 0.43, 'DataSourcehas_sestatus__Class': 0.43, 'DataSourcehas_sysctl__Class': 0.43, 'DataSourcehas_isainfo__Class': 0.43, 'DataSourcehas_kstat__Class': 0.43, 'DataSourcehas_sysinfo__Class': 65.084, 'DataSourcehas_lscpu__Class': 0.43, 'DataSourcehas_ibm_pa_features__Class': 0.43, 'DataSourcehas_wmic__Class': 70.6735, 'DataSourcecat_proc_cpuinfo__Class': 47.4735, 'DataSourcecpufreq_info__Class': 47.4735, 'DataSourcesestatus_b__Class': 47.4735, 'DataSourcedmesg_a__Class': 47.4735, 'DataSourcecat_var_run_dmesg_boot__Class': 47.4735, 'DataSourcesysctl_machdep_cpu_hw_cpufrequency__Class': 47.4735, 'DataSourceisainfo_vb__Class': 47.4735, 'DataSourcekstat_m_cpu_info__Class': 47.4735, 'DataSourcesysinfo_cpu__Class': 47.4735, 'DataSourcelscpu__Class': 47.4735, 'DataSourceibm_pa_features__Class': 57.634, 'DataSourcewmic_cpu__Class': 47.4735, 'DataSourcewinreg_processor_brand__Class': 10.704, 'DataSourcewinreg_vendor_id_raw__Class': 0, 'DataSourcewinreg_arch_string_raw__Class': 0, 'DataSourcewinreg_hz_actual__Class': 0.557, 'DataSourcewinreg_feature_bits__Class': 0, '_program_paths': 1385933.924, '_run_and_get_stdout': 187.58999999999995, '_read_windows_registry_key': 76.45400000000001, '_check_arch': 34.267, '_obj_to_b64': 32.972, '_b64_to_obj': 70.303, '_utf_to_str': 223.046, '_copy_new_fields': 116806.3775, '_get_field_actual': 353146.51, '_get_field': 11.194, '_to_decimal_string': 121.74400000000004, '_hz_short_to_full': 165.65000000000003, '_hz_friendly_to_full': 165.99300000000002, '_hz_short_to_friendly': 98.21200000000002, '_to_friendly_bytes': 137.103, '_friendly_bytes_to_int': 137.086, '_parse_cpu_brand_string': 134.503, '_parse_cpu_brand_string_dx': 32924.9665, '_parse_dmesg_output': 571.7020000000002, '_parse_arch': 174.8970000000001, '_is_bit_set': 0.43, '_is_selinux_enforcing': 67.60200000000002, '_filter_dict_keys_with_empty_values': 326.841, 'ASM__init____Class': 71.372, 'ASMcompile__Class': 357.51800000000026, 'ASMrun__Class': 10.704, 'ASMfree__Class': 62.146000000000015, 'CPUID__init____Class': 89.814, 'CPUID_asm_func__Class': 97.72999999999999, 'CPUID_run_asm__Class': 36.324, 'CPUIDget_vendor_id__Class': 91.272, 'CPUIDget_info__Class': 61.495999999999995, 'CPUIDget_max_extension_support__Class': 11.134, 'CPUIDget_flags__Class': 485.6810000000005, 'CPUIDget_processor_brand__Class': 98.8415, 'CPUIDget_cache__Class': 193.566, 'CPUIDnew_func__Class': 55.004000000000005, 'CPUIDget_ticks_func__Class': 113.93599999999999, 'CPUIDget_raw_hz__Class': 53.326, '_get_cpu_info_from_cpuid_actual': 420.1709999999999, '_get_cpu_info_from_cpuid_subprocess_wrapper': 42.932999999999986, '_get_cpu_info_from_cpuid': 745.2630000000006, '_get_cpu_info_from_proc_cpuinfo': 484.7860000000005, '_get_cpu_info_from_cpufreq_info': 493.5770000000001, '_get_cpu_info_from_lscpu': 485.4770000000003, '_get_cpu_info_from_dmesg': 268.309, '_get_cpu_info_from_ibm_pa_features': 593.1730000000007, '_get_cpu_info_from_cat_var_run_dmesg_boot': 184.953, '_get_cpu_info_from_sysctl': 508.7370000000004, '_get_cpu_info_from_sysinfo': 10.704, '_get_cpu_info_from_sysinfo_v1': 570.7400000000002, 'get_subsection_flags': 57.634, '_get_cpu_info_from_sysinfo_v2': 389.4909999999999, '_get_cpu_info_from_wmic': 742.0540000000004, 'is_set': 0.43, '_get_cpu_info_from_registry': 320.13199999999995, '_get_cpu_info_from_kstat': 791.7410000000008, '_get_cpu_info_from_platform_uname': 337.496, '_get_cpu_info_internal': 1108.3639999999998, 'get_cpu_info_json': 64.36, 'get_cpu_info': 10.224, 'main': 954.2320000000021, '_program_pathspar0': 0, '_program_pathsparReturnStatement': 0, '_run_and_get_stdoutpar0': 0, '_run_and_get_stdoutparReturnStatement': 0, '_run_and_get_stdoutpar1': 0, '_read_windows_registry_keypar0': 0, '_read_windows_registry_keyparReturnStatement': 0, '_read_windows_registry_keypar1': 0, '_obj_to_b64par0': 0, '_obj_to_b64parReturnStatement': 0, '_b64_to_objpar0': 0, '_b64_to_objparReturnStatement': 0, '_utf_to_strpar0': 0, '_utf_to_strparReturnStatement': 0, '_copy_new_fieldspar0': 0, '_copy_new_fieldsparReturnStatement': 0, '_copy_new_fieldspar1': 0, '_get_field_actualpar0': 0, '_get_field_actualparReturnStatement': 0, '_get_field_actualpar1': 0, '_get_field_actualpar2': 0, '_get_fieldpar0': 0, '_get_fieldparReturnStatement': 0, '_get_fieldpar1': 0, '_get_fieldpar2': 1, '_get_fieldpar3': 0, '_to_decimal_stringpar0': 0, '_to_decimal_stringparReturnStatement': 0, '_hz_short_to_fullpar0': 0, '_hz_short_to_fullparReturnStatement': 2, '_hz_short_to_fullpar1': 0, '_hz_friendly_to_fullpar0': 0, '_hz_friendly_to_fullparReturnStatement': 0, '_hz_short_to_friendlypar0': 0, '_hz_short_to_friendlyparReturnStatement': 0, '_hz_short_to_friendlypar1': 0, '_to_friendly_bytespar0': 0, '_to_friendly_bytesparReturnStatement': 0, '_friendly_bytes_to_intpar0': 0, '_friendly_bytes_to_intparReturnStatement': 0, '_parse_cpu_brand_stringpar0': 0, '_parse_cpu_brand_stringparReturnStatement': 8, '_parse_cpu_brand_string_dxpar0': 0, '_parse_cpu_brand_string_dxparReturnStatement': 0, '_parse_dmesg_outputpar0': 0, '_parse_dmesg_outputparReturnStatement': 0, '_parse_archpar0': 0, '_parse_archparReturnStatement': 5, '_is_bit_setpar0': 0, '_is_bit_setparReturnStatement': 0, '_is_bit_setpar1': 0, '_is_selinux_enforcingpar0': 0, '_is_selinux_enforcingparReturnStatement': 0, '_filter_dict_keys_with_empty_valuespar0': 0, '_filter_dict_keys_with_empty_valuesparReturnStatement': 0, '_get_cpu_info_from_cpuid_subprocess_wrapperpar0': 0, '_get_cpu_info_from_cpuid_subprocess_wrapperparReturnStatement': 0, '_get_cpu_info_from_cpuidparReturnStatement': 1, '_get_cpu_info_from_proc_cpuinfoparReturnStatement': 1, '_get_cpu_info_from_cpufreq_infoparReturnStatement': 1, '_get_cpu_info_from_lscpuparReturnStatement': 1, '_get_cpu_info_from_dmesgparReturnStatement': 1, '_get_cpu_info_from_ibm_pa_featuresparReturnStatement': 1, '_get_cpu_info_from_cat_var_run_dmesg_bootparReturnStatement': 1, '_get_cpu_info_from_sysctlparReturnStatement': 1, '_get_cpu_info_from_sysinfoparReturnStatement': 1, 'get_subsection_flagspar0': 0, 'get_subsection_flagsparReturnStatement': 0, '_get_cpu_info_from_wmicparReturnStatement': 1, '_get_cpu_info_from_registryparReturnStatement': 1, 'is_setpar0': 0, 'is_setparReturnStatement': 0, '_get_cpu_info_from_kstatparReturnStatement': 1, '_get_cpu_info_from_platform_unameparReturnStatement': 1}
    elif benchmark=="Raytrace_TRANS":
        return {'vector': 0, 'dot': 2, 'magnitude': 3.7, 'scale': 1, 'normalized': 1, 'sphere': 0, 'scene': 1, 'lookAt': 1, 'addObject': 2.7, 'addLight': 3.7, 'simpleSurface': 0, 'bench_raytrace': 700, 'main': 17.2}
    elif benchmark=="Pascal_TRANS":
        return {'pascal_upp': 36006, 'pascal_low': 1, 'pascal_sym': 24006, 'printMatrix': 0, 'printMatrixes': 0, 'nextperm': 0, 'perm3': 0, 'main': 0}
    elif benchmark=="Sieve_TRANS":
        return {'Stream__init____Class': 0, 'stream_first': 1.7, 'stream_rest': 1.7, 'make_stream': 2.4, 'stream_unfold': 1, 'stream_get': 1, 'stream_take': 1, 'count_from': 0, 'sift': 1, 'sieve': 1, 'primes': 0, 'main': 0}
    elif benchmark=="Richard_TRANS":
        return {'Packet__init____Class': 0, 'Packetappend_to__Class': 13.6, 'DeviceTaskRec__init____Class': 0, 'IdleTaskRec__init____Class': 0, 'HandlerTaskRec__init____Class': 0, 'HandlerTaskRecworkInAdd__Class': 10.5, 'HandlerTaskRecdeviceInAdd__Class': 10.5, 'WorkerTaskRec__init____Class': 0, 'TaskState__init____Class': 0, 'TaskStatepacketPending__Class': 0, 'TaskStatewaiting__Class': 0, 'TaskStaterunning__Class': 0, 'TaskStatewaitingWithPacket__Class': 0, 'TaskStateisPacketPending__Class': 1.7, 'TaskStateisTaskWaiting__Class': 1.7, 'TaskStateisTaskHolding__Class': 1.7, 'TaskStateisTaskHoldingOrWaiting__Class': 5.1, 'TaskStateisWaitingWithPacket__Class': 5.1, 'trace': 2, 'TaskWorkArea__init____Class': 0, 'Task__init____Class': 23.999999999999996, 'Taskfn__Class': 0, 'TaskaddPacket__Class': 9.5, 'TaskrunTask__Class': 24.399999999999995, 'TaskwaitTask__Class': 0, 'Taskhold__Class': 5.1, 'Taskrelease__Class': 11.5, 'Taskqpkt__Class': 26.099999999999994, 'Taskfindtcb__Class': 21.399999999999995, 'DeviceTask__init____Class': 0, 'DeviceTaskfn__Class': 15.899999999999999, 'HandlerTask__init____Class': 0, 'HandlerTaskfn__Class': 49.500000000000014, 'IdleTask__init____Class': 0, 'IdleTaskfn__Class': 27.799999999999994, 'WorkTask__init____Class': 0, 'WorkTaskfn__Class': 72.7, 'schedule': 810405.4, 'Richardsrun__Class': 170.20000000000005, 'pascal_upp': 36006, 'pascal_low': 1, 'pascal_sym': 24006, 'printMatrix': 0, 'printMatrixes': 2, 'nextperm': 42, 'perm3': 5, 'main': 0}
    elif benchmark=="Meteor_TRANS":
        return {'rotate': 0, 'flip': 0, 'permute': 881, 'convert': 377, 'get_footprints': 18854, 'get_senh': 50, 'get_puzzle': 6, 'solve': 1578.0, 'bench_meteor_contest': 6, 'main': 3}
    elif benchmark=="Scimark_TRANS":
        return {'array2d': 3, 'idx': 2, 'getitem': 1, 'setitem': 5, 'SOR_execute': 2839, 'bench_SOR': 17.2, 'main': 0}
def retrunDatasets(benchmark,linesFile1,linesFile2):
    X_arr, y_arr = {}, {}
    x_filename = ""
    y_filename = ""
    for i in range(len(linesFile1)):
        if i % 2 == 0:
            x_filename = linesFile1[i]
        else:
            data = ast.literal_eval(linesFile1[i])
            X_arr[x_filename] = data
    for i in range(len(linesFile2)):
        if i % 2 == 0:
            y_filename = linesFile2[i]
        else:
            y_arr[y_filename] = float(linesFile2[i])
    X = []
    y = []
    for key in X_arr:
        X.append(X_arr[key])
        y.append(y_arr[key])
    call_graph=call_graph_loop_of(benchmark)
    cn = 0
    dictionary = {}
    for key in call_graph:
        if key not in dictionary:
            dictionary[key] = cn
            cn += 1
        for val in call_graph[key]:
            if val[0] not in dictionary:
                dictionary[val[0]] = cn
                cn += 1
    return X, y, call_graph, dictionary

def retrunDatasetsNoCG(benchmark,linesFile1,linesFile2):
    X_arr, y_arr = {}, {}
    x_filename = ""
    y_filename = ""
    for i in range(len(linesFile1)):
        if i % 2 == 0:
            x_filename = linesFile1[i]
        else:
            data = ast.literal_eval(linesFile1[i])
            X_arr[x_filename] = data
    for i in range(len(linesFile2)):
        if i % 2 == 0:
            y_filename = linesFile2[i]
        else:
            try:
                #string=linesFile2[i].split(' ')
                #y_arr[y_filename] = float(string[-1])
                y_arr[y_filename] = float(linesFile2[i])
            except:
                print(y_filename)
    X = []
    y = []
    for key in X_arr:
        X.append(X_arr[key])
        y.append(y_arr[key])
        
    cn = 0
    call_graph=call_graph_loop_of(benchmark)
    
    dictionary = {} 
    for key in X[0]:
        #if not any ([x[key] for x in X]):
            #print('All values for {} is zero, skipped'.format(key))
            #continue
        
        #print('Remained feature: {}'.format(key))
        dictionary [key] = cn
        cn += 1
    return X, y, call_graph, dictionary


def raytrace(clf = False):
    """X, y = pd.read_csv(os.path.join(PATH, "datasets", "fc_nonli.txt"), sep=" ", header=None).to_numpy(), \
           pd.read_csv(os.path.join(PATH, "datasets", "raytrace_log.txt"), sep=" ", header=None).to_numpy()"""
    file1 = open(os.path.join(PATH, "datasets", "raytrace_fc_nli_sheng2080.txt"), 'r')
    #file1=open('fc_nonli.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "raytrace_log_sheng2080.txt"), 'r')
    #file2=open('raytrace_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Raytrace",linesFile1,linesFile2)



def pascal_matrix(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "pascal_loop.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "pascal_log_codeworld.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Pascal", linesFile1, linesFile2)

def pascal_matrix_argcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "pascal_fc_nli_argcast.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "pascal_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Pascal", linesFile1, linesFile2)

def pascal_matrix_transcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_pascal.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_pascal.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Pascal_TRANS", linesFile1, linesFile2)
def sieve_transcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_sieve.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_sieve.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Sieve_TRANS", linesFile1, linesFile2)
def richard_transcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_richard.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_richard.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Richard_TRANS", linesFile1, linesFile2)
def scimark_transcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_scimark.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_SOR.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Scimark_TRANS", linesFile1, linesFile2)
def meteor_transcast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_meteor.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_meteor.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Meteor_TRANS", linesFile1, linesFile2)
def nbody(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "nbody_fc_nli.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "nbody_log_thinkpadp17.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Nbody", linesFile1, linesFile2)

def sieve(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "sieve_fc_nli.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "sieve_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Sieve", linesFile1, linesFile2)
def monte_carol(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "fc_nonli_monte.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_monte.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Monte", linesFile1, linesFile2)
def meteor(clf=False):
    file1 = open(os.path.join(PATH, "datasets", "meteor_fc_nonli.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "meteor_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Meteor", linesFile1, linesFile2)
def scimark(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "SOR_fc_nli_parcast.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "SOR_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasets("Scimark", linesFile1, linesFile2)
def monte(clf=False):
    file1 = open(os.path.join(PATH, "datasets", "fc_nonli_monte.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_monte.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Monte", linesFile1, linesFile2)
def scimarkParCast(clf = False):
    file1 = open(os.path.join(PATH, "datasets", "SOR_fc_nli_parcast.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "SOR_log_sheng2080.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Scimark", linesFile1, linesFile2)
def chaosbenchmark():
    file1 = open(os.path.join(PATH, "datasets", "fc_nli_chaos.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_fc_chaos.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Chaos", linesFile1, linesFile2)
def richardbenchmark():
    file1 = open(os.path.join(PATH, "datasets", "fc_nli_richard.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_richard.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Richard", linesFile1, linesFile2)
def pdfconverterchmark():
    file1 = open(os.path.join(PATH, "datasets", "fc_nli_pdf.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_pdf.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Pdf", linesFile1, linesFile2)
def cpu_benchmark():
    file1 = open(os.path.join(PATH, "datasets", "fc_nli_cpu.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_cpu_new.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Cpu", linesFile1, linesFile2)
def benchfirst_benchmark():
    file1 = open(os.path.join(PATH, "datasets", "fc_nli_benchfirst.txt"), 'r')
    #file1=open('pascal_without_loop.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "bechfirst_log.txt"), 'r')
    #file2=open('pascal_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Benchfirst", linesFile1, linesFile2)
def getBenchmarks(bencmarks):
    Xs,ys,call_graphs, dictionarys=[],[],[],[]
    for benchmark in bencmarks:
        if benchmark=="Scimark":
            X, y, call_graph, dictionary =scimarkParCast()
            Xs.append(X)
            ys.append(y)
            call_graphs.append(call_graph)
            dictionarys.append(dictionary)
        elif benchmark=="Pascal":
            X, y, call_graph, dictionary =pascal_matrix_argcast()
            Xs.append(X)
            ys.append(y)
            call_graphs.append(call_graph)
            dictionarys.append(dictionary)
        elif benchmark=="Sieve":
            X, y, call_graph, dictionary =sieve()
            Xs.append(X)
            ys.append(y)
            call_graphs.append(call_graph)
            dictionarys.append(dictionary)
    return Xs,ys,call_graphs,dictionarys
def raytraceParCast(clf = False):
    """X, y = pd.read_csv(os.path.join(PATH, "datasets", "fc_nonli.txt"), sep=" ", header=None).to_numpy(), \
           pd.read_csv(os.path.join(PATH, "datasets", "raytrace_log.txt"), sep=" ", header=None).to_numpy()"""
    file1 = open(os.path.join(PATH, "datasets", "raytrace_fc_nli_parcast.txt"), 'r')
    #file1=open('fc_nonli.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "raytrace_log_sheng2080.txt"), 'r')
    #file2=open('raytrace_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Raytrace",linesFile1,linesFile2)
def raytrace_trans_cast(clf = False):
    """X, y = pd.read_csv(os.path.join(PATH, "datasets", "fc_nonli.txt"), sep=" ", header=None).to_numpy(), \
           pd.read_csv(os.path.join(PATH, "datasets", "raytrace_log.txt"), sep=" ", header=None).to_numpy()"""
    file1 = open(os.path.join(PATH, "datasets", "trans_fc_nli_raytrace.txt"), 'r')
    #file1=open('fc_nonli.txt', 'r')
    linesFile1 = file1.readlines()
    file2 = open(os.path.join(PATH, "datasets", "log_transient_raytrace.txt"), 'r')
    #file2=open('raytrace_log.txt', 'r')
    linesFile2 = file2.readlines()
    return retrunDatasetsNoCG("Raytrace_TRANS",linesFile1,linesFile2)
def raytraceDynamicParCast():
    file1 = open(os.path.join(PATH, "datasets", "feature_mapping.txt"), 'r')
    linesFile1 = file1.readlines()
    filenames,X,bit_strings,y=[],[],[],[]
    for i in range(len(linesFile1)):
        if i % 4 == 0:
            filenames.append(linesFile1[i])
        elif i%4==1:
            data = ast.literal_eval(linesFile1[i])
            
            X.append(data)
        elif i%4==2:
            
            y.append(float(linesFile1[i]))
        elif i%4==3:
            bit_strings.append(linesFile1[i][1:-1])
    dictionary = {} 
    cn=0
    for key in X[0]:
        dictionary [key] = cn
        cn += 1
    return X,y,filenames,bit_strings,dictionary
def load_data_Sets_X_Y_dictionary(benchmark):
    X, y, call_graph, dictionary =None,None,None,None
    if benchmark=="Raytrace": 
        X, y, call_graph, dictionary=raytraceParCast()
    elif benchmark=="Scimark":
        X, y, call_graph, dictionary=scimarkParCast()
    elif benchmark=="Sieve":
        X, y, call_graph, dictionary=sieve()
    elif benchmark=='Nbody':
        X, y, call_graph, dictionary = nbody()
    elif benchmark=='Pascal':
        X, y, call_graph, dictionary = pascal_matrix_argcast()
    elif benchmark=='Meteor':
        X, y, call_graph, dictionary = meteor()
    elif benchmark=='Chaos':
        X,y,call_graph,dictionary=chaosbenchmark()
    elif benchmark=="Monte":
        X,y,call_graph,dictionary=monte()
    elif benchmark=="Richard":
        X,y,call_graph,dictionary=richardbenchmark()
    elif benchmark=="Pdf":
        X,y,call_graph,dictionary=pdfconverterchmark()
    elif benchmark=="Benchfirst":
        X,y,call_graph,dictionary=benchfirst_benchmark()
    elif benchmark=="Cpu":
        X,y,call_graph,dictionary=cpu_benchmark()
    
    int_to_str = {}
    for key in dictionary:
        int_to_str[dictionary[key]] = key
    # print(int_to_str)
    node = []
    for x in X:
        temp = []
        for key in range(len(dictionary)):
            temp.append(x[int_to_str[key]])
        node.append(temp)
    X_node = np.array(node)
    y = np.array(y).reshape(-1, 1)
    return (X_node,y)
if __name__ == "__main__":
    #print(PATH)

    if scimark() == scimarkNoCG():
        print ("The same")
    else:
        print('Different')
    
