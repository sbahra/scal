{
  'includes': [
    'common.gypi',
  ],
  'targets': [
    {
      'target_name': 'libscal',
      'type': 'static_library',
      'sources': [
        'src/util/atomic_value128.h',
        'src/util/atomic_value64_base.h',
        'src/util/atomic_value64_no_offset.h',
        'src/util/atomic_value64_offset.h',
        'src/util/atomic_value.h',
        'src/util/atomic_value_new.h',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/barrier.h',
        'src/util/bitmap.h',
        'src/util/malloc-compat.h',
        'src/util/operation_logger.h',
        'src/util/platform.h',
        'src/util/random.h',
        'src/util/random.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/time.h',
        'src/util/workloads.h',
        'src/util/workloads.cc',
      ],
    },
    {
      'target_name': 'computational-load',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/computational-load/computational-load.cc',
      ],
    },
    {
      'target_name': 'mm-harness',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/mm/mm.cc',
      ],
    },
    {
      'target_name': 'prodcon-base',
      'type': 'static_library',
      'libraries': [ '<@(default_libraries)' ],
      'sources': [
        'src/benchmark/common.h',
        'src/benchmark/common.cc',
        'src/util/allocation.h',
        'src/util/allocation.cc',
        'src/util/threadlocals.h',
        'src/util/threadlocals.cc',
        'src/util/workloads.h',
        'src/util/workloads.cc',
        'src/benchmark/prodcon/prodcon.cc',
      ],
    },
    {
      'target_name': 'seqalt-base',
      'type': 'static_library',
      'sources': [
        'src/benchmark/common.cc',
        'src/benchmark/seqalt/seqalt.cc',
      ],
    },
    {
      'target_name': 'prodcon-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ms',
      ],
    },
    {
      'target_name': 'prodcon-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:treiber',
      ],
    },
    {
      'target_name': 'prodcon-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:kstack',
      ],
    },
    {
      'target_name': 'prodcon-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-kstack',
      ],
    },
    {
      'target_name': 'prodcon-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dds-1random-ms',
      ],
    },
    {
      'target_name': 'prodcon-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'prodcon-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'prodcon-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'prodcon-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:fc',
      ],
    },
    {
      'target_name': 'prodcon-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:rd',
      ],
    },
    {
      'target_name': 'prodcon-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:sq',
      ],
    },
    {
      'target_name': 'prodcon-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:us-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:bs-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dds-ms',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-ms-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dds-ms-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dds-treiber-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dds-treiber-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-ms-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dyn-dds-ms-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-treiber-nonlinempty',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dyn-dds-treiber-nonlinempty',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dyn-dds-ms',
      ],
    },
    #{
    #  'target_name': 'prodcon-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'prodcon-base',
    #    'glue.gypi:wf-queue',
    #  ],
    #},
    {
      'target_name': 'seqalt-ll-dyn-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-dyn-dds-ms',
      ],
    },
    {
      'target_name': 'prodcon-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'seqalt-ll-dyn-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-dyn-dds-treiber',
      ],
    },
    {
      'target_name': 'prodcon-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:lcrq',
      ],
    },
    {
      'target_name': 'seqalt-lcrq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:lcrq',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'prodcon-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'prodcon-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ts-cas-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ts-interval-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'prodcon-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'prodcon-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:rts-queue',
      ],
    },
    {
      'target_name': 'prodcon-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:cts-queue',
      ],
    },
    {
      'target_name': 'prodcon-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:eb-stack',
      ],
    },
    {
      'target_name': 'prodcon-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:lb-stack',
      ],
    },
    {
      'target_name': 'prodcon-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:lb-queue',
      ],
    },
    {
      'target_name': 'prodcon-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:lru-dds-ms',
      ],
    },
    {
      'target_name': 'prodcon-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:lru-dds-treiber-stack',
      ],
    },
    {
      'target_name': 'seqalt-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ms',
      ],
    },
    {
      'target_name': 'seqalt-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:treiber',
      ],
    },
    {
      'target_name': 'seqalt-dds-partrr-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:dds-partrr-ms',
      ],
    },
    {
      'target_name': 'seqalt-dds-partrr-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:dds-partrr-treiber',
      ],
    },
    {
      'target_name': 'seqalt-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:kstack',
      ],
    },
    {
      'target_name': 'seqalt-ll-kstack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-kstack',
      ],
    },
    {
      'target_name': 'seqalt-dds-1random-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:dds-1random-ms',
      ],
    },
    {
      'target_name': 'seqalt-dds-1random-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:dds-1random-treiber',
      ],
    },
    {
      'target_name': 'seqalt-fc',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:fc',
      ],
    },
    {
      'target_name': 'seqalt-rd',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:rd',
      ],
    },
    {
      'target_name': 'seqalt-sq',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:sq',
      ],
    },
    {
      'target_name': 'seqalt-bs-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'prodcon-base',
        'glue.gypi:bs-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:us-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-ll-us-kfifo',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-us-kfifo',
      ],
    },
    {
      'target_name': 'seqalt-ll-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-dds-ms',
      ],
    },
    {
      'target_name': 'seqalt-ll-dds-treiber',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ll-dds-treiber',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-cas-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-cas-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-stutter-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-stutter-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-interval-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-interval-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-atomic-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-atomic-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-hardware-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-hardware-stack',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-cas-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-cas-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-stutter-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-stutter-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-interval-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-interval-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-atomic-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-atomic-queue',
      ],
    },
    {
      'target_name': 'seqalt-hc-ts-hardware-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:hc-ts-hardware-queue',
      ],
    },
    {
      'target_name': 'seqalt-ts-cas-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ts-cas-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-stutter-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ts-stutter-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-interval-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ts-interval-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-atomic-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ts-atomic-deque',
      ],
    },
    {
      'target_name': 'seqalt-ts-hardware-deque',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:ts-hardware-deque',
      ],
    },
    {
      'target_name': 'seqalt-rts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:rts-queue',
      ],
    },
    {
      'target_name': 'seqalt-cts-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:cts-queue',
      ],
    },
    {
      'target_name': 'seqalt-eb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:eb-stack',
      ],
    },
    {
      'target_name': 'seqalt-lb-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:lb-stack',
      ],
    },
    {
      'target_name': 'seqalt-lb-queue',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:lb-queue',
      ],
    },
    #{
    #  'target_name': 'seqalt-wf-queue',
    #  'type': 'executable',
    #  'libraries': [ '<@(default_libraries)' ],
    #  'dependencies': [
    #    'libscal',
    #    'seqalt-base',
    #    'glue.gypi:wf-queue',
    #  ],
    #},
    {
      'target_name': 'seqalt-lru-dds-ms',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:lru-dds-ms',
      ],
    },
    {
      'target_name': 'seqalt-lru-dds-treiber-stack',
      'type': 'executable',
      'libraries': [ '<@(default_libraries)' ],
      'dependencies': [
        'libscal',
        'seqalt-base',
        'glue.gypi:lru-dds-treiber-stack',
      ],
    }

  ]
}
